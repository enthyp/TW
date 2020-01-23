import Buffer.Item
import Consumer.Get
import Producer.Put
import akka.actor.typed.{ActorRef, ActorSystem, Behavior}
import akka.actor.typed.scaladsl.Behaviors

import scala.concurrent.Await
import scala.concurrent.duration.Duration

// Assignment:
// - implement solution to the producers/consumers problem
//   using the actor model / Akka
// - test the correctness of the created solution for multiple
//   producers and consumers
// Hint: use akka.actor.Stash

sealed trait Msg

object Producer {

  case class Put(x: Long) extends Msg

  def apply(name: String, buf: ActorRef[Msg], numMessages: Int): Behavior[Msg] = Behaviors.setup { context =>
    for (i <- 1 to numMessages) {
      buf ! Put(i)
      context.log.info(s"PUT $i")
    }
    Behaviors.stopped
  }
}

object Consumer {

  case class Get(sender: ActorRef[Msg]) extends Msg

  def apply(name: String, buf: ActorRef[Msg], parent: ActorRef[Msg]): Behavior[Msg] = Behaviors.setup { context =>
    buf ! Get(context.self)

    Behaviors.receive { (context, msg) =>
      msg match {
        case Item(x) =>
          context.log.info(s"$name received $x")
          parent ! msg
          buf ! Get(context.self)
          Behaviors.same
      }
    }
  }
}

object Buffer {

  case class Item(x: Long) extends Msg

  def apply(n: Int): Behavior[Msg] = {
    run(0, n, new Array[Long](n))
  }

  def run(count: Int, max: Int, buf: Array[Long]): Behavior[Msg] = Behaviors.withStash(20000) { buffer =>
    Behaviors.receive { (context, msg) =>
      msg match {
        case Put(x) if (count < max) =>
          buf(count) = x
          buffer.unstashAll(run(count + 1, max, buf))
        case Put(x) =>
          if (!buffer.isFull)
            buffer.stash(msg)
          else
            context.log.info("Dropped PUT message!")

          Behaviors.same
        case Get(sender) if (count > 0) =>
          sender ! Item(buf(count - 1))
          run(count - 1, max, buf)
        case Get(sender) =>
          if (!buffer.isFull)
            buffer.stash(msg)
          else
            context.log.info("Dropped GET message!")
          Behaviors.same
      }
    }
  }
}

object Supervisor {

  final case class Init(numConsumers: Int, numProducers: Int, numMessages: Int) extends Msg
  final case class Shutdown() extends Msg

  def apply(): Behavior[Msg] = Behaviors.receive { (context, msg) =>
    msg match {
      case Init(numConsumers, numProducers, numMessages) =>
        val consumers = new Array[ActorRef[Msg]](numConsumers)
        val producers = new Array[ActorRef[Msg]](numProducers)
        val buffer = context.spawn(Buffer(numMessages), "Buffer")

        // Run consumers and then producers.
        for (i <- consumers.indices) {
          val name = s"Consumer$i"
          consumers(i) = context.spawn(Consumer(name, buffer, context.self), name)
        }

        for (i <- producers.indices) {
          val name = s"Producer$i"
          consumers(i) = context.spawn(Producer(name, buffer, numMessages), name)
        }

        awaitTermination(numMessages)
      case _ => Behaviors.ignore
    }
  }

  def awaitTermination(numMessages: Int): Behavior[Msg] = Behaviors.receive { (context, msg) =>
    msg match {
      case _: Item if (numMessages > 0) =>
        awaitTermination(numMessages - 1)
      case _: Item =>
        context.log.info("Supervisor shutdown")
        Behaviors.stopped
    }
  }
}

object Main extends App {
  val system: ActorSystem[Supervisor.Init] = ActorSystem(Supervisor(), "ProdKons")
  system ! Supervisor.Init(10, 10, 1000)
  Await.result(system.whenTerminated, Duration.Inf)
}