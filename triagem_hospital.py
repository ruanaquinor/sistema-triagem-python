
# Cria a lista com o nodo cor e numero
class ElementoDaListaSimples:
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None

    def __repr__(self):
        return f'[{self.cor}, {self.numero}]'

# Cria a lista encadeada simples
class ListaEncadeadaSimples:

    # Cria o self.senha_v para a numeração do cartão Verde
    # Cria o self.senha_a para a numeração do cartão Amarelo
    def __init__(self):
        self.head = None
        self.senha_v = 1
        self.senha_a = 201

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(str(nodo))
            nodo = nodo.proximo
        return "Lista -> " + " ".join(nodos)

    # Varre a lista
    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    # Inserir o cartão Verde(V)
    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo

    # Inserir o cartão Amarelo(A)
    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return

        if self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo != None and nodo_atual.proximo.cor == 'A':
            nodo_atual = nodo_atual.proximo

        nodo.proximo = nodo_atual.proximo
        nodo_atual.proximo = nodo

    # Inserir os dados dos cartões(A/V)
    def inserir(self):
        cor = input('Informe a cor do cartão (A/V): ')
        if cor == 'V':
            numero = self.senha_v
            self.senha_v += 1
        elif cor == 'A':
            numero = self.senha_a
            self.senha_a += 1
        else:
            print('Dado inválido!')
            return

        novo_nodo = ElementoDaListaSimples(cor, numero)

        if self.head is None:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)

    # Mostrar os pacientes da fila
    def imprimirListaEspera(self):
        if self.head is None:
            print('Lista Vazia')
        else:
            print(self)

    # Chamar o paciente
    def atenderPaciente(self):
        if self.head is None:
            print('Nenhum paciente na fila.')
            return
        paciente = self.head
        self.head = self.head.proximo
        print(f'Atendendo o paciente cartão cor {paciente.cor} e número {paciente.numero}')


# Programa principal
DadoPaciente = ListaEncadeadaSimples()

while True:
    print('1 - Adicionar paciente a fila')
    print('2 - Mostrar pacientes na fila')
    print('3 - Chamar paciente')
    print('4 - Sair')
    op = int(input('Escolha uma opção:'))
    if op == 1:
        DadoPaciente.inserir()

    elif op == 2:
        DadoPaciente.imprimirListaEspera()

    elif op == 3:
        DadoPaciente.atenderPaciente()

    elif op == 4:
        print('Encerrando...')
        break
    else:
        print('Selecione outra opção!\n')
