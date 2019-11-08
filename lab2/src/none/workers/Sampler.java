package none.workers;

import java.util.Random;

public class Sampler {
    private Random rand = new Random(0);
    private double lambda = 1.;

    public int sample(int max, SamplingType type) {
        if (type == SamplingType.GEOMETRIC) {
            int val = (int)(Math.log(1 - rand.nextDouble())/(-lambda));
            return Math.min(val, max);
        } else {
            // Default to UNIFORM.
            return rand.nextInt(max) + 1;
        }
    }
}
