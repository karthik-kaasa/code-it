"""
This module implements a set of platform-neutral Unix utilities that can be useful in day-to-day activities.
This module can be useful in Windows and Unix where command line unavailable.
"""

def uniq(L,count=False):
    """
    uniq function remove duplicates in input list and return unique items.
    Optionally also return count of number of occurrence of each item when second arguement is True.
    """
    if not count:
        return list(set(list(L)))
    D = {}
    for i in L:
        if i in D: D[i] += 1
        else: D[i] = 1
    return sorted([(k,D[k]) for k in D], key=lambda x: x[1], reverse=True)


def cat(filename=""):
    """
    Prints file content in stdout.
    """
    if not filename:
        return "Usage: cat(filename)"
    fh = open(filename)
    print(fh.read())
    fh.close()

def tac(filename=""):
    """
    Prints file content in stdout in reverse order.
    """
    if not filename:
        return "Usage: tac(filename)"
    fh = open(filename)
    lines = reversed(fh.readlines())
    for ln in lines: print(ln, end="")
    fh.close()

def wc(filename=""):
    """
    Return tuple of 3 elements:
        (char count, word count, line count)
        By indexing returned tuple, desired count can be selected.
        Example:
            To get number of lines in a file, run:
                wc("testfile.txt")[2]
    """
    if not filename:
        return "Usage: wc(filename)"
    fh = open(filename)
    ch, wd, ln = 0, 0, 0
    ch = len(fh.read()); fh.seek(0)
    wd = len(fh.read().split()); fh.seek(0)
    ln = len(fh. readlines())
    fh.close()
    return (ch, wd, ln)

if __name__ == "__main__":
    L = [0,4,1,5,4,6,7,6]
    print(uniq(L))
    print(uniq(L,True))
    
    print(wc("test.txt"))
    print(wc("test.txt")[2])
    
    cat("test.txt")
    print("-" * 60)
    tac("test.txt")

"""
output:
[0, 1, 4, 5, 6, 7]
[(4, 2), (6, 2), (0, 1), (1, 1), (5, 1), (7, 1)]
(853, 144, 21)
21
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
...
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea — let’s do more of those!
————————————————————
Namespaces are one honking great idea — let’s do more of those!If the implementation is easy to explain, it may be a good idea.
...
Beautiful is better than ugly.

The Zen of Python, by Tim Peters
"""
