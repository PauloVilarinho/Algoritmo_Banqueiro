

def printar_matriz(matriz):
    text = ""
    count = 1
    for x in matriz:
        for y in x:
            if count != len(x):
                text += str(y) + " "
                count += 1
            else :
                text += str(y) + "\n" 
                count = 1
    return text
    