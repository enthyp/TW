package none.config.elements;

import none.config.SimpleConfiguration;

public class BufferType implements ConfigElement {
    public none.buffers.BufferType value;

    public BufferType(none.buffers.BufferType value) {
        this.value = value;
    }

    @Override
    public void visitSimpleConfiguration(SimpleConfiguration configuration) {
        configuration.setBufferType(value);
    }
}
