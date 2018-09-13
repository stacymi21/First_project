age = int(input('Сколько тебе лет? '))

def who_are_you(age):
	if age < 7:
		return ('Тебе уже {}, вкусной каши тебе в детском саду!'.format(age))
	elif age > 7 and age < 18:
		return ('Тебе уже {}, отличных оценок в школе!'.format(age))
	elif age > 18 and age < 23:
		return ('Тебе {}, полезных знаний в университете!'.format(age))
	elif age > 23:
		return ('Тебе только {}, карьера в твоих руках!'.format(age))

print (who_are_you(age))
