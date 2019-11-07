package none.buffers;

public class FairBuffer implements IBuffer {
    private int size;
    private int length;

    public FairBuffer(int M) {
        this.size = 0;
        this.length = 2 * M;
    }

    @Override
    public void put(int count) throws InterruptedException {

    }

    @Override
    public void take(int count) throws InterruptedException {

    }

    @Override
    public int getLength() {
        return 0;
    }
}
