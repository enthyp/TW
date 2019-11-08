package none.workers;

import none.buffers.IBuffer;

public class Producer extends Worker {

    public Producer(IBuffer buffer, SamplingType type) {
        super(buffer, type);
    }

    @Override
    public void engage(int count) throws InterruptedException {
        buffer.put(count);
    }
}
