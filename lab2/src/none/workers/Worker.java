package none.workers;

import none.buffers.IBuffer;
import none.experiments.Logger;

import java.util.concurrent.atomic.AtomicBoolean;

public abstract class Worker extends Thread {
    protected AtomicBoolean working;
    protected int max;
    protected IBuffer buffer;
    protected Sampler sampler;
    protected SamplingType type;
    protected Logger logger;

    public Worker(IBuffer buffer, SamplingType type) {
        this.max = buffer.getLength() / 2;
        this.buffer = buffer;
        this.type = type;
        this.sampler = new Sampler();
    }

    public void setWorking(AtomicBoolean working) {
        this.working = working;
    }

    public void setLogger(Logger logger) {
        this.logger = logger;
    }

    public void run() {
        while (working.get()) {
            int cnt = sampler.sample(max, type);
            try {
                long startTime = System.nanoTime();
                engage(cnt);
                long estimatedTime = System.nanoTime() - startTime;
                logger.log(WorkerType.CONSUMER, cnt, estimatedTime);
            } catch (InterruptedException e) { // Just exit. }
            }
        }
    }

    public abstract void engage(int count) throws InterruptedException;
}
