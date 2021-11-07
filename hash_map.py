# Course: CS261 - Data Structures
# Assignment: 5
# Student: Sullivan L Myer
# Description: Hashtable with constrained data structure and time-complexity


# Import pre-written DynamicArray and LinkedList classes
from helper_structures import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        clears the current hash table,
        updating size to 0 but
        leaving capacity unchanged
        :return:
        """
        self.buckets = DynamicArray()
        for bucket in range(0, self.capacity):
            self.buckets.append(LinkedList())
        self.size = 0

    def get(self, key: str) -> object:
        """
        returns either the value associated with the
        key passed as parameter, or None if key
        does not currently exist in the hash table
        :param key:
        :return: None or value at key
        """
        if self.contains_key(key):
            return self.buckets.get_at_index(self.hash_function(key) % self.capacity).contains(key).value
        else:
            return None

    def put(self, key: str, value: object) -> None:
        """
        updates the key:value pair in the HashMap,
        adding a key if one does not exist
        :param key: key
        :param value: value
        :return:
        """

        if self.contains_key(key):
            cur_node = self.buckets.get_at_index(self.hash_function(key) % self.capacity).contains(key)
            cur_node.value = value
        else:
            self.size += 1
            self.buckets.get_at_index(self.hash_function(key) % self.capacity).insert(key, value)

    def remove(self, key: str) -> None:
        """
        removes the key passed as parameter,
        and its associated value from the HashMap.
        if key is absent, method does not raise exception
        :param key:
        :return:
        """
        pass
        if self.contains_key(key):
            self.buckets.get_at_index(self.hash_function(key) % self.capacity).remove(key)
            self.size -= 1
        return

    def contains_key(self, key: str) -> bool:
        """
        returns True if the hashmap contains
        the key passed as parameter, False otherwise
        :param key:
        :return:
        """
        for bucket in range(0, self.capacity):
            if self.buckets.get_at_index(bucket).contains(key) is not None:
                return True
        return False

    def empty_buckets(self) -> int:
        """
        returns number of empty buckets
        :return: int representing number of empty buckets
        """
        empties = 0
        for bucket in range(0, self.capacity):
            if self.buckets.get_at_index(bucket).length() == 0:
                empties += 1
        return empties

    def table_load(self) -> float:
        """
        returns lambda (i.e. nodes divided by buckets)
        :return: lambda
        """
        total_nodes = 0
        for bucket in range(0, self.buckets.length()):
            contents = self.buckets.get_at_index(bucket)
            total_nodes += contents.length()
        return total_nodes/self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        changes the capacity of the internal has table,
        preserving all key value pairs, but rehashing
        all links, if new_capacity is 0, do nothing
        :param new_capacity:
        :return:
        """

        if new_capacity >= 1:
            old_size = self.size
            new_buckets = DynamicArray()
            for bucket in range(0, new_capacity):
                new_buckets.append(LinkedList())
            for bucket in range(0, self.capacity):
                for node in self.buckets.get_at_index(bucket):
                    new_buckets.get_at_index(self.hash_function(node.key) % new_capacity).insert(node.key, node.value)
            self.clear()
            self.size = old_size
            self.capacity = new_capacity
            self.buckets = new_buckets
            return
        else:
            return

    def get_keys(self) -> DynamicArray:
        """
        returns a dynamic array that contains all
        keys stored in the HashMap. order is irrelevant
        :return: dynamic array containing all unique keys
        """
        map_keys = DynamicArray()
        for bucket in range(0, self.capacity):
            for node in self.buckets.get_at_index(bucket):
                map_keys.append(node.key)
        return map_keys
