'''
@author: grekz
'''
class E0950_RevealCardsInIncreasingOrder:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        i, res = collections.deque(range(n)), [0] * n
        for card in sorted(deck):
            res[i.popleft()] = card
            if i :
                i.append(i.popleft())
        return res