website = "http://www.qwertasdfg.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

course_length = len(course)
print(course_length)

print(website[7:10])

print(website[-3:])

print(course[0:15])

print(course[-15:])

print(website[::-1])



ad, soyad, yas, meslek = "Bora", "Yilmaz", 32, "muhendis"

yaz1 = "benim adim " + ad + " " + soyad + ", yasim " + str(yas) + " meslegim " + meslek
print(yaz1)

yaz2 = "adim {} {} yasim {}".format(ad, soyad, yas)
print(yaz2)

yaz3 = f"adim {ad}"
print(yaz3)



abc = "abc"

print(abc*3)