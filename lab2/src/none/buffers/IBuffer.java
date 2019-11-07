package none.buffers;

public interface IBuffer {
    void put(int count) throws InterruptedException;
    void take(int count) throws InterruptedException;
    int getLength();
}
