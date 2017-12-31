def uniq(L,count=False):
    if not count:
        return list(set(list(L)))
    D = {}
    for i in L:
        if i in D: D[i] += 1
        else: D[i] = 1
    return sorted([(k,D[k]) for k in D], key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    L = [0,4,1,5,4,6,7,6]
    print(uniq(L))
    print(uniq(L,True))

"""
output:
[0, 1, 4, 5, 6, 7]
[(4, 2), (6, 2), (0, 1), (1, 1), (5, 1), (7, 1)]
"""
