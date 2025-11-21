#arithmetic operator

#   OPERATOR                    NAME
# .....................................
#      +                Addition
#      -                Substraction
#      *                Multipication
#      /                Division
#      %                Modulus
#      **               Exponentitation
#      //               Floor Division


#arithmetic operation

#langsung dalam print
print(50 + 18)

#melalui Variabel
number1 = 50
number2 = 18
result= number1 + number2
print(result)


a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
result = int(a) + int(b)


a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
result = int(a) * int(b)

print(a, "*", b, "=", result)

print("Division Calculator")
print("--------------------")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
result = int(a) / int(b)

print(a, "/", b, "=", result)

print("Power Calculator")
print("-----------------")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
result = int(a) ** int(b)

print(a, "**", b, "=", result)