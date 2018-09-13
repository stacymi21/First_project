def string_comparison (first, second):

	if type (first) != str or type (second) != str :
		return 0

	if  first == second:
		return 1

	if len(first) > len(second):
		return 2

	if second == 'learn':
		return 3

	return ('Такого условия нет')


print ('Результат работы функции по прописанным переменным: ')
print(string_comparison(123, 'кот'))
print(string_comparison('котик', 'котик'))
print(string_comparison('котик', 'кот'))
print(string_comparison('котик', 'learn'))
print(string_comparison('кошка', 'котик'))

print ('Работа функции по вводимым данным')

while True:
	frst_word = input ('Введите слово ')
	sec_word = input ('Введите другое слово ')

	result = string_comparison (frst_word, sec_word)
	print(result)

	if result == 'Такого условия нет':
		break


#while string_comparison (first, second) != -1:


