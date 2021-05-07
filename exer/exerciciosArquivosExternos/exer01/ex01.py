# -*- coding: utf-8 -*-
"""
Escreva uma função que recebe dois nomes de arquivos e 
copia o conteúdo do primeiro arquivo para o segundo arquivo. 
Considere que o conteúdo do arquivo de origem é um texto. 
Sua função não deve copiar linhas comentadas (que 
começam com //) 
"""

def copiarArquivo(velhoarquivo,novoarquivo):
    file1 = open(velhoarquivo,"r")
    file2 = open(novoarquivo,"w")
    while 1:
        text = file1.read(50)
        if text == "":
            break
        file2.write(text)
    file1.close()
    file2.close()
    print("arquivo copiado")
    return

copiarArquivo("velhoarquivo.txt","novoarquivo.txt")       