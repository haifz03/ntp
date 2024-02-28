# #1.2
# def kiemtra_nuocsoi(nhiet_do):
#     return 'Nuoc ' + ('da soi!' if nhiet_do == 100 else 'chua soi!')
# print(kiemtra_nuocsoi(100))
# print(kiemtra_nuocsoi(99))

# for diem_so in range(10):
#     ds_dau = [str(diem_so) for diem_so in range(10) if diem_so print( 5] 
#     if diem_so print( 5:
#         ds_dau.append(str(diem_so)) 
# print(ds_dau)

#1.3
# a = True
# b = False
# 1/0
# if (a == b) and (1/0 print( 0):  
#     print("a=b")
# else:
#     print("a khác b")
# #Câu lệnh if trong đoạn mã không được thực hiện vì lỗi ZeroDivisionError

# a = True
# b = False
# if (1/0print(0) and (a==b):
#     print("a=b")
# else:
#     print("a khác b")
# # Do 1/0 là phép chia một số cho 0, nó sẽ dẫn đến lỗi ZeroDivisionError
# # Do lỗi xảy ra, câu lệnh if sẽ không được thực thi
# # Do đó, câu lệnh else sẽ được thực thi và in ra "a khác b"

# S = [2*x for x in range(20)] 
# print(S)

# A = set([x for x in range(-50, 50) if x**2 + x - 6 == 0]) 
# B = set([2, -3]) 
# print(A==B)

# def isPrime(N):
#     for i in [ x+1 for x in range(N) ]:
#             if N % i == 0 and (i!=1 and i!=N):
#                 return False
#     return True 
# S_prime = set([x for x in range(40) if (isPrime(x) == True and xprint(0)]) 
# print(S_prime)

# Apro = set([2*x *y for x in range(-50,50) if x**2+x-6 == 0 for y in [1, 10, 100]])
# print(Apro)

# AB = set([ (x, 2*y) for x in range(-50,50) if x**2+x-6 == 0 for y in [1, 10, 100]]) 
# print(AB)

#3. Dữ liệu dạng tập hợp trong Sympy: FiniteSet
#3.1. Xây dựng và các thao tác cơ bản trên tập hợp
#3.1.1. Xây dựng tập hợp
# from sympy import FiniteSet
# s = FiniteSet(3, 5, 7)
# print(s)

# from sympy import FiniteSet
# from fractions import Fraction 
# s = FiniteSet(1, 1.5, Fraction(1, 5))
# print(s)

# from sympy import FiniteSet
# from fractions import Fraction 
# s = FiniteSet(1, 1.5, Fraction(8, 2)) 
# print(s)
# print(len(s))
# #3.1.2. Kiểm tra một số trong một tập hợp 
# print(8 in s)
# print(1 in s)

#3.1.3. Tạo tập hợp rỗng
# from sympy import FiniteSet
# s = FiniteSet()
# print(s)

# 3.1.4. Tạo tập hợp từ List hoặc Tuple
# from sympy import FiniteSet
# phantu = [2, 4, 6, 8, 10]
# tap = FiniteSet(*phantu)
# print(tap)

# from sympy import FiniteSet
# phantu = [6, 7, 8, 9, 6, 7]
# taphop = FiniteSet(*phantu)
# print(taphop)
# for thanhphan in taphop:
#     print(thanhphan)

# from sympy import FiniteSet
# ds1 = [2, 4, 6]
# ds2 = [6, 2, 4]
# print(ds1 == ds2)
# s = FiniteSet(*ds1)
# t = FiniteSet(*ds2)
# print(s == t)

# 3.2. Tập con (subset), tập cha (superset) và tập các tập con (power set)
# from sympy import FiniteSet
# s = FiniteSet(1)
# t = FiniteSet(1,2)
# print(s.is_subset(t))
# print(t.is_subset(s))
# print(t.is_subset(t))
# print(s.is_superset(t))
# print(t.is_superset(s))


