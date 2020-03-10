# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def lookup_chain(self, key):
        if self.key == key:
            return self
        elif self.next is None:
            return None
        else:
            return self.next.lookup_chain(key)


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # Initialize hash with value 5381
        # For each char, multiply the hash by 33 and add the interger value of the char

        h = 5381
        for c in key:
            h = (h * 33) + ord(c)
        return h


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        hashed_key = self._hash_mod(key)
        current_val = self.storage[hashed_key]
        self.storage[hashed_key] = LinkedPair(key, value)
        self.storage[hashed_key].next = current_val



    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        hashed_key = self._hash_mod(key)
        current_val = self.storage[hashed_key]
        if current_val is None:
            print("Key not found")
            return None
        else:
            node = current_val
            prev = None
            while node is not None:
                if node.key == key:
                    if prev is not None:
                        prev.next = node.next
                    else:
                        self.storage[hashed_key] = node.next
                    return
                node = node.next
                prev = node
            print("Key not found")
            return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        hashed_key = self._hash_mod(key)
        current_val = self.storage[hashed_key]
        if current_val is None:
            return None
        else:
            value = current_val.lookup_chain(key).value
            return value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.capacity *= 2
        store = self.storage[:]
        self.storage = [None] * self.capacity
        for bucket in store:
            node = bucket
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next

  

 
if  __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
