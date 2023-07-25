

# Sistema Bancário Otimizado <img src='https://raw.githubusercontent.com/gist/ManulMax/2d20af60d709805c55fd784ca7cba4b9/raw/bcfeac7604f674ace63623106eb8bb8471d844a6/github.gif' width='80' height='80' >


##  Objetivo da otimização do Sistema Banário
Separar funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## Desafio

O desafio é deixar o código mais modularizado, para isso foi criado funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do novo sistema foi implementado duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

## Saque

A função saque recebe os argumentos apenas por nome (keyword only). 
Argumentos: saldo, valor, extrato, limite, numero_saque, limite_saque.
Retorno: saldo e extrato.


## Depósito

A função depósito recebe os argumentos apenas por posição (positional only). 
Argumentos: saldo, valor, extrato. Retorno: saldo e extrato.
    
## Extrato 

A função extrato recebe os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo. Argumentos nomeados: extrato.
 
## Novas funções 

Duas novas funções implementadas: criar usuário e criar conta corrente. 

## Criando usuário(cliente) 

O programa armazena os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradorouro, nro - bairro - cidade/sigla estado. E é armazenado somente os números do cpf. Não cadastramos 2 usuários com o mesmo cpf.

## Criando conta corrente

O programa armazena contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta e sequencial, iniciando em 1. O número da agência é fixo: '0001'. O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

##
##
Para vincular um usuário a uma conta, filtramos a lista de usuários buscando o número do cpf informado para casa usuário da lista. 

