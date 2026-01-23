# range(stop)
# range(start, stop)
# range(start, stop, step)

range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range(1,10)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

range(1,10,2)
# [1, 3, 5, 7, 9]


#---------------------------------------------------


# RANGE STOP

# menyimpan range ke dalam variable
numbers  = range(10)    # range(0,10)

# untuk mengetahui isinya
# gunakan list constructor

print(list(numbers))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# RANGE START, STOP

# menyimpan range ke dalam variable
numbers  = range(1,10)

# untuk mengetahui isinya
# gunakan list constructor

print(list(numbers))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]



# RANGE START, STOP, STEP

# menyimpan range ke dalam variable
numbers  = range(1,10,2)

# untuk mengetahui isinya
# gunakan list constructor

print(list(numbers))
# [1, 3, 5, 7, 9]
# diambil setipa 2 langkah


#----------------------------------------------------------


# INDEXING

#   1. NEGATIVE (kanan-kiri)
#   2. POSITIVE (kiri-kanan)

numbers = range(1,21)
# [1, 2, 3, . . . 18, 19, 20]


# Positive Indexing
numbers[4]
# output: 5

# Negative Indexing
numbers[-3]
# output: 18


#-----------------------------------------------------------


# SLICING

# list[:stop]
# list[start:stop]
# list[start:stop:step]

numbers = list(range(2, 21, 2))
# [2, 4, 6, . . . 16, 18, 20]

print(numbers[:5])
# output: [2, 4, 6, 8, 10]

print(numbers[2:6])
# output: [6, 8, 10, 12]

print(numbers[2:8:3])
#output: [6, 12]