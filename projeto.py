import os
import time

def limpar():
    return os.system('cls')

class Cliente:
    def __init__(self, nome, cpf, status, quarto, total):
        self.nome = nome
        self.cpf = cpf
        self.status = status
        self.quarto = quarto
        self.total = total
        pass

class Quarto:
    def __init__(self, numero, status):
        self.numero = numero
        self.status = status
        #Vago = 0
        #Ocupado = 1
        pass

def CriarListaQuartos():
    totQuartos = 9
    ListaQuartos = [None]*totQuartos
    for i in range(0,totQuartos//3):
        ListaQuartos[i] = (Quarto(101+i, 0))
        ListaQuartos[i+(totQuartos//3)] = (Quarto(201+i, 0))
        ListaQuartos[i+(totQuartos*2//3)] = (Quarto(301+i, 0))
    return ListaQuartos


def Cardapio():
    limpar()
    respTipoConsumo = int(input("[1] Lanches\n[2] Bebidas\n[3] Sobremesas\n[4] Voltar\n\nSelecione a opcao desejada  "))
    if respTipoConsumo == 1:
        OpcoesLanches() #Menu de lanches
    elif respTipoConsumo == 2:
        OpcoesBebidas() #Menu de bebidas
    elif respTipoConsumo == 3:
        OpcoesSobremesas() #Menu de sobremesas
    elif respTipoConsumo == 4:
        ServicoDeQuarto() #Menu anterior(Servicos de quarto)
    else:
        ErroMenu()
        Cardapio()

def OpcoesLanches():
    limpar()
    consumo = int(input("[1] Hamburguer + batata\n[2] Batata com chedar\n[3] Caviar\n[4] Voltar\n\nSelecione a opcao desejada  "))
    if consumo == 1 or consumo == 2 or consumo == 3:
        print("Certo, seu pedido foi feito") #Criar funcao que adiciona esse item na comanda do quarto
    elif consumo == 4:
        Cardapio() #Menu anterior(Cardapio)
    else:
        ErroMenu()
        OpcoesLanches()

def OpcoesBebidas():
    limpar()
    consumo = int(input("[1] Champagne\n[2] Coca Cola\n[3] Agua mineral\n[4] Voltar\n\nSelecione a opcao desejada  "))
    if consumo == 1 or consumo == 2 or consumo == 3:
        print("Certo, seu pedido foi feito")
    elif consumo == 4:
        Cardapio()
    else:
        ErroMenu()
        OpcoesBebidas()

def OpcoesSobremesas():
    limpar()
    consumo = int(input("[1] Torta de chocolate\n[2] Mousse de limao\n[3] Voltar\n\nSelecione a opcao desejada  "))
    if consumo == 1 or consumo == 2:
        print("Certo, seu pedido foi feito")
    elif consumo == 3:
        Cardapio()
    else:
        ErroMenu()
        OpcoesSobremesas()

def OpcoesRelacQuarto():
    limpar()
    consumo = int(input("[1] Solicitar limpeza extra do quarto\n[2] Solicitar Massagem\n[3] Voltar\n\nDigite o numero da opcao desejada"))
    if consumo == 1 or consumo == 2:
        print("Certo, seu pedido foi feito")
    elif consumo == 3:
        ServicoDeQuarto()
    else:
        ErroMenu()
        OpcoesRelacQuarto()


def ErroMenu():
    print("ERRO !! Digite somente os numeros do menu")
    time.sleep(1)


def ServicoDeQuarto():
    limpar()
    respServico = int(input("[1] Cardapio\n[2] Relacionados ao quarto\n[3] Voltar\n\nDigite o numero do servico desejado  "))
    if respServico == 1:
        Cardapio()
    elif respServico == 2:
        OpcoesRelacQuarto()
    elif respServico == 3:
        MenuMorador()
    else:
        ErroMenu()
        ServicoDeQuarto()

def MenuMorador():
    limpar()
    respMorador = int(input("[1] Solicitar servico de quarto\n[2] Telefones uteis do interfone\n\nDigite o numero desejado  "))
    if respMorador == 1:
        ServicoDeQuarto()
    elif respMorador == 2:
        limpar()
        voltar = str(input("Recepcao: 228\nEnfermaria: 505\n\nDeseja voltar ao menu? [s/n]  "))
        voltar = voltar.lower()
        if voltar == "s":
            MenuMorador()
        elif voltar == "n":
            limpar()
            print("processo finalizado")
    else:
        ErroMenu()
        MenuMorador()



#0 = Lead (nao atribuido)
#1 = Reservado
#2 = Cancelado
#3 = CheckedIn
#4 = CheckedOut

#Lista de Quartos
ListaQuartos = CriarListaQuartos()
pessoa1 = Cliente("Lucas", "17765772724", 0, 101, 0.0)
MenuMorador()


