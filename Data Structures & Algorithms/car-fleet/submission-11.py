class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleets = 0
        lead_arrival = 0.0
        for position, speed in reversed(cars):
            arrival = (target - position) / speed
            if arrival > lead_arrival:
                fleets += 1
                lead_arrival = arrival
        return fleets