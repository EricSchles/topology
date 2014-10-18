from itertools import chain, combinations

class Topology:
    def __init__(self,data=[]):
        self.data = data
        self.topology = self._powerset()

    def _topologize(self,data):
        pass
    
    def singleton(self):
        return [[elem] for elem in self.data]

    #expects singleton data
    def _powerset(self):
        i = self.data
        result = []
        for z in chain.from_iterable(combinations(i,r) for r in range(len(i)+1)):
            result.append(z)
        return result
    
    def intersection(self,set1,set2):
        return [filter(lambda x: x in set1, sublist) for sublist in set2]

    def union(self,set1,set2):
        return [set1+set2]

    def remove_duplicates(self):
        for ind,val in enumerate(self.data):
            if val in data:
                data[ind] = None
        final = []
        for val in data:
            if val:
                final.append(val)

        return val

    
    
