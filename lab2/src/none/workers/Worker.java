package none.workers;

import none.buffers.IBuffer;

public abstract class Worker extends Thread {
    private int nTimes;
    private int max;
    private IBuffer buffer;

    public Worker(int n, IBuffer buffer) {
        this.nTimes = n;
        this.max = buffer.getLength() / 2;
        this.buffer = buffer;
    }

    public abstract void run();
}
