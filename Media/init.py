# Adicionando as notas tiradas das provas. 
# Somando todas as notas  e divido total.

QntsNotas = int(input("Quantas notas?: "))

lista_vazia = []

for count in range(QntsNotas):
    adicionar_Notas = float(input("Qual nota você tirou?: "))
    
    lista_vazia.append(adicionar_Notas)
    
    Media = sum(lista_vazia)
    
    valor_final = Media / QntsNotas
    
print(valor_final)

