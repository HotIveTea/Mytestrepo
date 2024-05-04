# def fibnobacci(n):
#     if n <= 1:
#         return 1
#     else:
#         return fibnobacci(n-1) + fibnobacci(n-2)
# number = int(input("Nhap so nguyen: "))
# for i in range(number):
#     print(fibnobacci(i)) 
# # def fibonacci(n):
# #     f0 = 1
# #     print(f0)
# #     f1 = 1
# #     print(f1)
# #     for i in range(2, n):
# #         f = f1 + f0
# #         print(f)
# #         f0 = f1
# #         f1 = f
# # number = int(input("Nhap so nguyen: "))
# # fibonacci(number)        
# def fibonacci(n):
#     a, b = 0, 1
#     while a < n:
#         yield a
#         a, b = b, a+b
# number = int(input("Nhap so nguyen: "))
# fib = fibonacci(number)
# for i in fib:
#     print(i)         
# while True:
#     n = float(input("Nhap so khac 0: "))
#     if n == 0:
#         print("Vui long nhap lai")
#     else:
#         break    
for i in range(0,100):
    print("Ác")