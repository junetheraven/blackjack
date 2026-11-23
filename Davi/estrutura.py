class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.itens.pop(0)
        return None

    def is_empty(self):
        return len(self.itens) == 0


class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        return None

    def is_empty(self):
        return len(self.itens) == 0

    def total(self):
        return sum(self.itens)