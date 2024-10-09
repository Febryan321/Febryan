nilai = int(input("masukan nilai ujian anda (0-100): "))

if 100 >= nilai >= 90:
    print("feedback: sangat baik")
elif 80 <= nilai <= 89:
    print("feedback: baik")
elif 70 <= nilai <= 79:
    print("feedback: cukup")
elif 60 <= nilai <= 69:
    print("feedback: kurang")
else:
    print("feedback: sangat kurang")