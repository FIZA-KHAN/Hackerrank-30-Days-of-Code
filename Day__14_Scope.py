class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        #count = 0
        l1 = []
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                count = a[i] - a[j]
                abs_count = abs(count)
                l1.append(abs_count)
        #print(l1)
        self.maximumDifference = max(l1)
        #print(self.maximumDifference)
            
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
