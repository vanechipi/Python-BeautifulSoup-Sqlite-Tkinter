def esSubCadena(lista1, lista2):
    print "La cadena contiene a la subcadena: ", lista1.count(lista2), "veces"

if __name__ == "__main__":
    esSubCadena("subcadenasubcadenasubcadena","cadena")

def ordenAlfabetico(lista1, lista2):
    lista3= [lista1, lista2]
    lista3.sort()
    return lista3[0]

if __name__ == "__main__":
    print "--------------------"
    print "En orden alfabetico gana:", ordenAlfabetico("omega","way")

