sum = 0
while True:
    user_input=input()
    if user_input =="end":
        break
    number = int(user_input)
    if number%2==0:
        sum+=number
print(sum)