import itertools
for i in itertools.accumulate([1,2,3,4,5,6,7,8,9,10]):
    print(i)

#Hàm lặp (repeat)
for i in itertools.repeat('Red', 3):
    print (i) 

#Tích Descartes
#Phương pháp 1: Viết đoạn mã thuần bằng Python
for i in ((i,j) for i in [1,2] for j in [6,7,8,9]):
   print (i)

#Phương pháp 2: Sử dụng itertools
import itertools
for i in itertools.product ( [1,2], [6, 7, 8, 9]):
   print (i)
for i in itertools.product('AB', 'C', 'DEF'):
    print(i)
for i in itertools.product('24', 'IT', repeat = 2):
    print (i) 

#Hoán vị (permutation)
from itertools import permutations

for i in permutations ('ABC'):
    print(i)

#Chỉnh hợp chập k từ n (permutation)
from itertools import permutations

for i in permutations ('ABC', 2):
    print (i)
#Tổ hợp (combinations)
for i in itertools.combinations ('ABCDE', 3):
   print (i)

nhaccu = 'Đàn Trống Sáo Bo'.split()
chonmua2mon = list(itertools.combinations(nhaccu, 2))
print(chonmua2mon)

#Tổ hợp có lặp (combinations)
import itertools

for i in itertools.combinations_with_replacement('ABCDE', 3):
    print (i) 

#Xoay vòng giá trị cần lấy
import itertools

for i in itertools.repeat('Red', 3):
    print (i)
