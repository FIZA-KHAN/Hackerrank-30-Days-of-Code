# Enter your code here. Read input from STDIN. Print output to STDOUT
no_input = int(input())
phone_bk = dict()

for i in range(no_input):
    num_and_name = input().split(" ")
    phone_bk[num_and_name[0]] = num_and_name[1]

while True:
    try :
        name = input()
        #phone_name = phone_bk.keys()
        phone_num = phone_bk.get(name)
        if phone_num:
        #if name in phone_name:
            print(name + "=" + phone_num ) #phone_bk[name]
        else:
            print("Not found")
    except:
        break
