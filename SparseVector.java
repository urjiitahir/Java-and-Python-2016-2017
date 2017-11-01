import java.util.Arrays;

public class SparseVector extends Vector {  
    
    private int positions[];
    private double values[];

    public SparseVector( int length ) {
        this.length = length;
        positions = new int[0];
        values = new double[0];
    }

    public SparseVector( int length, int positions[], double values[]) { 
        if ( positions.length != values.length ) {
            System.out.println("`positions' and `values' must have the same length");
            throw new RuntimeException();
        }
        this.length = length;
        this.positions = positions;
        this.values = values;
    }


    public double get(int i) {
        if ( i >= length || i < 0) {
            throw new IndexOutOfBoundsException();
        }
            
        for( int j = 0 ; j < positions.length ; j++) {
            if(i == positions[j]) {
                return values[j];
            }
        }
        return 0;
    }
