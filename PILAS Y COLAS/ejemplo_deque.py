from collections import deque
#se puede inicializar con deque una lista
numbers=deque()
#utiliza append para ingresar valores
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)
#se puede hacer pop
last_item=numbers.pop()
print(last_item) # 47
print(numbers) # deque([99,15,82,50)]
# ofuncionar como cola
first_item=numbers.popleft()
print(first_item) # 99
print(numbers) #deque([15,82,50)]