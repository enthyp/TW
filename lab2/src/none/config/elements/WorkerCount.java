package none.config.elements;

import none.config.SimpleConfiguration;
import none.workers.WorkerType;

import java.util.Map;

public class WorkerCount implements ConfigElement {
    public Map<WorkerType, Integer> value;

    public WorkerCount(Map<WorkerType, Integer> value) {
        this.value = value;
    }

    @Override
    public void visitSimpleConfiguration(SimpleConfiguration configuration) {
        configuration.setWorkerCount(value);
    }
}
