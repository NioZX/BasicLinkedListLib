class NewLinkedList:

	def __init__(self,Nodes = []): #__init__ é uma função que é executada quando uma classe é chamada
		self.Nodes = Nodes #Joga o valor que passou pela função "LinkedList([1,2,3,4])" em si mesmo

	def AppendNode(self,Value): #Adiciona um nó
		self.Nodes.append(Value) #Adiciona um nó na ultima posição da lista

	def InsertNode(self,Value,Pos): #Adiciona um nó
		self.Nodes.insert(Pos,Value) #Adiciona um nó na posição desejada

	def RemoveNode(self,Value): #Remove nó
		self.Nodes.remove(Value) #Remove nó por valor

	def RemoveLastNode(self): #Remove nó
		self.Nodes.pop(self.Nodes[-1]) #Remove ultimo nó

	def PopNode(self,Pos): #Remove nó
		self.Nodes.pop(Pos) #Remove nó por index

	def Count(self,value): #Conta nós iguais
		return self.Nodes.count(value) #Retorna o tanto de vezes que o valor aparece nos nós

	def Reverse(self): #Inverte os nós
		self.Nodes.reverse() #Inverte a lista

	def ClearNodes(self): #Deleta todos os nós
		self.Nodes.clear() #Limpa a lista

	def Rotate(self,Times): #Rotaciona os nós

		output = [] #Cria uma lista para ser usada temporaria

		for time in range(0,Times): #Repete o tanto de vezes que foi pedido

			LastNode = len(self.Nodes) - 1 #Acha o ultimo nó
			for index, item in enumerate(self.Nodes): #Executa um código para cada item no "Nodes"
				if index == LastNode: #Se ele for o ultimo da lista
					output.insert(0,item) #Colocamos ele na frente
				else: #Senão
					output.append(item) #Colocamos no final da lista
			self.Nodes = output #Passamos o valor da lista temporaria para a lista real
			output = [] #Limpamos a lista temporária

	def Show(self): #Mostra os valores
		print(self.Nodes) #Coloca na tela o valor guardado em si msm

	def ShowLast(self): #Mostra o ultimo nó
		print(self.Nodes[-1]) #Pega o ultimo nó e mostra na tela

	def ShowFirst(self): #Mostra o ultimo nó
		print(self.Nodes[0]) #Pega o ultimo nó e mostra na tela

	def GetAll(self): #Pega todos os nós
		return self.Nodes #Retorna todos os nós

	def GetLast(self): #Pega o ultimo nó
		return self.Nodes[-1] #Retorna o ultimo´nó

	def GetFirst(self): #Pega o primeiro nó
		return self.Nodes[0] #Retorna o primeiro nó

	def ValueInNodes(self,Value): #Retorna True 
		if Value in self.Nodes: #Se o valor estiver nos nós
			return True #Retorna True
		return False #Retorna Falso


	def GetByIndex(self,Index): #Pega por index
		return self.Nodes[Index] #Retorna o valor por index










