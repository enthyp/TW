package none;

import none.config.IConfigFactory;
import none.config.SimpleConfigFactory;
import none.config.IConfiguration;
import none.experiments.Experiment;
import none.experiments.IBuilder;
import none.experiments.SimpleBuilder;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        IBuilder builder = new SimpleBuilder();
        IConfigFactory factory = new SimpleConfigFactory();
        List<IConfiguration> configs = factory.getAll();

        for (IConfiguration config : configs) {
            builder.setup(config);
            Experiment experiment = builder.build();
            experiment.run();

            try {
                Thread.sleep(1);
            } catch (InterruptedException e ) {
                System.out.println("Exiting abruptly.");
                System.exit(1);
            }

            experiment.stop();
        }
    }
}
