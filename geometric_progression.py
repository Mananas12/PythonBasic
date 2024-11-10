#Հայտարարել list, պարզել այն հանդիսանում է երկրաչափական պրոգրեսիա թե ոչ։

def geometric(ls):
    q = ls[1] / ls[0]
    
    for i in range(len(ls) - 1):
        if ls[i + 1] / ls[i] != q:
            return False
    return True

ls = [2, 6, 18, 54]

if geometric(ls):
    print("geometric progression")
else:
    print("none geometric progression")


