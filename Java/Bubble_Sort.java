//Simple bubble sort implemntation
import java.util.Arrays;

public class Bubble {
    public static void main(String[] args) {
        int[] myarr = {34, 23, 34, 2, 3, 8, 4, 5};
        BubbleSort(myarr);
        System.out.println(Arrays.toString(myarr));
    }

    public static void BubbleSort(int[] arr){
        for(int i = arr.length - 1; i > 1; i--){
            for(int j = 0; j < i; j++){
                if(arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1]= temp;
                }
            }
        }
    }
}
