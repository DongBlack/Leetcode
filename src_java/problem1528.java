//重新排列字符串
//基本Java语法
import java.util.ArrayList;

class Solution {
    public String restoreString(String s, int[] indices) {
        char[] s_ = new char[s.length()];
        for(int i=0;i<s.length();i++){
            s_[indices[i]] = s.charAt(i);
        } 
        return new String(s_);
    }
}
public class problem1528{
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] indices = {4,5,6,7,0,2,1,3};
        String result = solution.restoreString("codeleet",indices);
        System.out.println(result);
    }
}