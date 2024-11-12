# Գրեք ծրագիր, որը ամբողջ թվային զանգվածի բոլոր զույգ էլեմենտները  
# նույն զանգվածի մեջ՝ կտեղավորի զանգվածի սկզբից, իսկ կենտերը վերջից:

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls_even = []
ls_odd = []

for i in ls:
    if i % 2 == 0:
        ls_even.append(i)
    else:
        ls_odd.append(i)
    
ls = []

ls += ls_even
ls += ls_odd 
print(ls)