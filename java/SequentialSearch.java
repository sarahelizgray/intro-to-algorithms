public class SequentialSearch{

public static int findIndex(int[] numbers, int key){
    for (int index = 0; index < numbers.length; index++){
        if (numbers[index] == key){
            return index;  //There it is!
        }
    }
    return -1; //Nope, not in the array
}

public static void main(String[] args)
  {
    int[] numbers = {1,2,3,4,5,23,56,78};
    int result = findIndex(numbers, 23);
    System.out.println("result is "  + result);
  }

}
