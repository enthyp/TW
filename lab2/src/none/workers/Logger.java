package none.workers;

import none.buffers.BufferType;
import none.experiments.Experiment;

import java.io.File;
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

        File logDir = new File("./logs/");
        if( !(logDir.exists()) )
            logDir.mkdir();

        try {
            FileHandler fh = new FileHandler("logs/threads.csv");
            fh.setFormatter(new SimpleFormatter() {
                private static final String format = "%1$s\n";

                @Override
                public synchronized String format(LogRecord lr) {
                    return String.format(format, lr.getMessage());
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

        String format = "%1$d,%2$s,%3$d,%4$s,%5$b,%6$s,%7$d\n";
        String msg = String.format(format, bufferSize, consProd, units, counts, isFair, randomization, time);
        logger.log(Level.ALL, msg);
    }
}
