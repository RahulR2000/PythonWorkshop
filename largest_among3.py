print("Enter three numbers")

first_number = int(input("First Number : "))
second_number = int(input("Second Number : "))
third_number = int(input("Third Number : "))

if first_number > second_number:
	if first_number > third_number:
		print("Largest number : " + str(first_number))
	else:
		print("Largest number : " + str(second_number))
else:
	if second_number > third_number:
		print("Largest number : " + str(second_number))
	else:
		print("Largest number : " + str(third_number))
