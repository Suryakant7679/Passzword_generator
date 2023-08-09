'''for i in range(1,101):
    if(i%3==0)and (i%5==0):
        print("FIZZ Buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
        '''

# password generator
# here password will be generated in combination of letter digits and symbol

import random
design='''

           __________                                 
         .'----------`.                              
         | .--------. |                             
         | |Generate| |       __________              
         | |Password| |      /__________\             
.--------| `--------' |------|  ----=-- |-------------.
|        `----,-.-----'      |  C P U   |             | 
|       ______|_|_______     |__________|             | 
|      /1,2,3,4,,5,6,6  \                             | 
|     / a,s,c#,f,5,&,o   \                            | 
|    /____________________\                           | 
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''
print(design)

symbol_length=int(input("enter the number of symbol"))
digit_length=int(input("enter the no of digits"))
letter_length=int(input("enter the length of letter"))

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits=[1,2,3,4,5,6,7,8,9,0]
symbol=["@","#","$","%","&"]
password=[]
for i in range(0,symbol_length):
    password.append(random.choice(letter))
for i in range(0,digit_length):
    password.append(random.choice(digits))
for i in range(0,letter_length):
    password.append(random.choice(symbol))
random.shuffle(password)
your_password=''
for char in password:
    your_password=your_password+str(char)

print("your password is:- ",your_password)
