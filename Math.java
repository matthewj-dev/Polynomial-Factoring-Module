package system_backbone;

public class Math {
	
	/*
	 * This is the math class where all the steps to solving the polynomial
	 * will occur
	 * 
	 */

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String input;
		// reader = new keyboard(System.in);
		System.out.println("Please enter a String of a polynomial.");
		//input=keyboard.nextline();
		

	}
	/*
	 * This method takes the string that is the polynomial and assigns
	 * the parts to variables to be passed along
	 */
	/*public static assign(String input) {
		
	}*/
	
	public int[] factor(int x) {
		int[] factor_list = new int[x];
		int count = 0;		
		for(int n=0;n<=x;x++) {
			if((x % n)== 0) {
				factor_list[count]=n;
			}
			
		}
		return factor_list;
	}

}
