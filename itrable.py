
class Range:
    def __init__(self, start, stop, step):
        self.start = start 
        self.stop = stop
        self.step = step


    def __iter__(self):

        return RangeIterator(self)
 


class RangeIterator:

    def __init__(self, range):
        self.range = range


    def __next__(self):
        if self.range.start > self.range.stop:
            raise StopIteration
        result = self.range.start 
        self.range.start = self.range.start + self.range.step 
        return result

    def __iter__(self):
        return self




r = Range(1, 7, 3)
for item in r:
    print(item)


