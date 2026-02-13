# Format syntax Lambda
# Lambda Arguments : Expressions
lambda name : print("Selamat Datang", name)

# Membuat Lambda
lambda name : print("Selamat Datang", name)

# Lambda dlm Variable
sayHello = lambda name : print("Selamat Datang", name)

# Variable sayHello sdh mnjd Function
sayHello("Tei")


# Tanpa menyimpan ke Variable // ttp jalan
(lambda : print("Selamat Datang"))()

# Lambda dngn Argument // name
(lambda name : print("Selamat Datang", name))("Shuraka")

# lambda dngn Default Argument
(lambda name="" : print("Selamat Datang", name))()
