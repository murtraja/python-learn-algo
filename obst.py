p = [0,3,3,1,1]
q = [2,3,1,1,1]
w = [[-1 for _ in range(0, len(q))] for _ in range(0, len(q))]
e = [[-1 for _ in range(0, len(q)+1)] for _ in range(0, len(q)+1)]
r = [[-1 for _ in range(0, len(q)+1)] for _ in range(0, len(q)+1)]
'''
OUTPUT:
Cost of tree: 40
preorder traversal: 
2 
1 
3 
4 
'''
def getE(i, j):
    # print("e[{}][{}]".format(i,j))
    if e[i][j] != -1:
        return e[i][j];
    if i == j + 1:
        # raw_input("base case")
        e[i][j] = q[j]
        return e[i][j]
    elif i > j:
        print("Undefined value")
        return;
    possibleTreeCosts = [getE(i,R-1)+getE(R+1,j) for R in range(i, j+1)]
    minTreeCost = min(possibleTreeCosts)
    root = possibleTreeCosts.index(minTreeCost) + i; 
    e[i][j] = minTreeCost + getW(i,j)
    r[i][j] = root;
    return e[i][j]
    

def getW(i, j):
    # print("w[{}][{}]".format(i,j))
    if w[i][j] != -1:
        # raw_input("value available")
        return w[i][j];
    # raw_input("value unavailable")
    if i == j + 1:
        # raw_input("base case")
        w[i][j] = q[j]
        return w[i][j]
    elif i > j:
        print("Undefined value")
        return;

    # raw_input("recursion")
    w[i][j] = getW(i, j-1) + p[j] + q[j]
    return w[i][j]

def getTree(i, j):
    if i > j:
        return;
    # print("Tree {} {}".format(i,j))
    # raw_input();
    root = r[i][j];
    print("{} ".format(root))
    getTree(i,root-1)
    getTree(root+1, j)

def main():
    # first let's construct w
    # print(w);
    # print([getW(x,4) for x in range(1,5)]);
    # print(w);

    print("Cost of tree: {}".format(getE(1,len(p) - 1)))
    # for row in e:
    #     print(row)
    print("preorder traversal: ")
    getTree(1,len(p) - 1)




if __name__ == "__main__":
    main()