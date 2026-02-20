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

#Instanciação (p1 = Pessoa(...)): É o ato de criar o objeto real a partir do molde.
p1 = Pessoa("Irlan",34,"1.85") 
p2 = Pessoa("Vanessa",33,"1.72") 
# No Python, decimais usam PONTO. Se precisar mostrar com vírgula depois, você formata na saída: print(f"{self.altura:.2f}".replace('.', ','))

p1.apresentar()
p2.apresentar()

p1.set__idade(40) # Determina que a idade só pode ser alterada abaixo de 40 anos. 
p1.apresentar()

print(p1.get__nome())# Nova forma de printar a variavél nome, antes encapsulada.