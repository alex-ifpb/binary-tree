<h1 align="center">Estruturas de Dados Hierárquicas Orientada a Objetos</h1>

Este repositório reúne diferente implementações na Linguagem `Python` de Árvores Binárias utilizando a técnica <b>encadeada</b>. As estrurutas de dados são estudadas, discutidas e implementadas nos cursos de Sistemas para Internet e Redes de Computadores do IFPB Campus João Pessoa.

Contribua com o aprimoramento do código enviando as suas sugestões ou indicando situações em que houve falha funcional da estrutura de dados.

## Autor
Professor Alex Sandro da Cunha Rêgo
Lattes: http://lattes.cnpq.br/1582109846489096 
E-mail: alex@ifpb.edu.br
Doutor em Ciência da Computação

## Pré-Requisitos
+  Conhecimentos básicos na sintaxe de programação na linguagem Python
+  Entendimento de conceitos de Classes e Objetos (POO)
+  Conhecimento sobre árvores binárias 

## Características
Os seguintes métodos especiais estão presentes nas classes:

`__contains__()`: permite verificar se uma chave está contida em uma determinada coleção, usando o operador `in`. Neste caso, o operando usado em conjunto do operador `in` deve ser algo em que se deseja verificar se está na lista de elementos. Exemplo:
```
if key in minha_arvore:
      pass
```

`__iter__()`: Método mágico que permite iterar os elementos da árvore binária, usando como padrão o percurso em "pre-ordem". Exemplo:
```
for item in minha_arvore:
      print(item)
```


## Estruturas de Dados
| Nome | Descrição |
| ------ | ----------- |
| Árvore Binária com Cursor (`BTCursor`) | Árvore binária com `cursor`, ou seja, um apontador interno que determina em qual nó serão realizadas as operações de inserção e remoção na árvore. O `cursor` pode ser deslocado utilizando os métodos específicos de deslocamento à esquerda ou direita. Porém, não permite voltar para o nó `pai`. |
| Árvore Binária com link para o nó Pai (`BTParent`) | Árvore binária  em que a estrutura de um nó dispõe de acesso aos nós  `esquerdo`,  `direito` e `pai`. Ainda necessita de um `cursor`, porém, permite retornar ao nó `pai`.  |
| Árvore Binária de Busca (`BST`) | Implementação de uma Árvore Binária de Busca (_Binary Search Tree_ - BST)  |
| Árvore AVL (`AVLTree`) | Implementação de uma Árvore Binária de Busca Balanceada AVL (Adelson Velsky e Landis)  |

## Métodos

A tabela a seguir ilustra os métodos em comum nas diferentes implementações de árvores binárias. Maiores detalhes sobre cada método
podem ser conferidos na documentação do código.

| Implementação    | BST | AVL  | BTCursor | BTParent |
| ---------------- |---- | ---- | ---------| -------- |
| getRoot()        | X   |  X   |  X       |   X  |
| getCursor()      | N/A |  N/A |  X       |   X  |
| resetCursor()    | N/A |  N/A |  X       |   X  |
| createRoot()     | N/A |  N/A |  X       |   X  |
| downLeft()       | N/A |  N/A |  X       |   X  |
| downRight()      | N/A |  N/A |  X       |   X  |
| back()           | N/A |  N/A |  N/A     |   X  |
| addLeftChild()   | N/A |  N/A |  X       |   X  |
| addRightChild()  | N/A |  N/A |  X       |   X  |
| isEmpty()        | X   |  X   |  X       |   X  |
| height()         | X   |  X   |  X       |   X  |
| add()            | X   |  X   |  N/A     |  N/A |
| search()         | X   |  X   |  X       |   X  |
| traversal()      | X   |  X   |  X       |   X  |
| clear()          | X   |  X   |  X       |   X  |
| deleteNode()     | X   |  X   |  X       |   X  |
| treeView()       | X   |  X   |  X       |   X  |
| build()          | X   |  X   |  X       |  N/A |
| balance()        | X   |  N/A |  N/A     |  N/A |    
| `__str__()`      | X   |  X   |  X       |   X  |
| `__len__()`      | X   |  X   |  X       |   X  |
| `__iter__()`     | X   |  X   |  X       |   X  | 
| `__next__()`     | X   |  X   |  X       |   X  | 
| `__contains__()` | X   |  X   |  X       |   X  |

N/A: Não se aplica