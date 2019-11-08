package none.buffers;


public class NaiveBuffer implements IBuffer {
    private int size;
    private int length;

    public NaiveBuffer(int M) {
        this.size = 0;
        this.length = 2 * M;
    }

    public synchronized void put(int count) throws InterruptedException {
        while (this.size + count > length) {
            wait();
        }

        this.size += count;
        notifyAll();
    }

    public synchronized void take(int count) throws InterruptedException {
        while (this.size - count < 0) {
            wait();
        }

        this.size -= count;
        notifyAll();
    }

    public int getLength() {
        return this.length;
    }
}

