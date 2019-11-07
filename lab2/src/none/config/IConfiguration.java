package none.config;

import none.config.elements.ConfigElement;
import none.experiments.SimpleBuilder;

public interface IConfiguration {
    void visitSimpleBuilder(SimpleBuilder b);
    // ...other builders possibly, the Visitor pattern.

    void accept(ConfigElement element);
    // ...but can be visited too!
}
