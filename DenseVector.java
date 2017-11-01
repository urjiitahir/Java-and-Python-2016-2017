public class DenseVector extends Vector {  
    
    private double data[];

    public DenseVector(int length) {
        data = new double[length];
        this.length = length;
    }

    public DenseVector(double data[]){
        this.data = data;
        this.length = data.length;
    }

    public double get(int i) {
        if(i < 0 || i >= length) {
            throw new IndexOutOfBoundsException();
        }

        return data[i];
    }

    public void set(int i, double value) {
        if(i < 0 || i >= length ) {
            throw new IndexOutOfBoundsException();
        }

        data[i] = value;
    }
}
