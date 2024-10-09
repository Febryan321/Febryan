usia = int(input("masukan usia anda: "))
darah = int(input("masukan tekanan darah anda: "))

if usia >= 60 and darah > 140:
    print("status kesehatan: Tinggi")
elif usia >= 60 and darah <= 140:
    print("status kesehatan: Normal")
elif usia < 60 and darah > 130:
    print("status kesehatan: Tinggi")
elif usia < 60 and darah <= 130:
    print("status kesehatan: Normal")