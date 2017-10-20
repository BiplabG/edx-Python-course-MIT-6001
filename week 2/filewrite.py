fp = open('namefile.txt', 'w')
str = ''
while True:
    if str == 'quit':
        fp.close()
        break
    else:
        str = input("Enter the string to enter: and quit to go out.")
        fp.write(str + '\n')

