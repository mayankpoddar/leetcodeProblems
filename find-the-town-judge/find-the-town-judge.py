class People:
    def __init__(self, label):
        self.label = label
        self.trusts = []
        self.isTrustedBy = []

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [People(i) for i in range(1, n+1)]
        for a, b in trust:
            people[a-1].trusts.append(people[b-1])
            people[b-1].isTrustedBy.append(people[a-1])
        judge = -1
        for p in people:
            if len(p.trusts) == 0 and len(p.isTrustedBy) == n-1:
                judge = p.label
                break
        return judge