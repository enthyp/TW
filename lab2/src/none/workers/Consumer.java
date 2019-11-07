package none.workers;

import none.buffers.IBuffer;

public class Consumer extends Worker {

    private SamplingType type;

    public Consumer(int n, IBuffer buffer, SamplingType type) {
        super(n, buffer);
        this.type = type;
    }


    public void run() {

    }
}
