package none.config.elements;

import none.config.SimpleConfiguration;

public class LoopCount implements ConfigElement {
    public int value;

    public LoopCount(int value) {
        this.value = value;
    }

    @Override
    public void visitSimpleConfiguration(SimpleConfiguration configuration) {
        configuration.setLoopCount(value);
    }
}
