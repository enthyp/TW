package none.config.elements;

import none.config.SimpleConfiguration;
import none.workers.SamplingType;

public class SamplingVariant implements ConfigElement {
    public SamplingType value;

    public SamplingVariant(SamplingType value) {
        this.value = value;
    }

    @Override
    public void visitSimpleConfiguration(SimpleConfiguration configuration) {
        configuration.setSamplingVariant(value);
    }
}
