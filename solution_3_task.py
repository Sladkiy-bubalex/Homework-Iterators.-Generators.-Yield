class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.result = []
        self.flatten(list_of_list)
        
    def flatten(self, list_):        
        def recursion(list_):
            if type(list_) is list:
                for item in list_:
                    if type(item) is list:
                        recursion(item)
                    else:
                        self.result.append(item)
            else:
                self.result.append(item)
 
        recursion(list_)
 
        return self.result

    def __iter__(self):
        self.cursor = -1
        return self
    
    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.result):
            raise StopIteration
        return self.result[self.cursor]




def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()