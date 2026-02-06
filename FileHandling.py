open('filename.txt','x') # membuat file
open('filename.txt','r') # membaca file
open('filename.txt','w') # menulis konten pd file
open('filename.txt','a') # menambah konten pd file


open('file.txt','x')
# Klo nama filenya udah ada, maka error // FileExists

# MEMBACA FILE
# simpan Function dlm variable
# mengambil konten dengan read
# klo nama file yg disebut tdk ada, maka error // FileDoesNotExists
file = open('file.txt','r')
print(file.read())


# MENULIS KONTEN
# simpan Function dlm variable
# menulis konten ke dlm file
# setiap selesai hrs .close()
file = open('file.txt','w')

file.write("Sup Homies")
file.write("\n")
file.write("Searchin' Aequor to be add on my Team")

file.close()


# MENAMBAH KONTEN
# simpan Function dlm variable
# menulis konten ke dlm file
# setiap selesai hrs .close()
file = open('file.txt','a')

file.write("\n")
file.write("NIME is GB's most favorite Person")

file.close()



