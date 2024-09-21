i=0
while i < 3 :
	age_guess=int(input('猜测的年龄：'))
	if age_guess == 25:
		print('你答对了')
		exit()
	elif age_guess > 25:
		print("猜大了，再试试")
	elif age_guess < 25:
		print("猜小了，再试试")