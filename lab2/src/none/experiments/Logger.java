package none.experiments;

import none.buffers.BufferType;
import none.workers.SamplingType;
import none.workers.WorkerType;

import java.io.IOException;
import java.util.Map;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.LogRecord;
import java.util.logging.SimpleFormatter;

public class Logger {
    private static java.util.logging.Logger logger = getLogger();

    private static java.util.logging.Logger getLogger() {
        java.util.logging.Logger logger =
                java.util.logging.Logger.getLogger(Experiment.class.getName());

        try {
            FileHandler fh = new FileHandler("logs/threads.csv");
            fh.setFormatter(new SimpleFormatter() {
                private static final String format = "%1$d,%2$s,%3$d,%4$b,%5$s,%6$d";

                @Override
                public synchronized String format(LogRecord lr) {
                    return String.format(format, lr.getParameters());
                }
            });
            fh.setLevel(Level.ALL);
            logger.addHandler(fh);
        } catch (IOException e) {
            System.out.println("Failed to initialize logger!");
            System.exit(1);
        }

        return logger;
    }

    private int bufferSize;
    private BufferType bufferType;
    private SamplingType samplingType;
    private Map<WorkerType, Integer> workerCounts;

    public void setup(int bufferSize,
                      BufferType bufferType,
                      SamplingType samplingType,
                      Map<WorkerType, Integer> workerCounts) {
        this.bufferSize = bufferSize;
        this.bufferType = bufferType;
        this.samplingType = samplingType;
        this.workerCounts = workerCounts;
    }

    public void log(WorkerType type, int units, long time) {
        LogRecord lr = new LogRecord(Level.ALL, "");
        String consProd = (type == WorkerType.CONSUMER ? "CONS" : "PROD");
        String counts = String.format("%d+%d", workerCounts.get(WorkerType.CONSUMER), workerCounts.get(WorkerType.PRODUCER));
        boolean isFair = (bufferType == BufferType.FAIR);
        String randomization = samplingType.name();

        Object[] params = {bufferSize, consProd, units, counts, isFair, randomization, time};
        lr.setParameters(params);
        logger.log(lr);
    }
}
