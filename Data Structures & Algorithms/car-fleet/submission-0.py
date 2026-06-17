class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ps = []

        for i in range(len(position)):
            ps.append((position[i], speed[i]))

        ps.sort(reverse=True)

        for pos, spd in ps:
            if stack:
                pos2, spd2 = stack.pop()
                print("pos1:", pos, "spd1:", spd)
                print("pos2: ", pos2, "spd2: ", spd2)
                t1 = (target - pos) / spd
                t2 = (target - pos2) / spd2
                print("t1:", t1, "t2:", t2)

                if t2 >= t1:
                    stack.append((pos2, spd2))

                else:
                    stack.append((pos2, spd2))
                    stack.append((pos, spd))
    
            else:    
                stack.append((pos, spd))

        return len(stack)
            
