package none.workers;

import none.buffers.IBuffer;

import java.util.concurrent.atomic.AtomicBoolean;

public abstract class Worker extends Thread {
    protected AtomicBoolean working;
    protected int max;
    protected IBuffer buffer;
    protected Sampler sampler;
    protected SamplingType type;
    protected Logger logger;

    public Worker(IBuffer buffer, SamplingType type, Logger logger) {
        this.sampler = new Sampler();
        this.max = buffer.getLength() / 2;
        this.buffer = buffer;
        this.type = type;
        this.logger = logger;
    }

    public void setWorking(AtomicBoolean working) {
        this.working = working;
    }

    public void run() {
        while (working.get()) {
            int cnt = sampler.sample(max, type);
            try {
                engage(cnt);
            } catch (InterruptedException e) { /* Just exit. */ }
        }
    }

    public abstract void engage(int count) throws InterruptedException;
}
