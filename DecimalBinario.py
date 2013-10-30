def Binario2Decimal(binario):
    n=len(binario)
    valor=0
    for bit in binario:
         if bit == '1':
             valor=valor+2**(n­1)
         n ­=1
    return valor
