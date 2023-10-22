class HashableObjects:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    @staticmethod
    def __print__():
        print('Object created successfully!')


if __name__ == '__main__':
    print(hash(45))
    print(hash('Hello!'))
    print(hash(45))

    hashable_obj = HashableObjects(45)
    hashable_obj.__print__()

    # the following code snippet throws an error because list is not hashable
    # dict = {
    #     [1, 2, 3]: 1,
    # }

    print(hash(hashable_obj))

