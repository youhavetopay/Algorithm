import java.util.Scanner;

import java.util.*;
import java.io.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.nio.Buffer;
import java.util.ArrayList;
/**
 * 
 * 백준 6603문제
 * 백트래킹?? --> 가지치기(안될것 같은건 지우기)
 * 
 */
public class Rotto {

    private static ArrayList<ArrayList<Integer>> answers = new ArrayList<>();

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String[] giveArray = bf.readLine().split(" ");

        while(!giveArray[0].equals("0")){
            
            int count = Integer.parseInt(giveArray[0]);
            

            int[] arr = new int[count];
            for(int i=0; i < count ; i++){
                arr[i] = Integer.parseInt(giveArray[i+1]);
            }

            boolean[] visited = new boolean[count];

            combination(arr, visited, 0, count, 6);

            for(ArrayList<Integer> tempList: answers){
                for(int number: tempList){
                    if(number == tempList.get(tempList.size()-1)){
                        System.out.println(number);
                    } else {
                        System.out.print(number+" ");
                    }
                }

            }

            giveArray = bf.readLine().split(" ");

            if(!giveArray[0].equals("0")){
                System.out.println();
            }

            answers.clear();
            
        }

        bf.close();

    }

    static void combination(int[] arr, boolean[] visited, int start, int length, int selectCount){
        if(selectCount == 0){
            answers.add(addList(arr, visited, length));
            return;
        }
        for (int i = start; i <length; i++){
            visited[i] = true;
            combination(arr, visited, i + 1, length, selectCount - 1);
            visited[i] = false;
        }
    }

    static ArrayList<Integer> addList(int[] arr, boolean[] visited, int n){
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0; i<n; i++){
            if(visited[i]){
                answer.add(arr[i]);
            }
        }
        return answer;
    }

    
}
