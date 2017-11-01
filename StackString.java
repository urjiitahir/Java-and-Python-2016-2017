import StackGeneric.*;
public class StackString implements Stack<String>{

	//PROBLEM #6
	
// constuctor makes empty string
// push method, add string

// pop method takes away character from string

//peek returns last character

//test file to show examples, use a simple for loop

private String str = " ";

public static void main(String [] args){ 

String string = "Urjii Tahir";
System.out.println("result 1:  ");
System.out.println(string.substring(0,2));
System.out.println("\n");

String string1 = "Urjii Tahir";
System.out.println("result 2:  ");
System.out.println(string.substring(0,7));
System.out.println("\n");


String string2 = "Urjii Tahir";
System.out.println("result 3:  ");
System.out.println(string.substring(0,8));
System.out.println("\n");

}


public String emptString(){
	return str;

}	
	 
public void push(String value){
        
	 str+=value;
	 }

 public String pop(){

	String popT;
        popT = str.substring(str.length()-1);
	str = str.substring(0, str.length()-1);
	return popT;
        

	}

public String peek(){
	String t;
	t = str.substring(str.length()-1);
	return t;
	}


}


