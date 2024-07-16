alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
print(len(alfabeto))

def creaCifrado(d: int):
    def cifrar(texto: str):
        resultado = ''
        for item in texto:
            if item in alfabeto:
                # aqui buscamos donde esta el item en index y nos da el indice
                # alfabeto.index("A") = 0
                index = alfabeto.index(item)
                # aqui se suma index + d y cuando lleguemos a 27 de la longitud
                # regresa a 0
                new_index = (index + d) % 27
                # aqui ya vamos agregando cada letra que tenemos en el indice
                resultado += alfabeto[new_index]
            else:
                resultado += item
        return resultado
    return cifrar

c3 = creaCifrado(3)
print(c3('lolailo'))