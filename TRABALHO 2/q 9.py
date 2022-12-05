def qualamaiorpalavra(maiorpalavra_list):
    maiorpalavra = [ ]
    for n in maiorpalavra_list:
        maiorpalavra.append((len(n).n))
    maiorpalavra.sort()
    return maiorpalavra[-1][1]
print(qualamaiorpalavra("janeiro","fevereiro","março"))