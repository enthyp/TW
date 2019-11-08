package none.buffers;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class FairBuffer implements IBuffer {
    private int size;
    private int length;

    private Lock lock = new ReentrantLock();
    private boolean canProduce = true, canConsume = true;  // means: can become first.
    private Condition firstConsumer = lock.newCondition();
    private Condition restConsumers = lock.newCondition();
    private Condition firstProducer = lock.newCondition();
    private Condition restProducers = lock.newCondition();

    public FairBuffer(int M) {
        this.size = 0;
        this.length = 2 * M;
    }

    @Override
    public void put(int count) throws InterruptedException {
        lock.lock();
        try {
            // I think an IF would do.
            while (!canProduce) {
                restProducers.await();
            }

            while (length - size < count) {
                firstProducer.await();
            }

            size += count;
            canProduce = true;
            restProducers.signal();
            firstConsumer.signal();
        } finally {
            lock.unlock();
        }
    }

    @Override
    public void take(int count) throws InterruptedException {
        lock.lock();
        try {
            // I think an IF would do.
            while (!canConsume) {
                restConsumers.await();
            }

            while (size < count) {
                firstProducer.await();
            }

            size -= count;
            canConsume = true;
            restConsumers.signal();
            firstProducer.signal();
        } finally {
            lock.unlock();
        }
    }

    @Override
    public int getLength() {
        return this.length;
    }
}
