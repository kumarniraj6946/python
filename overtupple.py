numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if x %2:
    	     count_odd+=1
        else:
    	     count_even+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
