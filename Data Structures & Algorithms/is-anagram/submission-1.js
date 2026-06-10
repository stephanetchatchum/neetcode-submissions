class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const s_arr = [...s];
        const t_arr = [...t];
        s_arr.sort();
        t_arr.sort();
        if(s_arr.join('') == t_arr.join('')){
            return true;
        }else{
            return false
        }
    }
}
