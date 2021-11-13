cpf_valido = '16899535009'

cpf = '168995350'
multiplicador = 10
resul_multi = []

for n_cpf in cpf:

    n_cpf = int(n_cpf)

    resul_multi_temp = n_cpf * multiplicador
    print(n_cpf * multiplicador)
    resul_multi.append(resul_multi_temp)
    multiplicador -= 1

print(resul_multi)

n1, n2, n3, n4, n5, n6, n7, n8, n9 = resul_multi

resultot = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9

print(resultot)
codicao1 = (11 - (resultot % 11))

if codicao1 > 9:
    digito1 = 0
else:
    digito1 = codicao1

print(f'O primeiro dígito é: {digito1}.')

cpf2 = '1689953500'
multiplicador2 = 11
resul_multi2 = []

for n_cpf2 in cpf2:

    n_cpf2 = int(n_cpf2)

    resul_multi_temp2 = n_cpf2 * multiplicador2
    print(n_cpf2 * multiplicador2)
    resul_multi2.append(resul_multi_temp2)
    multiplicador2 -= 1

print(resul_multi2)

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = resul_multi2

resultot2 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9

print(resultot2)
codicao2 = (11 - (resultot2 % 11))

if codicao2 > 9:
    digito2 = 0
else:
    digito2 = codicao2
print(f'O segundo dígito é: {digito2}.')

if cpf == cpf_valido:
     print(f'Esse cpf é válido.')
else:
    print('Esse cpf não é válido.')

