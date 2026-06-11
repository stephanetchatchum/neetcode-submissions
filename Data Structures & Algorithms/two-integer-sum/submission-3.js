class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        
        for (let i = 0; i < nums.length; i++){
            let second = target - nums[i];
            if (nums.includes(second)){
                let j = nums.indexOf(second);
                if (j !== i){
                    return [Math.min(i,j), Math.max(i,j)];
                }
            }
        }
    }
}
