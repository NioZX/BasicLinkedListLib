**LinkedListLib** _Versão: **1.0**_

**Autor: _Nio.pyx#9066_**

**Funções:**
	
**AppendNode(_valor_):** _Adiciona um nó no final dos nós_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList()
L.AppendNode(5)
L.Show() #-> [5]
```

**InsertNode(_valor, posição_):** _Adiciona um nó na posição desejada_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList()
L.InsertNode(5,2)
L.InsertNode(1,1)
L.Show() #-> [1,5]
```

**RemoveNode(_valor, posição_):** _Adiciona um nó no final dos nós_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList()
L.InsertNode(5,2)
L.InsertNode(1,1)
L.Show() #-> [5, 1]
L.RemoveNode(5)
L.Show() #-> [1]
```

**RemoveLastNode(_valor_):** _Remove o ultimo nó dos nós_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList()
L.InsertNode(5,2)
L.InsertNode(1,1)
L.Show() #-> [5, 1]
L.RemoveLastNode()
L.Show() #-> [5]
```

**PopNode(_posição_):** _Remove o nó na posição desejada_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList([1,2,3,4,5])
L.Show() #-> [1, 2, 3, 4, 5]
L.PopNode(3)
L.Show() #-> [1, 2, 3, 5]
```

**Count(_valor_):** _Conta nós iguais_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList([1,2,2,4,5])
print(L.Count(2)) #-> 2
```
**ClearNodes():** _Limpa todos os nós_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList([1,2,2,4,5])
L.Show() #-> [1, 2, 2, 4, 5]
L.ClearNodes()
L.Show() #-> []
```

**Rotate(_vezes_):** _Rotaciona os nós_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList([1,2,2,4,5])
L.Show() #-> [1, 2, 2, 4, 5]
L.Rotate(2)
L.Show() #-> [4, 5, 1, 2, 2]
```

**Show():** _Mostra na tela todos os nós_

**ShowLast():** _Mostra na tela o ultimo nó_

**ShowFirst():** _Mostra na tela o primeiro nó_

**GetAll():** _Retorna uma lista com todos os nós_

**GetLast():** _Retorna o ultimo nó_

**GetFirst():** _Retorna o primeiro nó_

**ValueInNodes(_valor_):** _Retorna verdadeiro se o valor está nos nós_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList([1,2,2,4,5])
print(L.ValueInNodes(4)) #-> True
print(L.ValueInNodes(7)) #-> False
```

**GetByIndex(_posição_):** _Retorna um nó por posição_

```py
import LinkedListLib

L = LinkedListLib.NewLinkedList([1,2,2,4,5])
print(L.GetByIndex(2)) #-> 2
```



