"""
choices:
    calculate arr[l + 1] - arr[l] - l_diff
    calculate arr[r - 1] - arr[r] - r_diff

    if l_diff > r_diff
        move left pointer
    else:
        move right pointer
    
    calculate max volume


    move left pointer
        
    move right pointer

    1 10 8 1

step 1
max volume is - 3

max volume is - 3

Okay, so I'm given an integer array called `heights` where each value in the array represents the height of the nth bar. I can choose any two bars to form a container and return the maximum amount of water the container can store. Looking at the photo I have here, basically the maximum height this container can be is the minimum of the two bars that you choose, and the width is simply the higher index subtracted from the lower index. I'm supposed to return the maximum amount of water a container can store. In the example they've given me, where the height array includes `1, 7, 2, 5, 4, 7, 3, and 6`, the maximum height is given by the `7` and the `6` in the array. The width is `8 - 2 = 6`, and the maximum height is `6`. So, `6 * 6 = 36`. You return `36`.

Another example to give: they have three elements, all twos in the array. The output should be `4` because you basically pick the ends of the array. `2 * 2 = 4`.

Okay, so for my clarifying questions: what is the maximum and minimum size of the array? How many values can it contain? Okay, so the maximum is `1000`, and the minimum is `2`. What about the values themselves? Each individual bar can be between `0` and `1000`, inclusive. Oh, I see. Okay, great.

All right, my basic intuition now is that we start with the maximum width, so we select the two ends.

And then now we need to have a rule that decides, well, let's pick the biggest width, which is the two end values, and calculate and save the maximum volume of water there. And then what we have to do is move. Next, we need to basically optimize for having the highest height.

Right. So given the example that we have where the first number is one and the last number is six, we have the option of moving the left or the right pointer. How do you choose? Well, I look at the left or the right pointer, so we can try seeing the neighbors and seeing which one's higher. So next to the one is a seven, and next to the six is a three. Since seven is higher, we keep the right pointer where it is and move the left pointer to seven. Okay, now what? Next to the seven is a two, and next to the six is still a three. So now I can either move the left pointer from seven or move the right pointer from six. Oh, by the way, when I moved the first pointer, I didn't calculate the new area. Use the max function to replace the current max value. Okay, what do I do now? Do I move? Okay, let me just get the obvious brute force one out of the way, which is to basically have two for loops nested within each other, calculate all possible combinations of container sizes, keep track of the maximum value, and return it. That's O(n²). I'm assuming that's not the most optimal one. That's why I switched to the two-pointer solution. I guess you might want to not compare the ends because the problem I'm facing is you won't know. Like, imagine you have literally—understanding, like, imagine in the middle of the array you have a couple of pointers that are 1000 units high. That's going to be way bigger than, you know, something in the middle. But how do you even get there? What's the rules to get there? Is it literally move if my neighbor is higher than me? Let's come up with a simple example. So 1, 10, 10, 1, right? So step one, max volume is going to be 4 minus 1, so it's going to be 3. And then I see that next to 1, I have an array with 1, 10, 10, and 1. Next to 1 is a 10 on the left side. Or maybe I just do subtraction and just move. The one where it's higher. So if 10 minus one is higher than or equal to 10 minus one on the other pointer, then I move it. Let's make it interesting. Instead of 1, 10, 10, 1, I'm going to make it 1, 10, 8, 1. So I move the pointer to 10. Now its max volume is still, it's actually 2, so. Leave it at three, and then I could either move it to eight or. Okay, so the rule I'm understanding is move. So first, first calculate left. Oh, sorry, array at left plus one minus array at left. And then calculate array at right minus one minus array at right. Okay, call the first one L difference, second one R difference. If L difference is greater than R difference, move left pointer. Else move right pointer. Then calculate max volume. All right, let's just try it out with 222. So I need to do this until left is less than right. Yeah, what do you think? 
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_vol = 0

        while l < r:
            curr_vol = (r - l) * (min(heights[l], heights[r]))
            max_vol = max(max_vol, curr_vol)
            if heights[l] > heights[r]:
                # move right
                r -= 1
            else:
                l += 1
        return max_vol
        