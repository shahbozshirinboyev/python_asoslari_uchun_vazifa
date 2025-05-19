"""
Username Generator
"""
import random

def user_name():
  name = input("Ismingizni kiriting: ").lower()
  if name:
    username = ''.join(reversed(name))
    random_number = str(random.randint(0, 9))
    return f"Siz uchun generatsiya qilingan username: {username+random_number}"
  else:
    return f"Iltimos, ism kiriting..."