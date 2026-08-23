"""
position: List[int]
speed: List[int]

both of length n

destination is at [target] miles

Example:
target = 10
position = [1,4]
speed = [3, 2]

output: 1

t = 0
position = [1,4]
t = 1
[4, 6]
t = 2
[7,8]
t = 3
[10, 10]

===
target = 10
position = [4,1,0,7]


sorted:
position = [0,1,4,7]
speed = [1,2,2,1]

so to figure out how many time units (distance - starting position)/speed (and ceil it)

total_fleets = 0
how_many_time_units = [10, 5, 3, 3]
t = 0
position = [0,1,4,7]
t = 1
position = [1,3,6,8]
t = 2
position = [2,5,8,9]
t = 3
position = [3,7,10,10,10]  total_fleets = 1
t = 4
position = [4,9,10,10]



====

Edge cases 
- range for target = 1M
- range for n: 100k
- range of speed, 1 < 1M
- range of position: 0 < target

target = 10
position=[3,4,5,6,7,8]
speed=[4,4,4,4,4,4]
    [2, 2, 2, 1, 1, 1]


"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        car_tuple = []

        for i in range(len(position)):
            car_tuple.append((position[i], speed[i]))
        
        car_tuple.sort()

        time_units = []

        for position, speed in car_tuple:
            time_units.append((target - position) / speed)

        max_so_far = time_units[-1]
        result = 1

        for i in range(len(time_units) - 1, -1, -1):
            curr = time_units[i]
            if curr <= max_so_far:
                max_so_far = max(curr, max_so_far)
            else:
                result += 1
                max_so_far = curr
        return result
        