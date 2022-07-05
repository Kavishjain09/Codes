package java_01;

public class ND_Array {
	public static void main(String[] args) {
		int[][] arr = {
				{1,2,3,10},
				{4,5,6,20},
				{7,8,9,30}
		};
		System.out.println(arr[0][1]);
		System.out.println(arr[1][0]);
		System.out.println(arr[1][2]);
		for(int i=0;i<arr.length;i++) {
			for(int j=0;j<arr[i].length;j++) {
				System.out.print(arr[i][j]+ "   ");
			}
			System.out.println();
		}
//for Strings(declaring String)
		String[][] texts = new String[2][2];
		String[][] words = new String[2][]; //two rows only
		words[0]= new String[3]; //1st row has three columns
		words[1]= new String[2];
		words[0][1]= "Hey";
		for(int i=0;i<words.length;i++) {
			for(int j=0;j<words[i].length;j++) {
				System.out.print(words[i][j]+ "   ");
			}
			System.out.println();
		}
		System.out.println(texts.length);
	}
}
