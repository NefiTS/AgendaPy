#Definição de funções

agenda = [] # Criando a lista vazia

#Descrição : Este procedimento cria um novo contato na agenda

#Nome : novo()

#Tipo : procedimento

def novo():
    global agenda # Definindo a variavel como global
    nome = p_nome()
    celular = input("Celular ....:")
    email = input("E-mail...:")
    agenda.append([nome, celular, email])# adicionando os dados na agenda
    print(
        '''

        -----------------------------------------------------------------

        Registro gravado com Sucesso !


        -----------------------------------------------------------------


        '''
    )

#Descrição : Este procedimento lê o um nome
#Nome : p_nome()
#Tipo : procedimento

def p_nome():
    return(input("Nome.....:"))




# Descrição: Este procedimento lista um registro
# Nome: listar_dados(nome, celular, email)
# Tipo: procedimento
def listar_dados(nome, celular, email):
    print("Nome: %s\nCelular: %s\nEmail: %s" % (nome, celular, email))
    print("----------------------------------")


#Descrição : Este procedimento lista todos os registros da matriz

#Nome: listar()

#Tipo : procedimento

def listar(): #Função para mostrar lista de contatos
    print('''
    
    Contatos da Agenda ########@@@@@@@@

    ''')
    for e in agenda:
        listar_dados(e[0], e[1], e[2])
    print('''
    
    FIM DA AGENDA ########@@@@@@@@
    
    ''')

#Descrição : Esta função pesquisa um contato pelo nome

#Nome : pesquisa(nome): int

#Tipo : função

def pesquisa(nome): #Função para pesquisar contatos
    name = nome.lower()
    for d, e in enumerate(agenda): #percorre toda a matriz
        if e[0].lower() == name: #procura o nome desejado
            return d # representa o indice do nome encontrado
        return None # retorna vazio se não encontrar


#Descrição: Este procedimento exibe o registro ou mensagem de insucesso

#Nome : pesquisar():

#Tipo procedimento

def pesquisar():
    #pesquisar o nome
    p = pesquisa(p_nome()) # Entrada de dados
    if p != None:
        print (" Registro Encontrado")
        #Atualiza as variaveis se encontrou
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        #mostra o registro
        listar_dados(nome, celular, email)
    else:
        #Exibe a mensagem de insucesso na procura do registro

        print('''
        
        Nome não encontrado !!!
        
        ''')



#Descrição : Este procedimento apaga um contato

#Nome: apagar

#Tipo: procedimento

def apagar():
    global agenda
    nome = p_nome()
    #retorna o indice do nome ou vazio
    p = pesquisa(nome)
    if p != None : # Se encontrou o contato
        del agenda[p] #exclui o contato
        print('''
        
        Registro apagado com Sucesso !!!
        
        ''')
    else:
        #Não encontrou o registro para excluir
        print("Nome não encontrado")

# Descrição: Este procedimento edita um contato
# Nome: editar():
# Tipo: procedimento
def editar():
    p = pesquisa(p_nome())  # Entrada de dados.
    # Se encontrou o registro
    if p != None:
        # mostra o nome e pede a edição dos demais
        nome = agenda[p][0]
        print("Nome........: ", nome)
        celular = input("Celular....:")
        email = input("E-mail.....:")
        agenda[p] = [nome, celular, email]  # Armazenando os novos dados.
        print('''
-----------------------------
              
Registro EDITADO com Sucesso!!!
"
              -------------------------------''')
    else:
        print("Nome não encontrado.")  # Executa caso a condição seja falsa.

#Descrição : Esta função valida se o item digitado foi valido

#Nome : validar(pergunta, inicia, fim): int

#Tipo : função
def validar(pergunta, inicio, fim): #Função para validar números inteiros
    while True: # Criando um loop infinito
        try: # Criando o acordo/condição
            valor = int(input(pergunta)) #entrada de dados
            if inicio <= valor <= fim : #determina a condição
                return(valor) #executa se for verdadeiro
            else:
                return(0)
        except ValueError : #Executa caso for falsa
            print("Valor inválido, favor digitar entre %d e %d " % (inicio, fim))

#Descrição : Esta função retorna o item do menu ou 0 para invalido
#Nome : menu(pergunta, inicia, fim) : int
#Tipo : função

def menu(): #Função que exibe o menu de opções
    print('''
    
    1 - Adicionar Contato

    2 - Editar Contato

    3 - Pesquisar Contato

    4 - Editar Contato

    5 - Apagar Contato

    6 - Apagar Contato

    7 - Sair
    
    ''')
    return validar("Escolha a opção : ", 1,7)

while True: #Criando o loop infinito
    opcao = menu()
    if opcao == 0:
        print("Opção Invalida")
    elif opcao == 6:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar()
    elif opcao == 7:
        break