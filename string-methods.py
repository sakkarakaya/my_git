website = "http://www.qwertasdfg.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

m = " Hello World "
# m = m.replace(" ", "")
m = m.strip()
print(m)


kucuk_course = course.lower()
print(kucuk_course)

kactane_a = website.count("a")
print(kactane_a)

basliyormu = website.startswith("www")
bitiyormu = website.endswith("com")
print(basliyormu)
print(bitiyormu)

varmı = website.find(".com")
print(varmı)

alfamı = course.isalpha()
digitmi = course.isdigit()
print(alfamı)
print(digitmi)

