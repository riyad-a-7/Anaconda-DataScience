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
