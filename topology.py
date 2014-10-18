class Topology:
    def __init__(self,data=[]):
        self.data = data
        self.topology = self._topologize(self.data)

    def _topologize(self,data):
        pass
    
    def singleton(self,data):
        return [[elem] for elem in data]

    #expects singleton data
    def subset(self,data):
        subsets = []
        subsets.append(data)
        for ind,val in enumerate(data[1:]):
            for index,value in data:
                tmp = []
                for i in xrange(ind):
                    tmp += data[index+i]
                subsets.append(value+tmp)
        return subsets
            
    
    
    def intersection(self,set1,set2):
        return [filter(lambda x: x in set1, sublist) for sublist in set2]

    def union(self,set1,set2):
        return [set1+set2]

    def remove_duplicates(self,data):
        for ind,val in enumerate(data):
            if val in data:
                data[ind] = None
        final = []
        for val in data:
            if val:
                final.append(val)

        return val

    
    
