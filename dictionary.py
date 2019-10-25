# ogrenciler = {
#     "120" : {
#         "ad" : "Ali",
#         "soyad" : "Yılmaz",
#         "tel" : "532 1"
#     }
#     "121" : {
#         "ad" : "Can",
#         "soyad" : "Korkmaz",
#         "tel" : "532 2"
#     }
#     "122" : {
#         "ad" : "Volkan",
#         "soyad" : "Yukselen",
#         "tel" : "532 3"
#     }
# }

dic = {}

no1 = input("no gir: ")
ogrenci1 = input("ad gir: ")
no2 = input("no gir: ")
ogrenci2 = input("ad gir: ")
no3 = input("no gir: ")
ogrenci3 = input("ad gir: ")

dic.update({
    no1:{
         "ad" : ogrenci1,
         "soyad" : "Yılmaz",
         "tel" : "532 1"
    }
   }
)
print(dic)