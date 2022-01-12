# Dispaying usage of atleast one python library along with file handling
import os

while True:
    print('\n0: Exit')
    print('1: Create a File')
    print('2: Read a File')
    print('3: Write a File')
    print('4: Rename a File')
    print('5: Delete a File')
    try:
        choice = int( input('ENTER YOUR CHOICE: ') )
    except: 
        print('Invalid Input!!!\nEnter Integer Value From 0 to 5.')
        os.system('pause')
        continue
    print()
    if choice == 0:
        break
    elif choice == 1:
        file = input('Enter file name with extension: ')
        if not os.path.isfile(file):
            open(file, 'w')
            print('File Opened.')
        else:
            print('File Already Exists!!')
        
    elif choice == 2:
        file = input('Enter file name with extension: ')
        try:
            fh = open(file, 'r')
            for line in fh.readlines():
                print(line.strip())
            fh.close()
        except:
            print('File Not Found!!')
    elif choice == 3:
        file = input('Entert file name with extension: ') 
        fh = open(file,'w')
        print ('Enter Text (Enter eof to terminate writing): \n')
        text = input()
        while text.strip() != 'eof':
            fh.write(text + '\n')
            text = input()
        fh.close()
    elif choice == 4:
        file_old = input('Enter Old File Name with Extension: ')
        file_new = input('Enter New File Name with Extension: ')

        
        if os.path.isfile(file_new):
            print('\'' + file_new + '\'', 'Already Exists!!')
        elif os.path.isfile(file_old):
            os.rename(file_old, file_new)
            print('File Renamed!!')
        else:
            print('\'' + file_old + '\'','Does Not Exist? \nDO You Wish to Create a New File named', '\'' + file_new + '\'?(Y/N): ' )
            ch = input()
            if ch == 'Y' or ch == 'y':
                open(file_new, 'w')
                print('New File Created!!')
    elif choice == 5:
        file = input('Enter File Name with Extension: ')
        if not os.path.isfile(file):
            print('File Does Not Exist!!')
        else:
            os.remove(file)
            print('File Deleted!!')
    else:
        print('Incorrect Choice!!')
        
    os.system('pause')
