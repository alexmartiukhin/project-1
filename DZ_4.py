
#1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)

# string = input("Enter the sentence: ")
# letters_quantity = 0
# digits_quantity = 0
#
# for count in string:
#     if count.isalpha():
#         letters_quantity += 1
#
#     elif count.isnumeric():
#         digits_quantity +=1
#
#
# print(f"Letters quantity is: {letters_quantity}")
# print(f"Digits quantity is: {digits_quantity}")


#2. Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте скільки разів у рядку
# зустрічається потрібний символ. Отримане число виведіть на екран.

# string = input("Enter the string: ")
# symbol = input("Enter symbol for the search: ")
#
# quantity = 0
#
# for new_number in string:
#     if new_number == symbol:
#         quantity += 1
#
# print(f"symbol {symbol} appeared in string {quantity} times")


#3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.

# string = input("Enter the string: ")
# search_word = input("Enter word for searching: ")
# replace_word = input("Enter the word to replace: ")
#
# string = string.replace(search_word, replace_word)
#
# print(string)


#4. Дано рядок. (зробити зрізи)

# text = "I enjoy studying at Hillel IT school"
#
# #Спершу виведіть третій символ цього рядка.
# print(text[2:3])
#
# #У другому рядку виведіть передостанній символ цього рядка.
# print(text[-2:-1])
#
# #У третьому рядку виведіть перші п'ять символів цього рядка.
# print(text[:5])
#
# #У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# print(text[:-2])
#
# #У п'ятому рядку виведіть усі символи з парними індексами
# # (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
# print(text[::2])
#
# #У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# print(text[1::2])
#
# #У сьомому рядку виведіть усі символи у зворотному порядку.
# print(text[::-1])
#
# #У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# print(text[::-2])
#
# #У дев'ятому рядку виведіть довжину цього рядка.
# print(len(text))

