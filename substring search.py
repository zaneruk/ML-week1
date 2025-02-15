input_string = input()  
substring = input().lower() 
words = input_string.split()
for word in words:
    if substring in word.lower(): 
        print(word)