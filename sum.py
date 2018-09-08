def get_summ(one,two,delimeter = '&'):
	return (str(one) + str(delimeter) + str(two)).upper()

a = get_summ ('Learn','python')

print(a)
