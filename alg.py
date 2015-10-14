str = input("Enter an expression: ")
finalnum = ''
num1 = ''
num2 = ''
operator = ''
placeholder = 0
second_half = False
str_list = list(str)
print (str_list)
while placeholder < len(str_list):
	temp = str_list[placeholder]

	if second_half == True and temp.isdigit():
		num2 = num2 + temp
		print ('num2 is ' + num2)
	elif temp.isdigit() and second_half == False:
		num1 = num1 + temp
		print ('num1 is ' + num1)
	else:
		operator = temp
		second_half = True
		print ('operator is ' + operator)

	placeholder = placeholder + 1
if operator == '+':
	finalnum = (int(num1) + int(num2))
if operator == '-':
	finalnum = (int(num1) - int(num2))
if operator == '':
	finalnum = (int(num1) / int(num2))
if operator == '*':
	finalnum = (int(num1) * int(num2))

print(finalnum)