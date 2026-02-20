#lista em formato Fila
from collections import deque
fila = deque()
fila.append(1)
fila.append(2)
fila.append(3)
print(fila)

#No conceito de fila o 1º elemento a entrar na lista é o 1º a sair
fila.popleft()
print(fila)