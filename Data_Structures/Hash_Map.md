A hash map, also known as a hash table, is a data structure that implements an associative array abstract data type, a structure that can map keys to values. It is highly efficient for lookup, insertion, and deletion operations. Here’s a more detailed explanation:

### Key Characteristics of a Hash Map:
1. **Key-Value Pair Storage**: A hash map stores data in key-value pairs. Each key is unique and is associated with a specific value.
2. **Hash Function**: It uses a hash function to compute an index (hash code) into an array of buckets or slots, from which the desired value can be found. The hash function takes a key and converts it into an integer, which is then mapped to an index in the array.
3. **Efficient Operations**: The average time complexity for search, insert, and delete operations is O(1) due to the direct index-based access to the data. However, in the worst case, operations can degrade to O(n) due to collisions.

### Collisions:
A collision occurs when two keys hash to the same index. Hash maps handle collisions using various techniques, such as:
- **Chaining**: Each array index points to a linked list (or another collection) of entries that have the same hash index.
- **Open Addressing**: When a collision occurs, the algorithm searches for the next available slot in the array (using techniques like linear probing, quadratic probing, or double hashing).

### Hash Map Operations:
- **Insertion**: Add a key-value pair to the hash map.
- **Deletion**: Remove a key-value pair from the hash map.
- **Lookup**: Retrieve the value associated with a given key.
- **Update**: Modify the value associated with a given key.

### Example in Python:
In Python, the built-in `dict` type is an implementation of a hash map. Here’s a simple example:

```python
# Creating a hash map (dictionary in Python)
hash_map = {}

# Inserting key-value pairs
hash_map['a'] = 1
hash_map['b'] = 2
hash_map['c'] = 3

# Accessing a value by key
print(hash_map['a'])  # Output: 1

# Deleting a key-value pair
del hash_map['b']

# Checking if a key exists
print('b' in hash_map)  # Output: False

# Iterating over key-value pairs
for key, value in hash_map.items():
    print(f'{key}: {value}')
# Output:
# a: 1
# c: 3
```

### Custom Implementation:
Here’s a simplified custom implementation of a hash map in Python to illustrate the concept:

```python
class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.map = [None] * size

    def _get_hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def __str__(self):
        ret = ""
        for item in self.map:
            if item is not None:
                ret += str(item) + "\n"
        return ret

# Usage
h = HashMap()
h.add('a', 1)
h.add('b', 2)
h.add('c', 3)
print(h.get('a'))  # Output: 1
print(h.get('b'))  # Output: 2
print(h.get('c'))  # Output: 3
h.delete('a')
print(h.get('a'))  # Output: None
print(h)
```

This custom `HashMap` class demonstrates the basic principles of how a hash map works, including hashing, collision handling via chaining, and basic operations like insertion, retrieval, and deletion.

A hash map achieves O(1) average time complexity for search, insert, and delete operations primarily due to the way it uses a hash function to index its entries. Here's a detailed explanation of how this works:

### Hash Function:
1. **Hashing**:
   - The hash function takes a key and computes an integer hash value. This hash value is then reduced using modulo operation with the size of the hash table to ensure it maps to a valid index within the bounds of the array.
   - Example: `index = hash(key) % size`

2. **Direct Indexing**:
   - The result of the hash function is an index that directly corresponds to the position in the array (bucket) where the key-value pair should be stored or retrieved.
   - This allows the hash map to perform insertions and lookups in constant time, O(1), on average because it involves a simple array indexing operation.

### Collisions:
Collisions occur when two different keys hash to the same index. Hash maps handle collisions using various methods, primarily:

1. **Chaining**:
   - Each bucket (array index) contains a linked list or another secondary structure to hold all entries that hash to the same index.
   - When inserting, if a collision occurs, the new key-value pair is appended to the list at that index.
   - When searching, the list at the indexed bucket is traversed to find the key.

2. **Open Addressing**:
   - Instead of storing multiple items at a single index, open addressing searches for the next available bucket.
   - This can be done using linear probing, quadratic probing, or double hashing to resolve collisions.

### Average Case Efficiency:
- **Uniform Distribution**:
  - A good hash function distributes keys uniformly across the hash table, minimizing collisions and keeping the linked lists (in chaining) or the sequence of probes (in open addressing) short.
  - This ensures that most operations (insert, search, delete) can be done in constant time, O(1), on average.

- **Load Factor**:
  - The load factor, defined as the number of elements divided by the number of buckets, impacts performance.
  - Hash maps typically resize (rehash) when the load factor exceeds a certain threshold, keeping the average complexity of operations at O(1).

### Worst Case Efficiency:
- **High Collisions**:
  - In the worst-case scenario, where many keys hash to the same index, operations degrade to O(n) complexity.
  - This would result in traversing a long linked list (in chaining) or probing many times (in open addressing).

### Example:
Here's an example demonstrating how a hash map achieves O(1) average complexity:

```python
class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.map = [None] * size

    def _get_hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def __str__(self):
        ret = ""
        for item in self.map:
            if item is not None:
                ret += str(item) + "\n"
        return ret

# Example usage
h = HashMap()
h.add('a', 1)
h.add('b', 2)
h.add('c', 3)
print(h.get('a'))  # Output: 1
print(h.get('b'))  # Output: 2
print(h.get('c'))  # Output: 3
h.delete('a')
print(h.get('a'))  # Output: None
print(h)
```

In this example:
- **Hash Function**: `_get_hash` computes an index from the key.
- **Insert**: `add` places the key-value pair directly into the array or appends it to the list at the computed index.
- **Search**: `get` retrieves the value by computing the index and traversing the list at that index, if necessary.

By ensuring uniform distribution and maintaining a low load factor, hash maps can provide O(1) average time complexity for most operations.
