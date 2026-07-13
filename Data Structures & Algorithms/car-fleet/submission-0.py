class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 1. Pair position with speed, and sort in descending order of position
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        # 2. Iterate through each car and compute its arrival time
        for pos, spd in cars:
            time = (target - pos) / spd
            
            # 3. Push to stack. If it takes longer than the fleet ahead, 
            # it forms a new fleet. If it's faster, it merges (do nothing).
            if not stack or time > stack[-1]:
                stack.append(time)
                
        # The remaining elements in the stack represent distinct fleets
        return len(stack)