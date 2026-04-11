class Solution {
    public void moveZeroes(int[] nums) {
        int last_idx = -1;
        for(int i=0; i< nums.length; i++) {
            if (nums[i] != 0) {
                last_idx++;
                int temp = nums[i];
                nums[i] = nums[last_idx];
                nums[last_idx] = temp;
            }
        }
    }
}