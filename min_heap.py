# Course: CS261 - Data Structures
# Assignment: 5
# Student: Sullivan Lucas Myer
# Description: MinHeap implementation with time complexity limitations


# Import pre-written DynamicArray and LinkedList classes
from helper_structures import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        adds an element to the heap
        :param node:
        :return:
        """
        if self.is_empty():
            self.heap.append(node)
        else:
            self.heap.append(node)
            node_index = self.heap.length() - 1
            parent_index = (node_index-1)//2
            while self.heap.get_at_index(parent_index) > node:
                if parent_index == 0:
                    self.heap.swap(parent_index, node_index)
                    break
                self.heap.swap(parent_index, node_index)
                node_index = parent_index
                parent_index = (node_index-1)//2

        return

    def get_min(self) -> object:
        """
        returns the min value on the heap
        :return:
        """
        if self.is_empty():
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        removes the min value (root),
        replacing it while maintaining heap
        properties
        :return:
        """
        if self.is_empty():
            raise MinHeapException
        elif self.heap.length() == 1:
            return self.heap.pop()
        else:
            self.heap.swap(0, (self.heap.length()-1))
            original_root = self.heap.pop()
            parent_index = 0
            l_child_index = 2*parent_index + 1
            r_child_index = 2*parent_index + 2
            while l_child_index < self.heap.length() or r_child_index < self.heap.length():
                if l_child_index < self.heap.length() > r_child_index:
                    if self.heap.get_at_index(l_child_index) <= self.heap.get_at_index(r_child_index):
                        if self.heap.get_at_index(parent_index) > self.heap.get_at_index(l_child_index):
                            self.heap.swap(parent_index, l_child_index)
                            parent_index = l_child_index
                            l_child_index = 2 * parent_index + 1
                            r_child_index = 2 * parent_index + 2
                        else:
                            break
                    else:
                        if self.heap.get_at_index(parent_index) > self.heap.get_at_index(r_child_index):
                            self.heap.swap(parent_index, r_child_index)
                            parent_index = r_child_index
                            l_child_index = 2 * parent_index + 1
                            r_child_index = 2 * parent_index + 2
                        else:
                            break
                elif l_child_index < self.heap.length():
                    if self.heap.get_at_index(parent_index) > self.heap.get_at_index(l_child_index):
                        self.heap.swap(parent_index, l_child_index)
                        parent_index = l_child_index
                        l_child_index = 2 * parent_index + 1
                        r_child_index = 2 * parent_index + 2
                    else:
                        break
                else:
                    if self.heap.get_at_index(parent_index) > self.heap.get_at_index(r_child_index):
                        self.heap.swap(parent_index, r_child_index)
                        parent_index = r_child_index
                        l_child_index = 2 * parent_index + 1
                        r_child_index = 2 * parent_index + 2
                    else:
                        break
            return original_root

    def build_heap(self, da: DynamicArray) -> None:
        """
        creates a heap from the unsorted
        dynamic array passed as parameter
        :param da:
        :return:
        """
        self.heap = DynamicArray()
        for i in range(0, da.length()):
            self.heap.append(da.get_at_index(i))
        if self.heap.length() <= 1:
            return
        else:
            if ((self.heap.length() - 1) % 2) == 0:  # check if last element is right node
                r_child_index = self.heap.length() - 1
                l_child_index = r_child_index - 1
                parent_index = l_child_index // 2

            else:  # if last element is left node
                l_child_index = self.heap.length() - 1
                parent_index = l_child_index // 2
                if self.heap.get_at_index(parent_index) > self.heap.get_at_index(l_child_index):
                    self.heap.swap(l_child_index, parent_index)
                r_child_index = l_child_index - 1
                l_child_index = r_child_index - 1
                parent_index = l_child_index // 2
            while parent_index >= 0:
                if self.heap.get_at_index(r_child_index) <= self.heap.get_at_index(l_child_index):
                    child_index = r_child_index
                else:
                    child_index = l_child_index

                if self.heap.get_at_index(parent_index) >= self.heap.get_at_index(child_index):
                    self.heap.swap(child_index, parent_index)
                    new_p = child_index
                    new_l = new_p * 2 + 1
                    new_r = new_p * 2 + 2
                    ####
                    if new_r >= self.heap.length():
                        if new_l < self.heap.length():
                            if self.heap.get_at_index(new_p) > self.heap.get_at_index(new_l):
                                self.heap.swap(new_p, new_l)
                    else:
                        while (self.heap.get_at_index(new_p) > self.heap.get_at_index(new_l)
                                or self.heap.get_at_index(new_p) > self.heap.get_at_index(new_r)):
                            if self.heap.get_at_index(new_l) > self.heap.get_at_index(new_r):
                                self.heap.swap(new_r, new_p)
                                new_p = new_r
                            else:
                                self.heap.swap(new_l, new_p)
                                new_p = new_l
                            new_l = new_p * 2 + 1
                            new_r = new_p * 2 + 2
                            if new_r >= self.heap.length():
                                if new_l < self.heap.length():
                                    if self.heap.get_at_index(new_p) > self.heap.get_at_index(new_l):
                                        self.heap.swap(new_p, new_l)
                                        break
                                    else:
                                        break
                                else:
                                    break
                r_child_index = l_child_index - 1
                l_child_index = r_child_index - 1
                parent_index = l_child_index // 2
            return
