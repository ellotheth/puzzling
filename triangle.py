class Trinode(object):
    
    sum = 0
    
    def __init__(self, value):
        self.val = int(value)
        self.left = None
        self.right = None
        
    def __repr__(self):
        return str(self.val) + ': ' + str(self.sum)
        
    def __lt__(self, other):
        return self.sum < other.sum
        
    def setsum(self, parent):
        sum = parent.sum + self.val
        if sum > self.sum: self.sum = sum

if __name__ == '__main__':

    input = """
            5
          9  6
        4   6  8
     500  7  1   501
    """
    
    raw = [list(map(Trinode, line.strip().split())) for line in input.split('\n') if line.strip()]
    print(raw)
    
    prev = []
    for layer in raw:
        for i in range(len(prev)):
            layer[i].setsum(prev[i])
            layer[i+1].setsum(prev[i])
            
        if not prev: layer[0].sum = layer[0].val
        prev = layer
        
    print(max(prev))