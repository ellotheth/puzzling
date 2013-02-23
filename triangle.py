class Trinode(object):
    
    def __init__(self, value):
        self.val = int(value)
        self.left = None
        self.right = None
        
    def __repr__(self):
        return str(self.val)
    
def trisum(node):
    if node.left and node.right:
        left, right = node.val + trisum(node.left), node.val + trisum(node.right)
        val = left if left > right else right
    else: val = node.val
    
    return val

if __name__ == '__main__':

    input =
"""
        5
      9  6
    4   6  8
  0   7  1   5
"""
    
    raw = [list(map(Trinode, line.strip().split())) for line in input.split('\n') if line.strip()]
    print(raw)
    
    apex = None
    prev = []
    for layer in raw:
        for i in range(len(prev)):
            prev[i].left = layer[i]
            prev[i].right = layer[i + 1]
        prev = layer
        if not apex: apex = prev[0]
        
    print(trisum(apex))