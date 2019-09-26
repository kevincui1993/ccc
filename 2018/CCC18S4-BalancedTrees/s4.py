"""
This code serves as a template that captures the main algorithim. 
To pass the online judge, you may need to covnert it to C++
"""

import sys
import collections

mem = collections.Counter()

def dfs(current_weight):
    global mem
    if current_weight <= 2:
        return 1
        
    #check if it's already cached
    if current_weight in mem:
        return mem[current_weight]
    res = 0
    
    """
    Start to check from the middle as everything greater than it will result 
    in a subtree of weight 1
    """
    start = current_weight // 2
    while True:
        count = current_weight // start

        #count the number of time this weight has appeared
        res  += dfs(start) * (count - current_weight // (start+1)) 
        if start == 1: break
        
        #skip to the next index that result in different weight
        start = (current_weight) // (count+1)
    mem[current_weight] = res
    return res
    
weight = int(sys.stdin.readline())
res = dfs(weight)
print(res)