# Tipleri göstər
number=12 #integer type
float_number=34.66 #float type
my_list=["kitab","qelem"] #list type
print(f"""
    {number}`in tipi: {type(number)},
    {float_number}`in tipi: {type(float_number)},
    {my_list}`in tipi: {type(my_list)}
    """)

# 3 dəyərdən ibarət list yarat daha sonra bir dəyəri sil, sonra sildiyin dəyəri əlavə et yenidən
ilist = ["men", "sen", "biz"]  # List yarat
ilist.remove("men")  # "men" elementini sil
ilist.append("size")  # Siyahıya "size" əlavə et
print(ilist)

# Verilmiş şərt daxilində input yaz. Daxil edilən 2 dəyər dən biri digərindən böyükdürsə onda 1 ci dəyərdən 2 ci dəyəri çıx və caavbı yazdır
number1=int(input("Birinci ededi daxil edin: ")) #birinci eded daxil edilir
number2=int(input("İkinci ededi daxil edin: ")) #ikinci eded daxil edilir

if number1>number2: #birinci ededin ikinci ededden boyuk olub olmadigini yoxlayir
    print(f"birinci eded yeni: {number1} boyukdur ikinci ededden yeni: {number2}\n {number1} > {number2}")

elif number1<number2: #ikinci ededin birinci ededden boyuk olub olmadigini yoxlayir
    print(f"ikinci eded yeni: {number2} boyukdur birinci ededden yeni: {number1}\n {number2} > {number1}")

else:
    print(f"Ededler beraberdir")

# Funksiya yaz. Funksiya daxilində 3 input yaz sonda bu inputlar toplanacaq və result olarq cavab qaytaracaq
def Func(): # function yaradilir
    number1 = int(input("Birinci ededi daxil edin: "))  # birinci eded daxil edilir
    number2 = int(input("İkinci ededi daxil edin: "))  # ikinci eded daxil edilir
    number3 = int(input("Üçüncü ededi daxil edin: "))  # üçüncü eded daxil edilir
    result=number1+number2+number3
    return result
print(f" ededlerin cemi: {Func()}")