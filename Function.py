# menmbuat Function
def sayHello():
    print("Selamat Datang!")

# mengjalankan Function
sayHello()


# ==== print: running langsung
# ==== return: tambah function print buat keliatan


# kata kunci return
def sayHello():
    return "Selamat Datang!"

# mengjalankan Function
print(sayHello())



# Function Arguments
def sayHello(name):
    return "Selamat Datang, " + name

# mengjalankan Function
print(sayHello("Charlotte"))



# menambahkan argumen
# lebih dari satu
def addition(num1, num2):
    result = num1 + num2
    print(num1, "+", num2, "=", result)

#memanggil function
# dengan argumen lebh dari satu
addition(30, 51)



# Function Default Arguments // akan menjadi error
#def sayHello(name):
#    return "Selamat Datang, " + name

#print(sayHello())



# menerapkan default arguments
# argumen sudah memiliki nilai bawaan
#def sayHelo(namee=""):
#    return "Selamat Datang, " + namee

# mengjalankan Function
# tanpa argumen
#print(sayHello())



# Keywornd Arguments
def fullname(xname, yname=""):
    return xname + " " + yname

#tanpa argumen yang berurutan
print(fullname(xname="Moran", yname="Greenor"))



# ARGS // Arbitary Arguments
# ga bisa bikin argumen pd tanda kurung
# tidak harus menghitung jumlah argumennya
def substraction(*numbers):
    result = 0

    for n in numbers:
        result += n

    return result



# **KWARGS // Arbitary Keyword Arguments
# Keyword n Argumen bisa sebanyak2nya
def allname(**kwargs):
    values = kwargs.values()
    print(" ".join(values))

allname(a="Lilliam", b="Acra", c="Sara", d="Dwelle", e="Darren", f="Hans")