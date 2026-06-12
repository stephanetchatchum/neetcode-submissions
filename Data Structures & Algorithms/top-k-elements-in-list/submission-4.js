class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const hashmap = {};
        for (let num of nums){
            if(!(num in hashmap)){
                hashmap[num] = 0;
            }
            hashmap[num] += 1
        }
        const array = Object.keys(hashmap).sort((a,b) => hashmap[b] - hashmap[a]);

        return array.slice(0,k).map(Number);
    }
}
