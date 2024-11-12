# Հայտարարել ֆունկցիա, որը կստանա երկու set և կվերադարձնի True, 
# եթե մեկը մյուսի ենթաբազմություն է, False հակառակ դեպքում:

def checker(set1: set, set2: set) -> bool:
    if len(set1) > len(set2):
        if set2 - set1 == set():
            return True
        else:
            return False
    if len(set2) > len(set1):
        if set1 - set2 == set():
            return True
        else:
            return False
        
set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 6, 4}

print(checker(set1, set2))