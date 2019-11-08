package none.workers;

import none.buffers.IBuffer;

public class Producer extends Worker {

    public Producer(IBuffer buffer, SamplingType type, Logger logger) {
        super(buffer, type, logger);
    }

    @Override
    public void engage(int count) {
        try {
            long startTime = System.nanoTime();
            buffer.put(count);
            long estimatedTime = System.nanoTime() - startTime;
            logger.log(WorkerType.PRODUCER, count, estimatedTime);
        } catch (InterruptedException e) {
            // Just quit, do not log.
        }
    }
}
