class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        n1, n2 = len(str(left)), len(str(right))
        results = []
        if n1 == 1:
            for i in range(left, min(right+1, 10)):
                results.append(i)
            n1 += 1
        if n1 == 2:
            for i in range(1, 10):
                for j in range(1, 10):
                    num = 10*i + j
                    if num < left:
                        continue
                    if num > right:
                        return results
                    if num % i == 0 and num % j == 0:
                        results.append(num)
            n1 += 1
        if n1 == 3:
            for i in range(1, 10):
                for j in range(1, 10):
                    for k in range(1, 10):
                        num = 100*i + 10*j + k
                        if num < left:
                            continue
                        if num > right:
                            return results
                        if num % i == 0 and num % j == 0 and num % k == 0:
                            results.append(num)
            n1 += 1
        if n1 == 4:
            for i in range(1, 10):
                for j in range(1, 10):
                    for k in range(1, 10):
                        for l in range(1, 10):
                            num = 1000*i + 100*j + 10*k + l
                            if num < left:
                                continue
                            if num > right:
                                return results
                            if num % i == 0 and num % j == 0 and num % k == 0 and num % l == 0:
                                results.append(num)
        return results