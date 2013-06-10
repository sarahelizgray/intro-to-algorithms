public class BinarySearch{

public static int binarySearch( int[] numbers, int key) {
        int low = 0;
        int high = numbers.length - 1;
        while (low <= high) {
            int pivot = (low + high) / 2;
            if (key == numbers[pivot]) {
                return pivot;
            }
            else if (key > numbers[pivot]){
                low = pivot + 1;
            }
            else {
                high = pivot - 1;
            }
        }
        return -1;
    }

public static void main(String[] args)
  {
    int[] numbers = {1,2,3,4,5,23,56,78};
    int result = binarySearch(numbers, 23);
    System.out.println("result is "  + result);
  }

}