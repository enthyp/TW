package none.workers;

import none.buffers.IBuffer;

public class Consumer extends Worker {

    public Consumer(IBuffer buffer, SamplingType type, Logger logger) {
        super(buffer, type, logger);
    }

    @Override
    public void engage(int count) {
        try {
            long startTime = System.nanoTime();
            buffer.take(count);
            long estimatedTime = System.nanoTime() - startTime;
            logger.log(WorkerType.CONSUMER, count, estimatedTime);
        } catch (InterruptedException e) {
            // Just quit, do not log.
        }
    }
}
