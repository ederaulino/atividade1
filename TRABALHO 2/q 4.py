def maior_numero( list ):
    max = list [ 0 ] 
    for a in list:
        if a > max:
            max = a
    return max
print(maior_numero([1, 5, 8, 0]))
