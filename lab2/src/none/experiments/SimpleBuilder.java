package none.experiments;

import none.buffers.FairBuffer;
import none.buffers.IBuffer;
import none.buffers.NaiveBuffer;
import none.config.IConfiguration;
import none.buffers.BufferType;
import none.workers.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

// TODO: exception handling in general!!!

public class SimpleBuilder implements IBuilder {

    private int bufferSize;
    private BufferType bufferType;
    private SamplingType samplingType;
    private Map<WorkerType, Integer> workerCounts;

    @Override
    public void setup(IConfiguration config) {
        config.visitSimpleBuilder(this);
    }

    @Override
    public Experiment build() {
        List<Worker> workers = new ArrayList<>();

        IBuffer buffer;
        if (bufferType == BufferType.FAIR) {
            buffer = new FairBuffer(bufferSize);
        } else if (bufferType == BufferType.NAIVE) {
            buffer = new NaiveBuffer(bufferSize);
        } else {
            System.out.println("Unknown buffer type, defaulting to naive...");
            buffer = new FairBuffer(bufferSize);
        }

        for (Map.Entry<WorkerType, Integer> kv : workerCounts.entrySet()) {
            for (int i = 0; i < kv.getValue(); i++) {
                if (kv.getKey() == WorkerType.PRODUCER) {
                    workers.add(new Producer(buffer, samplingType));
                } else {
                    workers.add(new Consumer(buffer, samplingType));
                }
            }
        }

        Logger logger = new Logger();
        logger.setup(bufferSize, bufferType, samplingType, workerCounts);

        return new Experiment(workers, logger);
    }

    public void setBufferSize(int bufferSize) {
        this.bufferSize = bufferSize;
    }

    public void setBufferType(BufferType bufferType) {
        this.bufferType = bufferType;
    }

    public void setSamplingType(SamplingType samplingType) {
        this.samplingType = samplingType;
    }

    public void setWorkerCounts(Map<WorkerType, Integer> workerCounts) {
        this.workerCounts = workerCounts;
    }
}
