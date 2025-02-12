number=12 #integer type
float_number=34.66 #float type
my_list=["kitab","qelem"] #list type
print(f"""
<<<<<<< HEAD
    {type(number)},
    {type(float_number)},
    {type(my_list)}
=======
    {dir(number)},
    {dir(float_number)},
    {dir(my_list)}
>>>>>>> 216c9506c2d06d7d939321d6dafdde66dff212df
    """)