package none;

import none.config.SimpleConfiguration;
import none.config.IConfiguration;
import none.experiments.Experiment;
import none.experiments.IBuilder;
import none.experiments.SimpleBuilder;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        IBuilder builder = new SimpleBuilder();
        List<IConfiguration> configs = SimpleConfiguration.getAll();

        for (IConfiguration config : configs) {
            builder.setup(config);
            Experiment experiment = builder.build();
            experiment.run();
        }
    }
}
