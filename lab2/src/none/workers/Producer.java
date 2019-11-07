package none.workers;

import none.buffers.IBuffer;

public class Producer extends Worker {

    private SamplingType type;

    public Producer(int n, IBuffer buffer, SamplingType type) {
        super(n, buffer);
        this.type = type;
    }

    public void run() {

    }
}
