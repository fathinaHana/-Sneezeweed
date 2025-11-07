print("Selamat Siang")
print("Hello World")

print("Selamat", end=" ")
print("Datang")




name = "James"
#Variabel dengan nama "name"
#Berisi nilai "James"

_name = "Noel"            #Boleh
full_name = "Nam Ae-ri"   #Boleh
name2 = "Myungsoo"        #Boleh

name3 = "Luke"
Name3 = "Andrew"
#Dua variabel di atas adalah berbeda



#Tidak perlu seperti ini
name4 = "Theodore"
print("Theodore")

#Cukup seperti ini
name4 = "Theodore"
print("name4")




name6 = "Elios"

#Dengan koma ( , )
print("Selamat Datang", name6, "!")

#Dengan plus ( + )
print("Selamat Datang" + name6 + "!")




#beri nilai pada variabel
first_name = "Ae-ri"
last_name = "Nam"

#beri nilai pada variabel
#dari nilai variabel lain
full_name = first_name + " " + last_name
print(full_name)


#variabel denngan nilai awal
name9 = "Seungha"
print("Selamat Datang", name9, "!")

#variabel dipanggil lagi
#dan diberi nilai yang berbeda
name9 = "Jaewook"
print("Selamat Datang", name9, "!")

#..........................................................................

# INPUT FUNCTION 

#inptu ()
#diikuti dengan kalimat permintaan
input("Masukkan nama anada: ")

name10 = input("Masukkan nama Anda: ")
print("Selamat Datang", name, "!")


#PHYTON Data Types

#   TYPE                    DATA TYPE
# .....................................
#   Text                    str
#   Numeric                 int, float, complex
#   Sequence                list, tuple, range
#   Mapping                 dict
#   Boolean                 bool
#   NoneType                None

#string (str)
#kombinasi huruf, text, angka
#di dalam kkutip ( " " )
name11 = "Hong-gyu"

#integer (int)
#angka bulat, bukan koma2an
number = 100

#float
#angka pecahan (koma2an)
pi = 3.14

#complex
#gabungan antara: bilangan real dan imajiner
complex_number = 1+2j

#list
#kumpulan banyak data (pake tanda "[]" )
number_list = [1, 2, 3]

#tuple
#kumpulan banyak data (tp pake tanda "()" )
number_tuple = (1, 2, 3)

#Mapping/dictionary (dict)
#menyimpan kumpulan data
#format key:value
student = {'name':'Lu Yang', 'age':31}

#boolean (bool)
#hanya berisi 2 kemungkinan
#True or False
active = True

#NoneType (None)
#berarti kosong (empty)
#tidak ada apa2
data =  None


#........................................


#DATA TYPE

#klo mau tau tipe data dari variabel tertentu pake funct type()
name12 = "Darren"
print(type(name12))


#DATA TYPE CONVERSION

#str()
#mengubah ke tipe data string
number = 5
text = str(number)

#int()
#mengubah ke tipe data integer
text = "99"
number = int(text)

#float ()
#mengubah ke tipe data float
number = 123
float_number = float(number)