#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """Node class defines a node of a singly linked list"""

    # constructor
    def __init__(self, data, nextnode=None):
        self.__data = data
        self.__nextnode = nextnode

    # Private instance attribute: data
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    # Private instance attribute: nextnode
    @property
    def nextnode(self):
        return self.__nextnode

    @nextnode.setter
    def nextnode(self, value):
        if value != None and type(value) is not Node:
            raise TypeError("nextnode must be a Node object")
        self.__nextnode = value


class SinglyLinkedList:
    """singly linked list class"""

    def __init__(self):
        self.__head = None

    def sortedinsert(self, value):
        new_node = Node(value)
        if self.__head == None:
            self.__head = new_node
        elif self.__head.nextnode == None:
            if value < self.__head.data:
                new_node.nextnode = self.__head
                self.__head = new_node
            else:
                self.__head.nextnode = new_node
        else:
            temp = self.__head
            if value < self.__head.data:
                new_node.nextnode = self.__head
                self.__head = new_node
                return
            while temp != None:
                if temp.nextnode == None:
                    temp.nextnode = new_node
                    break
                elif temp.nextnode.data >= value:
                    new_node.nextnode = temp.nextnode
                    temp.nextnode = new_node
                    break
                temp = temp.nextnode

    # print result
    def __str__(self):
        """print result SinglyLinkedList."""
        values = ""
        while self.__head != None:
            values += str(self.__head.data)
            self.__head = self.__head.nextnode
            if self.__head != None:
                values += "\n"
        return values
