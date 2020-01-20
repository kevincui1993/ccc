import time

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.maxNutrient = []

root = Node(0)
res = ''

def buildTree():
    nutrientInput = input()[1:-1]
    stack = [root]

    i = 0
    while i < len(nutrientInput):
        while i < len(nutrientInput) and nutrientInput[i] == ' ':
            i+=1
        start = i
        if i >= len(nutrientInput):
            break
        if nutrientInput[start] not in "()":
            while i+1 < len(nutrientInput) and nutrientInput[i+1] not in "( )":
                i+=1
        if nutrientInput[start] != ')':
            if stack[-1].left == None:
                stack[-1].left = Node(-1)
                stack.append(stack[-1].left)
            else:
                stack[-1].right = Node(-1)
                stack.append(stack[-1].right)
            if nutrientInput[start] != '(':
                value = int(nutrientInput[start:i+1])
                if stack[-1].left != None:
                    stack[-1].right = Node(-1)
                    stack.append(stack[-1].right)
                stack[-1].val = value
                stack.pop()
        else:
            stack.pop()
        i+=1

def verifyTree(node):
    global res
    if node:
        if node.val != -1:
            res = res + str(node.val) + ' ' 
        if node.left == None and node.right == None:
            return
        res += '('
        verifyTree(node.left)
        res += ' '
        verifyTree(node.right)
        res += ')'
        
def dp(node):
    X = int(input()) + 1
    level = []
    bfs = [node]
    while bfs:
        size = len(bfs)
        for i in range(size):
            if bfs[i].left:bfs.append(bfs[i].left)
            if bfs[i].right: bfs.append(bfs[i].right)
        level.insert(0, bfs[:size])
        bfs = bfs[size:]
    
    preprocessTime = 0
    mainprocessTime = 0
    for i in range(len(level)):
        for j in range(len(level[i])):
            #print("i: " + str(i))
            #print("j: " + str(j))
            #print("value: " + str(level[i][j].val))
            start = time.time()

            leftTotal,rightTotal = [1] * X, [1] * X
            if (level[i][j].left == None and level[i][j].right == None):
                level[i][j].maxNutrient = range(level[i][j].val, level[i][j].val+X)
                leftTotal = rightTotal = None
            else:
                level[i][j].maxNutrient = [1] * X
                nodeVal,edgeFlow,currentAlloc = 0, 1, 0
                while currentAlloc < X:
                    flow = edgeFlow**2
                    nnode =  level[i][j].left.maxNutrient[nodeVal]
                    if nnode <= flow:
                        nodeVal +=1
                        leftTotal[currentAlloc] = nnode
                    else:
                        edgeFlow+=1
                        leftTotal[currentAlloc] = flow
                    currentAlloc+=1
                
                nodeVal,edgeFlow,currentAlloc = 0, 1, 0
                while currentAlloc < X:
                    flow = edgeFlow**2
                    nnode =  level[i][j].right.maxNutrient[nodeVal]
                    if nnode <= flow:
                        nodeVal+=1
                        rightTotal[currentAlloc] = nnode
                    else:
                        edgeFlow+=1
                        rightTotal[currentAlloc] = flow
                    currentAlloc+=1
            end = time.time()
            preprocessTime += (end - start)
            """
            for k in range(X):
                if (level[i][j].left == None and level[i][j].right == None):
                    level[i][j].maxNutrient.append(level[i][j].val+k)
                    leftTotal = rightTotal = None
                else:
                    level[i][j].maxNutrient.append(1)
                    for l in range(k+1):
                        leftNodeAlloc,leftEdgeAlloc = k-l, l
                        rightNodeAlloc,rightEdgeAlloc = k-l, l
                        leftTotal[k] = max(leftTotal[k], max(1, min(level[i][j].left.maxNutrient[leftNodeAlloc], (leftEdgeAlloc+1) ** 2)))
                        rightTotal[k] = max(rightTotal[k], max(1, min(level[i][j].right.maxNutrient[rightNodeAlloc], (rightEdgeAlloc+1) ** 2)))
            """
            start = time.time()
            for k in range(X):
                for l in range(k+1):
                    #print("k: " + str(k))
                    #print("l: " + str(l))
                    #print("left: " + str(leftTotal[k-l]))
                    #print("right: " + str(rightTotal[l]))
                    if leftTotal != None and rightTotal != None:
                        #print(leftTotal)
                        #print(rightTotal)
                        level[i][j].maxNutrient[k] = max(level[i][j].maxNutrient[k], leftTotal[k-l] + rightTotal[l])
            #print(level[i][j].maxNutrient)
            end = time.time()
            mainprocessTime += (end - start)

    print("preprocess time Elapsed: " + str(preprocessTime * 1000) + " ms")
    print("mainprocess time Elapsed: " + str(mainprocessTime * 1000) + " ms")
    return max(root.maxNutrient)

if __name__== "__main__":
    buildTree()
    verifyTree(root)
    #print(res[2:])

    start = time.time()
    print(dp(root))
    end = time.time()
    print("Time Elapsed: " + str((end - start) * 1000) + " ms")