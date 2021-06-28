class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        marks = [1] * n
        # 0 for UNVISITED
        # 1 for CURRENT
        # 2 for PAST
        
        # (index + num[index])%len == index
        # set.add()
        # set.remove()
        for start in range(n):
            # while looping through the loop, if we encounter a past node, dont process it, just skip
            if marks[start] == 2: 
                continue
            
            # built-in data-structure
            current_nodes = set()     
            sign = 1 if nums[start] > 0 else -1
          
            index = start
            check_sign = True
            while True:
                if sign * nums[index] < 0:
                    check_sign = False
                
                print("index: ", index, "sign: ", sign)
                
                if (check_sign == False):
                    break
                # if visits an element that already in the current_nodes 
                if (index in current_nodes):
                    return True
                    
                current_nodes.add(index)
                    
                # check if stuck 
                if (index + nums[index]) % n == index:
                    # if stuck, move all current into past
                    break

                # if visited a past node -> break
                if marks[index] == 2:
                    break

                # update next index
                index = (index+nums[index])%n

                for current in current_nodes: 
                    marks[current] = 2

        return False
        	
