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
    private int loopCount;

    public SimpleConfiguration() {};

    public SimpleConfiguration(SimpleConfiguration other) {
        bufferSize = other.bufferSize;
        bufferType = other.bufferType;
        samplingVariant = other.samplingVariant;
        workerCount = other.workerCount;
        loopCount = other.loopCount;
    }

    @Override
    public void visitSimpleBuilder(SimpleBuilder b) {
        b.setBufferSize(bufferSize);
        b.setBufferType(bufferType);
        b.setSamplingType(samplingVariant);
        b.setWorkerCounts(workerCount);
        b.setLoopCount(loopCount);
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

    public void setLoopCount(int loopCount) {
        this.loopCount = loopCount;
    }
}
