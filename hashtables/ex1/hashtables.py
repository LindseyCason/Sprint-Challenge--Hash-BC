

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# Hash int
def hash(x, max):
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x)

    return x % max


def hash_table_insert(hash_table, key, value):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        #While node at that index exists and the key does NOT match the key passed in
        last_pair = current_pair #Set the new last pair to the current pair...
        current_pair = last_pair.next #Set the new current pair to the pair after the last pair, this keeps going and checks again until a key is matched...

    if current_pair is not None:
        #When the key matches we move here and assign the value to the key at that index of current pair
        current_pair.value = value
    else:
        #otherwise if node is NONE, the spot is available for use so we make a new node with the linked pair k,v
        new_pair = LinkedPair(key, value)
        new_pair.next = hash_table.storage[index]
        #after making the new pair, we make the NEXT node the storage at the index above which "moves it over"
        hash_table.storage[index] = new_pair
        #Then set the storage at the index to the new pair, which will replace what we just assigned to new pair.next which was moved over..


def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = last_pair.next
        #keeps going until hits a None or a match

    if current_pair is None:
        print("ERROR: Unable to remove entry with key " + key)
    else:
        if last_pair is None:  # Removing the first element in the LL
            hash_table.storage[index] = current_pair.next
        else:
            last_pair.next = current_pair.next


def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]

    while current_pair is not None:#If there is a k,v pair in the bucket
        if(current_pair.key == key): #and the key matches
            return current_pair.value #return the value
        current_pair = current_pair.next #otherwise set current pair to the next k,v pair and try again until a match.


def hash_table_resize(hash_table):
    new_hash_table = HashTable(2 * len(hash_table.storage))
    #makes a new hashtable double the length

    current_pair = None

    for i in range(len(hash_table.storage)):#for every node in the storage range
        current_pair = hash_table.storage[i] #each node
        while current_pair is not None: #if there is a k,v in the bucket
            hash_table_insert(new_hash_table,
                              current_pair.key,
                              current_pair.value) #add current pair to the new hashtable
            current_pair = current_pair.next #set current pair to the next node and repeat until all nodes are in the new hashtable and return it.

    return new_hash_table
