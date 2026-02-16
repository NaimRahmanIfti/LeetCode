class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        car = list(zip(position, speed))
        car.sort()

        while car:
            c, s = car.pop()
            time = (target - c) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
