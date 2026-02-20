class Pessoa: #A (class Pessoa): é como uma fôrma de bolo. Ela define o formato, mas não é o bolo em si.
    def __init__(self,nome,idade, altura): #O Construtor (def __init__): É o como se fosse receita de bolo. Ele recebe os ingredientes (nome, idade, altura) e os guarda.
        self.nome = nome    
        self.idade = idade #O self. é a forma de o objeto dizer "isso pertence a mim". Sem ele, o Python não saberia se a idade é do Irlan ou da Vanessa.
        self.altura = altura

    def apresentar(self):
        # O f (f-strings) antes das aspas permite colocar variáveis dentro de chaves {}, deixam o código muito mais limpo e fácil de ler. 
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e meço {self.altura}m.")

#Instanciação (p1 = Pessoa(...)): É o ato de criar o objeto real a partir do molde.
p1 = Pessoa("Irlan",34,"1.85") # Se precisar mostrar com vírgula depois, você formata na saída:
p2 = Pessoa("Vanessa",33,"1.72") # print(f"{self.altura:.2f}".replace('.', ','))
# No Python, decimais usam PONTO

p1.apresentar()
p2.apresentar()