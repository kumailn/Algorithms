import java.util.Arrays;

public class Insert {
    public static void sortInsert(Integer[] arr){
        for(int i = 0; i < arr.length; i++){
            int j = i;
            while(j > 0 && arr[j] < arr[j - 1]){
                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
                j--;
            }
        }
    }

    public static void main(String[] args) {
        Integer[] a = new Integer[]{5, 6, 4, 3};
        System.out.println(Arrays.toString(a));
        sortInsert(a);
        System.out.println(Arrays.toString(a));
    }

}
