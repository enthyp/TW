package none.config;

import none.config.elements.*;
import none.workers.SamplingType;
import none.workers.WorkerType;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class SimpleConfigFactory implements IConfigFactory {

    @Override
    public List<IConfiguration> getAll() {
        // Not such a great idea after all...
        IConfiguration seedConfig = new SimpleConfiguration();
        List<IConfiguration> allConfigs = new ArrayList<IConfiguration>() {{
            add(seedConfig);
        }};

        List<List<? extends ConfigElement>> possibilities = new ArrayList<List<? extends ConfigElement>>() {{
            add(bufferSizes);
            add(bufferTypes);
            add(samplingTypes);
            add(workerCounts);
        }};

        for (List<? extends ConfigElement> list : possibilities) {
            List<IConfiguration> enhancedConfigs = new ArrayList<>();
            for (IConfiguration config : allConfigs) {
                for (int i = 0; i < list.size(); i++) {
                    IConfiguration cConfig = new SimpleConfiguration((SimpleConfiguration) config);
                    cConfig.accept(list.get(i));
                    enhancedConfigs.add(cConfig);
                }
            }
            allConfigs = enhancedConfigs;
        }

        return allConfigs;
    }

    private static List<BufferSize> bufferSizes = new ArrayList<BufferSize>() {{
        add(new BufferSize(10000));
        add(new BufferSize(100000));
    }};

    private static List<BufferType> bufferTypes = new ArrayList<BufferType>() {{
        //add(new BufferType(none.buffers.BufferType.NAIVE));
        add(new BufferType(none.buffers.BufferType.FAIR));
    }};

    private static List<WorkerCount> workerCounts = new ArrayList<WorkerCount>() {{
        add(new WorkerCount(new HashMap<WorkerType, Integer>() {{
            put(WorkerType.CONSUMER, 100);
            put(WorkerType.PRODUCER, 100);
        }}));
        add(new WorkerCount(new HashMap<WorkerType, Integer>() {{
            put(WorkerType.CONSUMER, 1000);
            put(WorkerType.PRODUCER, 1000);
        }}));
    }};

    private static List<SamplingVariant> samplingTypes = new ArrayList<SamplingVariant>() {{
        add(new SamplingVariant(SamplingType.UNIFORM));
        add(new SamplingVariant(SamplingType.GEOMETRIC));
    }};
}
