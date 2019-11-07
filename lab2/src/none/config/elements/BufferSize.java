package none.config.elements;

import none.config.SimpleConfiguration;

public class BufferSize implements ConfigElement {
    public int value;

    public BufferSize(int value) {
        this.value = value;
    }

    @Override
    public void visitSimpleConfiguration(SimpleConfiguration configuration) {
        configuration.setBufferSize(value);
    }
}
