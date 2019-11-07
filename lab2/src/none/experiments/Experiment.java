package none.experiments;

import none.workers.Worker;

import java.util.List;

public class Experiment {
    private List<Worker> workers;

    public Experiment(List<Worker> workers) {
        this.workers = workers;
    }

    public void run() {
        for (Worker w : workers) {
            w.start();
        }

        try {
            for (Worker w : workers) {
                w.join();
            }
        } catch (InterruptedException e) {
            System.out.println("Interrupted, terminating immediately.");
        }
    }
}
