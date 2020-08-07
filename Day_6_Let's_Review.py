# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case = int(input())

for j in range(test_case):

    string = input()
    even = ''
    odd = ''

    for i in range(len(string)):
        if i % 2 == 0:
            even = even + string[i]
            #print(even)
        else:
            odd = odd + string[i]

    print(even, odd)


        #print(string[i], end="")
