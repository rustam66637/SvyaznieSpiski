class Node:
    def __init__(self, v = None, n = None):
        self.value = v
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item): #добавление нового узла в конец списка
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self): #метод отладочного вывода списка
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val): #найти нужный узел по заданному значению
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val): #метод поиска всех узлов по конкретному значению
        node = self.head
        i = 0
        s = []
        while node is not None:
            if node.value == val:
                s.append(node)
            node = node.next
            i += 1
        return s

    def delete(self, val, all=False): #метод удаления одного узла по его значению
        node = self.head
        old = self.head
        while node != None:
            if node.value == val:
                if node == self.head and node == self.tail and node.value == val:
                    self.head = self.tail = None
                if node == self.head:
                    self.head = node.next
                if node == self.tail:
                    self.tail = old
                old.next = node.next
                if all == False:
                    return
            else:
                old = node
            node = node.next

    def clean(self): #метод очистки всего содержимого
        self.__init__()

    def len(self): #метод вычисления длины списка
        node = self.head
        s = 0
        while node != None:
            s += 1
            node = node.next
        return s

    def insert(self, afterNode, newNode): #метод вставки узла после заданного узла
        if afterNode == None and self.head == None and self.tail == None:
            if type(newNode) == Node:
                LinkedList.add_in_tail(self, newNode) # проверка на пустой список
            if type(newNode) == int:
                self.tail = self.head = Node(newNode)
            return
        node = self.head
        while True:
            if type(newNode) == Node:
                LinkedList.add_in_tail(self, newNode)
                return
            if type(newNode) == int and type(afterNode) == Node:
                if node.value == afterNode.value:
                    node.next = Node(newNode, node.next)
                    if node.next.next == None:
                        self.tail = node.next
                    break
                else: node = node.next
            if type(newNode) == int and type(afterNode) == int:
                if node.value == afterNode:
                    node.next = Node(newNode, node.next)
                    if node.next.next == None:
                        self.tail = node.next
                    break
                else: node = node.next

    def func(s, d): #функция, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков
        if s.len() == d.len():
            node1 = s.head
            node2 = d.head
            s = []
            while node1 != None:
                s.append(node1.value + node2.value)
                node1 = node1.next
                node2 = node2.next
            return s
