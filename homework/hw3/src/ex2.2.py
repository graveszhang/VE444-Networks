from collections import defaultdict
import random

def HillClimbing(pool,choice,satisfied):
    result = []
    best = ''
    now_satisfied = 0
    real_satisfied = satisfied.copy()

    while now_satisfied != 8:
        ## Initialize max before every round, update after each movie
        max_satisfied = 0
        random.shuffle(pool)
        for movie in pool:
            ## Before comparison of movies, update
            num_satisfied = 0
            satisfied = real_satisfied.copy()

            for person in choice[movie]:
                if not satisfied[person]:
                    satisfied[person] = True
                    num_satisfied += 1
            if num_satisfied > max_satisfied:
                max_satisfied = num_satisfied
                best = movie

        result.append(best)
        now_satisfied += max_satisfied
        for person in choice[best]:
            real_satisfied[person] = True
        if best in pool:
            pool.remove(best)
    return result

def getChoices():
    map = defaultdict(list)
    satisfied = {}
    f = open("Employee_Movie_Choices.txt")
    lines = f.readlines()[1:]
    for line in lines:
        person = line.split('\t', 1)[0]
        movie_name = line.split('\t', 1)[1].rstrip()
        satisfied[person] = False
        if person not in map[movie_name]:
            map[movie_name].append(person)
    f.close()
    return map, satisfied

def getMovies():
    names = []
    f = open("Employee_Movie_Choices.txt")
    lines = f.readlines()[1:]
    for line in lines:
        movie_name = line.split('\t',1)[1].rstrip()
        if movie_name not in names:
            names.append(movie_name)
    f.close()
    return names

if __name__ == '__main__':
    pool = []
    choice = defaultdict(list)
    satisfied = {}
    pool = getMovies()
    choice,satisfied = getChoices()

    result = HillClimbing(pool,choice,satisfied)
    print(result)


