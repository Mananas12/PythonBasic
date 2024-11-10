# Հայտարարել list,  որը բաղկացած է string-ներից: 
# List-ում եղած բոլոր string-ները դարձնել փոքրատառ և 
# տպել յուրաքանչյուրը հակառակ հերթականությամբ:

ls = ["barev", "heLLo", "HOLA"]

res = [i.lower() for i in ls ]
print(res[::-1])
