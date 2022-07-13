import java.util.Scanner;

public class TestClassJava {
    public static void main(String[] args) {
        
        // Scanner sc = new Scanner(System.in);
		// int T;
		// T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		UserSolution userSolution = new UserSolution();
		userSolution.init();

        int answer = 0;

		char[] test = {'m', 'a', 'l', 'e', '\0'};
		System.out.println(userSolution.add(1, 1, test, 50));
		System.out.println(userSolution.add(2, 1, test, 500));
		System.out.println(userSolution.add(3, 3, test, 500));

		System.out.println(userSolution.remove(3));

		int[] score1 = {1, 2};
		char[][] male1 = {{'m', 'a', 'l', 'e'}, {'f', 'e', 'm', 'a', 'l', 'e'}};
		System.out.println(userSolution.query(2, score1, 2, male1, 100));

		
    }
}
