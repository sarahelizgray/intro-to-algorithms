import java.util.Arrays;

public class BubbleSort{

    public static int[] bubbleSort(int[] numbers){
        int n = numbers.length;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                if (numbers[j] < numbers[i]) {
                    int swap = numbers[j];
                    numbers[j] = numbers[i];
                    numbers[i] = swap;
                }
           }
        }
        return numbers;
    }

public static void main(String[] args){
    int[] numbers = {1, 2, 3, 4, 5, 23, 56, 78, 22, 45, 9};
    int[] result = bubbleSort(numbers);
    System.out.println("result is "  + Arrays.toString(result));
    }

}





