def PageRank(AdMatrix):
    rankscore = [1/6 for i in range(6)]

    return rankscore


def Adjacency_Display(s,t):
    res = [[0 for j in range(6)] for i in range(6)]
    for i in range(9):
        res[s[i]-1][t[i]-1] = 1
    # for j in res:
    #     print(j)
    return res

if __name__ == '__main__':
    s = [1, 1, 2, 2, 3, 3, 3, 4, 5]
    t = [2, 5, 3, 4, 4, 5, 6, 1, 1]
    AdMatrix = Adjacency_Display(s,t)
    rankscore = PageRank(AdMatrix)
    print('NodeName\t', 'PageRankScore')
    node = 1
    for i in rankscore:
        print(node,'\t\t\t',i)
        node += 1