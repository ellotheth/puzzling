"""
Triangle puzzle: Top-down!
Author: ellotheth
Date: 2013.02.23

Developed in Python 3.3, but probably works in any Python 3 flavor.
"""

# this whole class could be replaced by a two-element list, but this is
# prettier
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

    # one-liner for brevity; since this is top-down, you could reduce memory
    # usage by processing one line at a time instead of reading the entire file
    # into memory at once
    raw = [list(map(Trinode, line.strip().split())) for line in open('triangle.txt') if line.strip()]
    
    parent = []
    for layer in raw:
        for i in range(len(parent)):
            layer[i].setsum(parent[i])
            layer[i+1].setsum(parent[i])
            
        if not parent: layer[0].sum = layer[0].val # special case for the apex
        parent = layer
        
    print(max(parent).sum)
