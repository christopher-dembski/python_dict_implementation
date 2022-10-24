from linked_list import LinkedList


class HashMap:

    def __init__(self, size=8):
        self.buckets = [None for _ in range(size)]

    def __setitem__(self, key, value):
        index = hash(key) % len(self.buckets)
        if self.buckets[index] is None:
            self.buckets[index] = LinkedList()
        self.buckets[index].add((key, value))

    def __getitem__(self, key, default=None):
        index = hash(key) % len(self.buckets)
        if self.buckets[index] is None:
            return default
        for bucket_key, bucket_value in self.buckets[index]:
            if key == bucket_key:
                return bucket_value
        return default

    def __repr__(self):
        result = 'Dict([\n\t'
        result += ',\n\t'.join(str(bucket) for bucket in self.buckets)
        result += '\n])'
        return result


# # # Testing # # #

if __name__ == '__main__':

    hash_map = HashMap()

    characters = (('Michael', 'Scott'),
                  ('Jim', 'Halpert'),
                  ('Pam', 'Beesly'),
                  ('Dwight', 'Schrute'))
    for first_name, last_name in characters:
        hash_map[first_name] = last_name

    print(hash_map)

    print(hash_map['Jim'])
