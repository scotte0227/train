password = "a123456"
i=3
print('最多輸入3次密碼')
while True:
	password_try = input('請輸入密碼: ')
	if password_try == password:
		print('登入成功')
		break
	else:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會')
		if i == 0:
			break