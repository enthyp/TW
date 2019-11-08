package none.experiments;

import none.workers.Worker;

import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;


public class Experiment {
    private AtomicBoolean working = new AtomicBoolean(false);
    private List<Worker> workers;


    public Experiment(List<Worker> workers) {
        this.workers = workers;
        for (Worker w : this.workers) {
            w.setWorking(working);
        }
    }

    public void run() {
        working.set(true);
        for (Worker w : workers) {
            w.start();
        }
    }

    public void stop() {
        working.set(false);
        for (Worker w : workers) {
            try {
                w.interrupt();
                w.join();
            }
            catch (InterruptedException e) { /* ... */ }
        }
    }
}
