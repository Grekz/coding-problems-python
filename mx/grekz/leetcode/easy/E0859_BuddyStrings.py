'''
@author: grekz
'''
class E0859_BuddyStrings:
    def buddyStrings(self, A: str, B: str) -> bool:
        a, b = len(A), len(B)
        if a != b : return False
        if A == B :
            x = [0] * 26
            for c in A :
                x[ord(c) - 97] += 1
            for z in x :
                if z > 1 :
                    return True
        else :
            xa, xb, ya, yb = -1, -2, -3, -4
            for i in range(a) :
                if A[i] != B[i] :
                    if xa == -1 :
                        xa = A[i]
                        yb = B[i]
                    elif ya == -3 :
                        ya = A[i]
                        xb = B[i]
                    else:
                        return False
            return xa == xb and ya == yb
        return False