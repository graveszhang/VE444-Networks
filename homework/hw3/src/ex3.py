import numpy as np

def PageRank(AdMatrix, beta=0.85):
    # beta is the probability of following a link, set 0.85 by default
    r = [1/6 for i in range(6)]
    N = [[1/6 for i in range(6)] for j in range(6)]
    r = np.array(r)
    M = np.array(AdMatrix)
    N = np.array(N)
    M = M.transpose()
    d = getDegree(M)
    d[-1] = 1
    M = np.divide(M,d)
    A = beta * M + (1 - beta) * N
    A[:,-1] = 1/6 # Lead to converge
    r_cpy = r.copy()
    while True:
        r = A.dot(r_cpy)
        if (r == r_cpy).all():
            break
        else:
            r_cpy = r
    return r

def getDegree(AdMatrix):
    deg = [0 for i in range(6)]
    for i in AdMatrix:
        for k in range(6):
            if i[k] == 1:
                deg[k] += 1
    # print(deg)
    return deg

def Adjacency_Display(s,t):
    res = [[0 for j in range(6)] for i in range(6)]
    for i in range(9):
        res[s[i]-1][t[i]-1] = 1
    # check the adjacency matrix result
    # for j in res:
    #     print(j)
    return res

if __name__ == '__main__':
    s = [1, 1, 2, 2, 3, 3, 3, 4, 5]
    t = [2, 5, 3, 4, 4, 5, 6, 1, 1]
    AdMatrix = Adjacency_Display(s,t)
    rank = PageRank(AdMatrix)
    print('NodeName\t', 'PageRankScore')
    node = 1
    for i in rank:
        print(node,'\t\t\t',i)
        node += 1