package none.workers;


import none.buffers.IBuffer;

public class Consumer extends Worker {

    public Consumer(IBuffer buffer, SamplingType type) {
        super(buffer, type);
    }

    @Override
    public void engage(int count) throws InterruptedException {
        buffer.take(count);
    }
}
