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
    
    prev = []
    for layer in raw:
        for i in range(len(prev)):
            layer[i].setsum(prev[i])
            layer[i+1].setsum(prev[i])
            
        if not prev: layer[0].sum = layer[0].val
        prev = layer
        
    print(max(prev).sum)
