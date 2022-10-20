from random import randint

key=[]

symbols="!@#$%^&*()-_=+[]{'};:><?/\|"
symbols_len=len(symbols)
numbers='1234567890'
numbers_len=len(numbers)
letters='asdfghjklzxcvbnmqwertyuiop'
letters_len=len(letters)

length=100
change_length=input("Do you want to specify the length? (y/n) ")
if change_length=='y':
    length=int(input("What length do you want your secret key to be? "))

for i in range(length):
    symbolType=randint(1,3)
    if symbolType==1:
        symbol=randint(0,symbols_len-1)
        symbol=symbols[symbol]
        key.append(symbol)
    elif symbolType==2:
        symbol=randint(0,numbers_len-1)
        key.append(numbers[symbol])
    if symbolType==3:
        symbol=randint(0,letters_len-1)
        case=randint(0,1)
        if case==0:
            key.append(letters[symbol])
        else:
            symbol=letters[symbol]
            key.append(symbol.upper())
        
print(''.join(key))