print("Hello GitHub")
def fibnonanic(n):
  a, b = 0, 1
  while a < n:
    yield a 
    a, b = b, a + b
number = int(input("Nhap so nguyên n: )
fib = fibnonanic(number)
for i in fib:
  print(i)
    
