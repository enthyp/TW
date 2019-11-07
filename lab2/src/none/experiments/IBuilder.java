package none.experiments;

import none.config.IConfiguration;

public interface IBuilder {
    void setup(IConfiguration config);
    Experiment build();
}
