class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        /* so one solution is to simply maintain a set
        and simply add to it and check if a number has 
        been seen before, 
        space / time i n
        */
        const seen = new Set();
        for (let num of nums) {
            if (seen.has(num)) {
                return true
            }
            seen.add(num)
        }
        return false
    }
}
