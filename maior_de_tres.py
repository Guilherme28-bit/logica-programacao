a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print(f"Maior: {maior}")
