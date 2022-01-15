import sqlite3, re, os


def clrscr():  # function to clear screen independent of OS
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		_ = os.system('cls')


def getNumber():  # Function to get a number of proper format
	while True:
		num = input('Enter Number or Press Enter: ').strip()
		if len(num) < 1: return None
		if re.match('^[1-9][0-9]{9}$', num): return num
		choice = input('Incorrect Syntax!! \nWant to Try Again?(Y/N): ')
		if choice != 'Y' and choice != 'y': return None


def getAttr(attr_list, isName: bool):  # Function to select a name/number from the given list
	if isName:
		while True:
			Name = input('\nSelect Name or Press Enter: ').strip().capitalize()
			if len(Name) < 1: return None
			if Name in attr_list: return Name
			choice = input('\nIncorrect Value!! \nWant to Try Again?(Y/N): ')
			if choice != 'Y' and choice != 'y': return None
	else:
		while True:
			Num = input('\nSelect Num or Press Enter: ').strip()
			if len(Num) < 1: return None
			if Num in attr_list: return Num
			choice = input('\nIncorrect Value!! \nWant to Try Again?(Y/N): ')
			if choice != 'Y' and choice != 'y': return None


# driver code
choice = input('\nDo You Want to Import a ContactList? (Y/N): ')
if choice == 'Y' or choice == 'y':
	file = input('\nEnter Database Name with Extension: ').strip()
	if re.match('^\\S+\\.sqlite$', file) is None:
		print('Invalid Database!!\nDefault Database Created')
		file = 'contactList.sqlite'
else: 
	file = 'contactList.sqlite'

database = sqlite3.connect(file)
cursor = database.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Contacts (
			Name TEXT,
			Number TEXT UNIQUE,
			PRIMARY KEY (Name, Number) )''')

while True:
	print()
	os.system('pause')
	clrscr()
	print('0: Exit\n1: Create Contact\n2: Find Contact')
	print('3: Edit Contact\n4: Delete Contact\n5: Print All Contacts\n')

	try:
		choice = int(input('Enter Your Choice: ').strip())
	except ValueError:
		print('Invalid Value!!\nEnter Integer From 0 to 5')
		os.system('pause')
		continue

	print()
	if choice == 0:  # Exiting the program After saving contacts if needed
		choice = input('Do You Want to Save The Database?(Y/N): ').strip()
		if choice != 'y' and choice != 'Y':
			database.close()
			os.remove(file)
		quit()

	elif choice == 1:  # Adding new contact
		name = input('Enter Name: ').strip().capitalize()
		number = getNumber()
		if number is not None:
			cursor.execute('INSERT OR IGNORE INTO Contacts (Name, Number) VALUES (?,?)', (name, number))
			database.commit()

	elif choice == 2:  # Viewing/Finding Required Contact
		keyword = '%' + input('Enter Keyword: ').strip() + '%'
		names = cursor.execute('SELECT Name FROM Contacts WHERE Name LIKE ? ORDER BY Name ASC', (keyword,)).fetchall()
		# found names having the keyword in them
		print()
		if len(names) == 0:
			print('No Contacts Found For the given KeyWord!!')
			continue

		namelist = list()  # creating namelist for getAttr function
		for name in names:
			print(name[0])
			namelist.append(name[0])
		
		name = getAttr(namelist, isName=True)
		if name is None: continue  # exit condition

		# Getting the required Data and printing them
		numbers = cursor.execute('SELECT Number FROM Contacts WHERE Name = ?', (name,))
		print(name + ": ")
		for number in numbers: print('\t' + number[0])

	elif choice == 3:  # Updating Numbers
		keyword = '%' + input('Enter Keyword: ').strip() + '%'
		# Keyword based Search
		contacts = cursor.execute('SELECT * FROM Contacts WHERE Name LIKE ? ORDER BY Name ASC', (keyword,))
		namelist = list()   # list for getAttr function
		print()
		if contacts == None:
			print('No Contacts Found For the Given KeyWord')
			continue

		for contact in contacts:
			print(contact[0], ':', contact[1])
			namelist.append(contact[0])

		# Getting target name from list name having keywords
		name = getAttr(namelist, isName=True)
		if name is None: continue
		x = cursor.execute('SELECT COUNT(*) FROM Contacts WHERE Name = ?', (name,))
		if x == 1:  # Single number for the given name
			print('\nENTER NEW NUMBER:')
			number = getNumber()
			if number is not None:
				cursor.execute('UPDATE Contacts SET Number = ? WHERE Name = ?', (number, name))
				print('\nNumber Updated!!')
				database.commit()

		else:  # More than one numbers for the person
			print('\nMore than One Numbers Found!! Select One From:\n')
			numberList = list()
			for number in cursor.execute('SELECT Number FROM Contacts WHERE Name = ?', (name,)):
				print(number[0])
				numberList.append(number[0])

			# (name, number) pair matching
			numOld = getAttr(numberList, isName=False)
			if numOld is None: continue
			print('\nENTER NEW NUMBER:')
			numNew = getNumber()
			if numNew is None: continue
			cursor.execute('UPDATE Contacts SET Number = ? WHERE Name = ? AND Number = ?', (numNew, name, numOld))
			print('\nNumber Updated!!')
			database.commit()

	elif choice == 4:
		keyword = '%' + input('Enter Keyword: ').strip() + '%'
		# Keyword based Search
		contacts = cursor.execute('SELECT * FROM Contacts WHERE Name LIKE ? ORDER BY Name ASC', (keyword,))
		namelist = list()  # Reusing list for getName function
		print()
		if contacts is None:
			print('No Contacts Found for the Given KeyWord!!')
			continue
		for contact in contacts:
			print(contact[0], ':', contact[1])
			namelist.append(contact[0])

		# Getting target name to delete
		name = getAttr(namelist, isName=True)
		x = cursor.execute('SELECT COUNT(*) FROM Contacts WHERE Name = ?', (name,)).fetchone()[0]
		if x == 1:  # Single number for the given name
			cursor.execute('DELETE FROM Contacts WHERE Name = ?', (name,))
			print('\nContact Deleted!!')
			database.commit()

		else:  # More than one numbers for the person
			choice = input('More than One Numbers Found!! Delete All?(Y/N): ')
			if choice == 'Y' or choice == 'y':
				cursor.execute('DELETE FROM Contacts WHERE Name = ?',(name,))
				print('\nAll Contacts Of \'' + name + '\' Deleted!!')
				database.commit()
				continue
			
			# Only One contact to be deleted
			numberList = list()
			for number in cursor.execute('SELECT Number FROM Contacts WHERE Name = ?', (name,)):
				print(number[0])
				numberList.append(number[0])

			# (name, number) pair matching
			number = getAttr(numberList, isName=False)
			if number is None: continue
			cursor.execute('DELETE FROM Contacts WHERE Name = ? AND Number = ?', (name, number))
			print('\nContact Deleted!!')
			database.commit()

	elif choice == 5:
		x = cursor.execute('SELECT COUNT(*) FROM Contacts').fetchone()[0]
		if x < 1:
			print('No Entries Found!!')
			continue
		for contact in cursor.execute('SELECT * FROM Contacts ORDER BY Name ASC'):
			print(contact[0], ':', contact[1])

	else:
		print('Incorrect Choice!!')
