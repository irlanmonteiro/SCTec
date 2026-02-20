class Pessoa: #A (class Pessoa): é como uma fôrma de bolo. Ela define o formato, mas não é o bolo em si.
    def __init__(self,nome,idade, altura): #O Construtor (def __init__): É o como se fosse receita de bolo. Ele recebe os ingredientes (nome, idade, altura) e os guarda.
        #O self. é a forma de o objeto dizer "isso pertence a mim". Sem ele, o Python não saberia se a idade é do Irlan ou da Vanessa.
        self.__nome = nome  # O duplo Undeline (__nome) é usado para encapsular o elemento nome e proteger os dados. 
        self.__idade = idade 
        self.altura = altura

    def apresentar(self):
        # O f (f-strings) antes das aspas permite colocar variáveis dentro de chaves {}, deixam o código muito mais limpo e fácil de ler. 
        print(f"Olá, meu nome é {self.__nome}, tenho {self.__idade} anos e meço {self.altura}m.")

    def get__nome(self): #Função para acessar a variavél nome que foi encapsulada.
        return self.__nome
    
    def set__idade(self, nova_idade):#Funçao para alterar a idade abaixo de 40 anos.
        if nova_idade <40:
            self.__idade = nova_idade

class Aluno(Pessoa): #Conceito de Herança: Aluno Herda os atributos da classe Pessoa
    def __init__(self, nome, idade, altura, matricula):
        super().__init__(nome, idade, altura)
        self.matricula = matricula

    def estudante(self):
        print('A matricula do aluno é', self.matricula)

    def apresentar(self): # Conceito de polimorfismo
        print('Olá, meu nome é:',super().get__nome(),'e minha matricula é' ,self.matricula)

aluno1 = Aluno('Pedro', 30,'1.90', '000678908')

aluno1.estudante()
aluno1.apresentar()