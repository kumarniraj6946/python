print("-----PROGRAM FOR STUDENT INFORMATION-----")

D = dict()

n = int(input('How many student record you want to store ?? '))


for i in range(0,n):
	x, y = input("Enter the complete name (First and last name) of student: ").split()
	z = input("Enter contact number: ")
	m = input('Enter Marks: ')
	D[x, y] = (z, m)
	

def sort():
	ls = list()
	
	for sname,details in D.items():
	
		tup = (sname[0],sname[1])
	
		ls.append(tup)
		
	ls = sorted(ls)
	for i in ls:
	
		print(i[0],i[1])
	return

def minmarks():
	ls = list()
	for sname,details in D.items():
		
		ls.append(details[1])
	
	ls = sorted(ls)
	print("Minimum marks: ", min(ls))
	
	return

# define a function for searching
# student contact number
def searchdetail(fname):
	ls = list()
	
	for sname,details in D.items():
	
		tup=(sname,details)
		ls.append(tup)
		
	for i in ls:
		if i[0][0] == fname:
			print(i[1][0])
	return

def option():

	choice = int(input('Enter the operation detail: \n \
	1: Sorting using first name \n \
	2: Finding Minimum marks \n \
	3: Search contact number using first name: \n \
	4: Exit\n \
	Option: '))
	
	if choice == 1:
	    
		sort()
		print('Want to perform some other operation??? Y or N: ')
		inp = input()
		if inp == 'Y':
			option()
		exit()
		
	elif choice == 2:
		minmarks()
		print('Want to perform some other operation??? Y or N: ')
		
		inp = input()
		if inp == 'Y':
			option()
		exit()
		
	elif choice == 3:
		first = input('Enter first name of student: ')
		searchdetail(first)
		
		print('Want to perform some other operation??? Y or N: ')
		inp = input()
		if inp == 'Y':
			option()
			
		exit()
	else:
		print('THANKS FOR EXECUTING ME!!!!')
		exit()
		
option()
