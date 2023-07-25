import textwrap

def menu():
    menu = """\n
    *************** MENU **************
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo Usuário
    [q] Sair
    ************************************

    => \n"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('\n Deposito Realizado com sucesso!\n')
    else:
            print('Operação falhou: O valor informado é invalido.')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = numero_saque >= limite_saque
    
    if saldo_excedido:
        print('Operação falhou! Voce não possui saldo suficiente.')
        
    elif limite_excedido:
        print('Operação falhou! Seu limite esta excedido.')
        
    elif saque_excedido:
        print('Operação falhou! Seu número de saque está excedido.')
        
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        numero_saque += 1
        print('\n DINHEIRO SACADO COM SUCESSO!!!')
    else: 
        print('Operação falhou! Informe um valor válido!')
      
    return saldo, extrato
    
def tela_extrato(saldo, /, *, extrato):
    print('\n***************EXTRATO***************\n')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('*****************************************')

def novo_usuario(usuarios):
    cpf = input('Informe o CPF (apenas os números): ')
    usuario = filtrar_usu(cpf, usuarios)
    
    if usuario:
        print('Esse número de CPF já está vinculado a outra conta.')
        return
        
    nome = input('Informe seu nome completo: ')
    data_nasc = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradorouro, nro - bairro - cidade/sigla estado): ')
    usuarios.append({'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'endereco': endereco})
    print('Usuário criado com sucesso!')
    
def filtrar_usu(cpf, usuarios):
    usuarios_filter = [usuario for usuario in usuarios if usuario['cpf']== cpf]
    return usuarios_filter[0] if usuarios_filter else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF (apenas os números): ')
    usuario = filtrar_usu(cpf, usuarios)
    if usuario:
        print("\nConta criada com sucesso!")
        return {'agencia':agencia ,'numero_conta': numero_conta,'usuario':usuario}
    print('Usuário não encontrado, fluxo de criação encerrado!')
    
def lista_contas(contas):
    for conta in contas:
        linha = f"""\
        Agencia: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print('*' * 100)
        print(textwrap.dedent(linha))
        print('*' * 100)

def main():
    Agencia = '0001'
    limite_saque = 3
    saldo = 0
    limite = 500
    extrato = '' 
    numero_saque = 0
    usuarios = []
    contas = []
    
    while True: 
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))
            
            saldo, extrato = depositar(saldo, valor, extrato)
             
                
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saque = numero_saque,
                limite_saque = limite_saque
            )
            
        elif opcao == 'e':
            tela_extrato(saldo, extrato= extrato)
           
        elif opcao == 'nu':
            novo_usuario(usuarios)
            
        elif opcao == 'nc':
            numero_conta = len(contas) + 1 
            conta = nova_conta (Agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                
        elif opcao == 'lc':
            lista_contas(contas)
        
        elif opcao == 'q':
            print('Sair')
            break
            
        else: print('Operação inválida, favor selecionar a operação desejada.')

main()