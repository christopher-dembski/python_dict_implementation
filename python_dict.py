class Dict:

    def __init__(self, size=8):
        self.indices = [None for _ in range(size)]
        self.keys = []
        self.values = []

    def __setitem__(self, key, value):
        indices_index = hash(key) % len(self.indices)
        key_value_index = self.indices[indices_index]
        if key_value_index is None:
            self.indices[indices_index] = len(self.keys)
        else:
            raise ValueError('Collision.')
        self.keys.append(key)
        self.values.append(value)

    def __getitem__(self, item, default=None):
        indices_index = hash(item) % len(self.indices)
        key_value_index = self.indices[indices_index]
        if key_value_index is None:
            return default
        return self.values[key_value_index]

    def __repr__(self):
        return f'Dict(indices={self.indices}, keys={self.keys}, values={self.values})'


# # # Testing # # #

d = Dict()

d['Michael'] = 'Scott'
print(d)

d['Jim'] = 'Halpert'
print(d)

d['Pam'] = 'Beesly'
print(d)

print(d['Michael'])
print(d['Jim'])
print(d['Cece'])
print(d['Pam'])
