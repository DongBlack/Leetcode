class Solution1528 {
    public String restoreString(String s, int[] indices) {
        char[] s_ = new char[s.length()];
        for(int i=0;i<s.length();i++){
            s_[indices[i]] = s.charAt(i);
        } 
        return new String(s_);
    }
}
