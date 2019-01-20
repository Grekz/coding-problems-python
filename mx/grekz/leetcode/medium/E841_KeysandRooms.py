'''
@author: grekz
'''


class E841_KeysandRooms:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = [False] * len(rooms)
        stack = [0]
        seen[0] = True
        while len(stack) != 0:
            cur = stack.pop()
            for x in rooms[cur]:
                if not seen[x]:
                    seen[x] = True
                    stack.append(x)
        for x in seen:
            if not x:
                return False
        return True
