class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const hashmap = new Map();
        for (let i = 0; i < strs.length; i++){
            var word_arr = [...strs[i]];
            word_arr.sort();
            var key = word_arr.join('');
            if (!hashmap.has(key)){
                hashmap.set(key, []);
            }
            hashmap.get(key).push(strs[i]);
        }
        return [...hashmap.values()]
    }
}
