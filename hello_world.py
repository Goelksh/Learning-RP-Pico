# Print Logic
print('Hello world | Examples:')
print(5 * 'A')
print(5 * "ABC ")
input('Press Enter to continue...')
# Range Logic
print('counting up')
for i in range(1,11,1):
    print('-->',i)

input('Press Enter to continue...')

print('counting down')
for i in range(10,0,-1):
    print('<--',i)

input('Press Enter to continue...')
print('table of 15')
for i in range(15,151,15):
    print('==X',i)

input('Press Enter to continue...')
print('table of 17')
for i in range(1,11,1):
    print('17 x', i,'=',i*17)

input('Press Enter to continue...')
# Input Logic    
table_of = input ("Now which table do you want? (put a Integer only) :")
print('Table of',table_of)
for i in range(1,11,1):
    print(table_of,'x', i,'=',i* int(table_of))

input('Press Enter to continue...')
#While & If Logic
name = input ("What's your name??? (capitalisation of initials required):")
if name != "Kshitij Goel":
    while name != "Kshitij Goel":
        print('I dont know you. Try again.')
        name = input ("What's your name??? (capitalisation of initials required):")
    print('Hi, welcome back to your project')  
else:
    print('Hi, welcome back to your project')
    
input('Press Enter to continue...')
print("that's it")
print("Thank You!!!!!!!!!!!!!")

