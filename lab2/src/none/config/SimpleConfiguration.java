package none.config;


import none.buffers.*;
import none.config.elements.ConfigElement;
import none.workers.*;
import none.experiments.SimpleBuilder;

import java.util.Map;

public class SimpleConfiguration implements IConfiguration {

    private int bufferSize;
    private BufferType bufferType;
    private SamplingType samplingVariant;
    private Map<WorkerType, Integer> workerCount;

    public SimpleConfiguration() {};

    public SimpleConfiguration(SimpleConfiguration other) {
        bufferSize = other.bufferSize;
        bufferType = other.bufferType;
        samplingVariant = other.samplingVariant;
        workerCount = other.workerCount;
    }

    @Override
    public void visitSimpleBuilder(SimpleBuilder b) {
        b.setBufferSize(bufferSize);
        b.setBufferType(bufferType);
        b.setSamplingType(samplingVariant);
        b.setWorkerCounts(workerCount);
    }

    @Override
    public void accept(ConfigElement element) {
        element.visitSimpleConfiguration(this);
    }

    public void setBufferSize(int bufferSize) {
        this.bufferSize = bufferSize;
    }

    public void setBufferType(BufferType bufferType) {
        this.bufferType = bufferType;
    }

    public void setSamplingVariant(SamplingType samplingVariant) {
        this.samplingVariant = samplingVariant;
    }

    public void setWorkerCount(Map<WorkerType, Integer> workerCount) {
        this.workerCount = workerCount;
    }

    @Override
    public String toString() {
        return "SimpleConfiguration{" +
                "bufferSize=" + bufferSize +
                ", bufferType=" + bufferType +
                ", samplingVariant=" + samplingVariant +
                ", workerCount=" + workerCount +
                '}';
    }
}
