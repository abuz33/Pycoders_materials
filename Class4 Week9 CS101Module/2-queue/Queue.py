from LinkedList import LinkedList


class Queue:
    def __init__(self) -> None:
        self.__list = LinkedList()

    def size(self):
        return self.__list.size()

    def is_empty(self):
        return self.__list.is_empty()

    def enqueue(self, value):
        self.__list.add(value)

    def dequeue(self):
        return self.__list.remove_first()

    def peek(self):
        return self.__list.peek_first()


q = Queue()

q.enqueue(1)
print(q.is_empty())
