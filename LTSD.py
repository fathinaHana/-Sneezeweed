# LIST
# Membuat list dengan biasa
names = ["GB", "Naha", "Nime"]

# Mwmbuta list dengan list constructor
names = list(("Dwelle", "Darren", "Hans"))

# Membuat list dari itarable object
name = "Hans"
letters = list(name)


    # Indexing list
# urutan dimulai dari 0
names =["Pickman", "Sorel", "Helot"]
#           0         1        2

# Mengakses item
print(names[2])
# Output: Helot

    # Manipulasi List
names = ["Casiah", "Clementine", "Corposant"]

# Nambah item
names.append("Celeste")

# Ubah item
names[0] = "Castor"

# Menghapus item
names.remove("Corposant")




# TUPLE
# Membuat Tuple dengan biasa
names = ("Pollux", "Uvhash", "Hameln")

# Mwmbuta Tuple dengan Tuple constructor
names = tuple(("Lotan", "Salvador", "Tulu"))

# Membuat Tuple dari itarable object
name = "Agrippa"
letters = tuple(name)


    # Indexing list
# urutan dimulai dari 0
names = ("Jenkins", "Doll", "Sanga")
#            0         1       2

# Mengakses item
print(names[2])
# Output: Sanga

    # Aslinya Tuple gabisa dimanipulasi, tapi bisa diakalin dengan cara konversi ke LIST:
names = ("Pandia", "Nymphea", "Aigis")

# Konversi kedalam List
names_list = list(names)

# Lakukan manipulasi (harus ada _list)
names_list.append("24")
names_list[2] = "Liz"
names_list.remove("Pandia")

# Konversi ke dalam Tuple kembali
names = tuple(names_list)




# SET
# Membuat Set dengan biasa
names = {"Tawil", "Goliath", "Nautila"}

# Mwmbuat set dengan Set constructor
names = set(("Ryker", "Thais", "Aurita"))

# Membuat Set dari itarable object
name = "Faint"
letters = set(name)

# Set ga ada indexing, karena mereka ga berurut
names = {"Miryam", "Ramona", "Lily"}
print(names)

# masing-masing itemnya ga bisa di akses
print(print[2]) # Ini  bakal error

    # Manipulasi item
# Secara bawaan, manipulasi dalam set hanya bisa menambahkan dan menghapus item

names = {"Faros", "Erica", "Karen"}

# Menambhaakan item baru
names.add("Daffodil")

# Menghapus item: .discard
# Item tidak ada = tdk error
names.discard("Faros") 

# Menghapus item: .remove
# Item tidak ada = error
names.remove("Erica") 

# Menghapus item: .pop
# Hapus acak
names.pop()




# DICTIONARY
# Membuat Dictionary dengan biasa
awakener = {'name':'Doresain', 'realm':'Caro'}

# Membuat Dictionary dengan dict constructor
awakener = dict(name = 'Doresain', realm = 'Caro')

    # Format penulisan Dictionary
# Bisa menyusun ke bawah
awakeners = {
    'name' : 'Murphy',
    'realm' : 'Aequor',
    'height' : '4,8.7',
    'active' : 'True',
    'Personality' : [
            'Proud'
            'Willful'
            'Self-centered'
        ]
}

    # Akses Dictinary
# Mengakses value
print(awakeners['realm'])

# Menambahkan key:value baru
awakeners['rarity']  = 'SSR'

# Mengubah key:value yang ada
awakeners['height'] = '5,9.8'

# Menghapus key:value
# Sebutkan key pda .pop()
awakeners.pop('active')

# Menghapus key:value terakhir
awakeners.popitem()