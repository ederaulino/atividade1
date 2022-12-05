def menor_numero( list ):
    min = list [ 0 ] 
    for a in list:
        if a < min:
            max = a
    return max
print(menor_numero([1, 5, 8, 0]))