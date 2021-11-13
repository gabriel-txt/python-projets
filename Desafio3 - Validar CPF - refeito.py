while True:
    cpf = (input('Digite o cpf para saber se é válido: (Digite 0 para parar) '))
    if cpf == '0':
        break
    novocpf = [cpf[0:-2]]
    cont = soma = 0
    for n in range(10, 1, -1):
        soma += int(novocpf[0][cont]) * n
        cont += 1
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    novocpf.append(str(digito))
    cont = soma = 0
    for m in range(11, 1, -1):
        if m == 2:
            soma += int(digito) * m
        else:
            soma += int(novocpf[0][cont]) * m
            cont += 1
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    novocpf.append(str(digito))
    novocpf = ''.join(novocpf)
    if novocpf == cpf:
        print(f'O cpf {cpf} é válido.')
    else:
        print(f'O cpf {cpf} não é válido, sua versão validado corretamente seria: {novocpf}')
