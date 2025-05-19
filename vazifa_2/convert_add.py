""" String to Integers """

def convert_add():
  numbers = []
  while True:
    user_input = input("Son kiriting: (To'xtatish uchun 'q' kiriting) ")
    if user_input == 'q':
      break
    if user_input.isdigit():
      numbers.append(int(user_input))
    else:
      print('Iltimos, son kiriting!')
  return numbers, sum(numbers)