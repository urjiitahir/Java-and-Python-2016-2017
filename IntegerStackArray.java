package StackGeneric;

public class IntegerStackArray implements Stack<Integer>
{
    private Integer data[];
    private int depth;
    private static final int MAXSIZE = 1000;

    public IntegerStackArray(){
        data = new Integer[MAXSIZE];
        depth = 0;
    }

    /* ... */

    public void push(Integer value){
        //data[depth++] = value;
 	
	    try{	    
	    data[depth++] = value;
	    
	    	    }
		 
	 catch(ArrayIndexOutOfBoundsException e){
		 System.out.println("Incompatible with max size of array: ERROR    ");
		 
	 }

    }

    public Integer pop(){
        return data[--depth];
    }

    public Integer peek(){
        return data[depth-1];
    }
}

