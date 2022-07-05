package java_01;

public class Array {
	public static void main(String[] args) {
		int[] values = new int[4];
		values[0]=10;
		values[1]=20;
		values[2]=30;
		values[3]=40;
		
		System.out.println(values[0]);
		System.out.println(values[1]);
		System.out.println(values[2]);
		System.out.println(values[3]);
//M-2
		int[] numbers = {2,3,5,9,4,8};
		System.out.println(numbers[3]);
		System.out.println(numbers[0]);
//without given attribute
		int[] num = new int[3];
		System.out.println(num[0]);
		System.out.println(num[2]);
//for String(without and with attributes)
		String[] s= new String[4];
		System.out.println(s[0]);
		System.out.println(s[3]);
		s[0]= "Hello";
		s[2]= "World";
		System.out.println(s[0]);
		System.out.println(s[1]);
		System.out.println(s[2]);
//for loop
		for(int i=0;i<s.length;i++) {
			System.out.println(s[i]);
		}
		s[3]="!";
//for loop M-2
		for(String str:s) {
			System.out.println(str);
		}
	} 

}
