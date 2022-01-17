import re, os
from typing import OrderedDict


def clrscr():  # function to clear screen independent of OS
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		_ = os.system('cls')

def getNumber(): # function to have user input of number of proper format
    while True:
        Num = input('Enter Number or Press Enter to exit: ').strip()
        if len(Num) < 1: return None
        if re.match('^[1-9][0-9]{9}$', Num) is not None: return Num

def selectName(name_list : list):
    while True:
        Name  = input('Select Name or press Enter: ').strip().capitalize()
        if len(Name) < 1: return None
        if Name in name_list: return Name

# Driver Code
contacts = OrderedDict()
try:  # try-except encasing to make sure all contacts are saved during any unhandled exception
    choice = input('\nDo You Want to Import a ContactList? (Y/N): ')

    if choice == 'Y' or choice == 'y':
        file = input('\nEnter file Name with Extension: ').strip()
        if re.match('^\\S+\\.txt$', file) is None:  # Ensuring text file
            print('Invalid File!!\nDefault File Created')
            file = 'contactList.txt'
    else: 
        file = 'contactList.txt'

    if os.path.isfile(file):
        print('Reading File to Import Contacts...')
        fh = open(file, 'r')  # readding contacts from file before beginning

        for line in fh:
            name, number = line.split()
            contacts[name] = number
        
        contacts = OrderedDict(sorted(contacts.items()))
        fh.close()

    while True:
        print()
        os.system('pause')
        clrscr()
        print('0: Exit\n1: Add Contact\n2: Find Contact')
        print('3: Edit Contact\n4: Delete Contact\n5: Print All Contacts')
        
        try:
            choice = int(input('\nEnter Your Choice: '))
        except ValueError as e:
            print('Exception:',e)
            continue

        print()
        if choice == 0:
            choice = input('Do You Want to Save The Database?(Y/N): ').strip()
            if choice == 'y' or choice == 'Y':
                fh = open(file, 'w')
                for item in contacts.items():
                    fh.write(item[0] + ' ' + item[1] + '\n')
                fh.close
            quit()
            
        elif choice == 1:
            name = input('Enter Name: ').strip().capitalize()
            number = getNumber()
            
            if number is not None:
                if contacts.get(name, None) is None:
                    contacts[name] = number
                    contacts = OrderedDict(sorted(contacts.items()))
                    print('Contact Added!!')
                else:
                    print('Contact With the name \'' + name + '\' already exists.\n Do you Want to replace it?:\n')
                    print(name, ':', contacts[name])
                    choice = input('\n(Y/N): ')
                    if choice == 'Y' or choice == 'y':
                        contacts[name] = number
                        print('Contact Replaced!!')

        elif choice == 2: 
            keyword = '^.*[' + input('Enter Keyword: ').strip().lower() + '].*$'
            nameList = list()
            print()
            for key in contacts.keys():
                if re.match(keyword, str(key).lower()) is not None:
                    nameList.append(key)
                    print(key)

            if len(nameList) < 1:
                print('No Contact Found for the Given KeyWord!!')
                continue

            print()
            name = selectName(nameList)
            if name is not None:
                print(name, ':', contacts[name])

        elif choice == 3:
            keyword = '^.*[' + input('Enter Keyword: ').strip().lower() + '].*$'
            nameList = list()
            print()
            for key in contacts.keys():
                if re.match(keyword, str(key).lower()):
                    print(key, ':', contacts[key])
                    nameList.append(key)
            
            if len(nameList) < 0:
                print('No Contact Found For the Given KeyWord!!')
                continue
            print()
            name = selectName(nameList)
            
            if name is not None:
                print('\nENTER NEW NUMBER:\n')
                newNum = getNumber()
                contacts[name] = newNum
                print('Contact Updated!!')

        elif choice == 4:
            keyword = '^.*[' + input('Enter Keyword: ').strip().lower() + '].*$'
            nameList = list()
            print()
            for key in contacts.keys():
                if re.match(keyword, str(key).lower()):
                    print(key, ':', contacts[key])
                    nameList.append(key)
            
            if len(nameList) < 0:
                print('No Contact Found For the Given KeyWord!!')
                continue
            print()
            name = selectName(nameList)
            
            if name is not None:
                contacts.pop(name)
                print('Contacted Deleted!!')
            
        elif choice == 5:
            if len(contacts) < 1:
                print('\nNo Contacts Found!!')
                continue
            
            for item in contacts.items():
                print(item[0], ':', item[1])
        else:
            print('Incorrect Value!!\nChoose From 0 to 5...')

except Exception as eobj:
    print('\n\nException:',eobj)
    print('Saving Data...')
    fh = open(file, 'w')
    for item in contacts.items():
        fh.write(item[0] + " " + item[1] + "\n")
