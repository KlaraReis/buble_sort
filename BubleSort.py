
def bubble_sort(array):
    array_tamanho = len(array)
    valor = False
    for j in range(array_tamanho - 1):
        if array[j] > array[j + 1]:
            valor = True
            array[j], array[j + 1] = array[j + 1], array[j]
        if not valor:
            return


# Teste da logica acima
array = [72, 68, 2014, 45, 112,]

print("Os valores do array eh, ")
print(array)

bubble_sort(array)

print("Aplicando o BubleSort:")
for i in range(len(array)):
    print("% d" % array[i], end=" ")

