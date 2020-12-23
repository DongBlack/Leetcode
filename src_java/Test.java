import java.util.Arrays;

//1528 重排字符串
// public class Test {
//     public static void main(String[] args) {
//         Solution1528 solution = new Solution1528();
//         int[] indices = {4,5,6,7,0,2,1,3};
//         String result = solution.restoreString("codeleet",indices);
//         System.out.println(result);
//     }
// }

//56 合并区间
public class Test {
    public static void main(String[] args) {
        Solution56 solution = new Solution56();
        int[][] arg = {{1,3},{8,10},{2,6},{0,1}};
        int[][] result = solution.merge(arg);
        System.out.println(Arrays.deepToString(result));
        // String[] words = {"123","leetcode"};
        // ArrayList<?> list = new ArrayList<>(Arrays.asList(words));
        // System.out.println(list);
    }
}