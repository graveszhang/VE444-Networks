def PageRank(AdMatrix, degree, beta=0.85):
    # beta is the probability of following a link, set 0.85 by default
    rankscore = [1/6 for i in range(6)]
    old_rankscore = rankscore[:]
    N = 6
    j = 0
    while True:
        i = 0
        curr_score = 0
        for row in AdMatrix:
            if row[j] == 1:
                curr_score += beta*(rankscore[i]/degree[i])
            i += 1
        rankscore[j] = ((1-beta)/N) + curr_score
        j += 1
        if j == 6: # finish one round updating
            j = 0  # start new round updating
            if rankscore == old_rankscore: # converge
                break
            else:
                # update a copy to check if converge
                old_rankscore = rankscore[:]
    return rankscore

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
    degree = getDegree(AdMatrix)
    rankscore = PageRank(AdMatrix, degree)
    print('NodeName\t', 'PageRankScore')
    node = 1
    for i in rankscore:
        print(node,'\t\t\t',i)
        node += 1