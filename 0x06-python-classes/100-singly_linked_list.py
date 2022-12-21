#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """Node class defines a node of a singly linked list"""

    # constructor
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    # Private instance attribute: data
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    # Private instance attribute: next_node
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def nextnode(self, value):
        self.next_node(value)


class SinglyLinkedList:
    """singly linked list class"""

    def __init__(self):
        self.__head = None

    def sortedinsert(self, value):
        self.sorted_insert(value)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head == None:
            self.__head = new_node
        elif self.__head.next_node == None:
            if value < self.__head.data:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                self.__head.next_node = new_node
        else:
            temp = self.__head
            if value < self.__head.data:
                new_node.next_node = self.__head
                self.__head = new_node
                return
            while temp != None:
                if temp.next_node == None:
                    temp.next_node = new_node
                    break
                elif temp.next_node.data >= value:
                    new_node.next_node = temp.next_node
                    temp.next_node = new_node
                    break
                temp = temp.next_node

    # print result
    def __str__(self):
        """print result SinglyLinkedList."""
        values = ""
        while self.__head != None:
            values += str(self.__head.data)
            self.__head = self.__head.next_node
            if self.__head != None:
                values += "\n"
        return values
