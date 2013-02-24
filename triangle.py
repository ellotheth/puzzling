class Trinode(object):

    def __init__(self, value):
        self.val = int(value)
        self.sum = 0

    def __lt__(self, other):
        return self.sum < other.sum
        
    def setsum(self, parent):
        sum = parent.sum + self.val
        if sum > self.sum: self.sum = sum

if __name__ == '__main__':
    raw = [list(map(Trinode, line.strip().split())) for line in open('triangle.txt') if line.strip()]
    
    parent = []
    for layer in raw:
        for i in range(len(parent)):
            layer[i].setsum(parent[i])
            layer[i+1].setsum(parent[i])
            
        if not parent: layer[0].sum = layer[0].val
        parent = layer
        
    print(max(parent).sum)
