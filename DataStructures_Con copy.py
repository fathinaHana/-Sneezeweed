# Condition IF, IF ELSE, Elif

score = 50
min_criteria = 75

if score >= min_criteria:
    print("Anda berhasil naik level!")
elif score < min_criteria:
    print("Anda belum berhasil naik level!")
else:
    print("Nilai anda tidak ditemukan")


# LOOP WHILE n FOR

# While
# tergantung kondisi yang dikasih
number = 10

while number <= 10:
    print("I Like Python")
    number ++ 1

# For
# dikasih range sendiric
numbers = range(10)

# n merupakan variabel baru
# yang akan menyimpan masing2 item
# dari iterable object
for n in numbers:
    print("I Like python")