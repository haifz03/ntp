import random

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
rand5_char = random.sample(chars, 5)
print (rand5_char)
print(random.sample(range(10, 100), 15))
print(random.sample(range(100), 10))# với Python 2.x câu lệnh là: xrange(100)
print(random.randrange(20, 100, 2))# số ngẫu nhiên chẵn do 20 là chẵn và bước nhảy bằng 2 
print(random.randrange(50, 500))
print(random.randrange(6))
print(random.choice(['Táo', 'Lê', 'Ổi', 'Chuối']))
print(random. uniform(4.9, 10.0)) # a = 4.9 và b = 10, số ngẫu nhiên trong khoảng [4.9, 10.0) 
print(random.random()) # random số thực (float)
