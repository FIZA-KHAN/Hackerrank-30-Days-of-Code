

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        l1 = []
        for i in range(1, n+1):
            if n % i == 0:
                l1.append(i)
        #return(l1)
        tot = 0
        for i in l1:
            tot = tot + i
        return(tot)

