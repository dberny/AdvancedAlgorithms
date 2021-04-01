import copy

def getNumVars(cnf):
    nums = []
    for clause in cnf:
        for literal in clause:
            if abs(literal) not in nums:
                nums.append(abs(literal))
    return len(nums)

def solveCNF(cnf):
    numVars = getNumVars(cnf)
    literals = list(range(1, numVars+1))
    return recSolveCNF(cnf, numVars, literals)

def recSolveCNF(cnf, numVars, literals):
    if len(cnf) == 0:
        return True

    for clause in cnf:
        if len(clause) == 0:
            return False

    findAndRemoveUnitClauses(cnf, literals)
    print(literals)
    findAndRemovePureLiterals(cnf, literals)
    return solveCNF(cnf)
    newCnf = assignAndSimplify(cnf)
    return solveCNF(newCnf)
    return len(cnf) == 0

def assignAndSimplify(origCnf):
    cnf = copy.deepcopy(origCnf)
    if len(cnf) == 0:
        return cnf
    print(cnf)
    assigning = cnf[0][0]
    # if assigning < 0
    i = 0
    while i < len(cnf):
        if assigning in cnf[i]:
            cnf.pop(i)
            continue
        elif -assigning in cnf[i]:
            cnf[i].remove(-assigning)
        i += 1
    return cnf


# def assignAndRemove(cnf):


def findAndRemovePureLiterals(cnf, literals):
    i = 0
    pureTracking = {}
    while i < len(literals):
        negate = False
        foundFirst = False
        for clause in cnf:
            for x in clause:
                if abs(x) == literals[i]:
                    if not foundFirst:
                        pureTracking[abs(x)] = True
                        foundFirst = True
                        if x < 0:
                            negate = True
                    else:
                        if (negate and x > 0) or (not negate and x < 0):
                            pureTracking[abs(x)] = False
        i += 1
    print(pureTracking)
    removePureLiterals(cnf, literals, pureTracking)

def removePureLiterals(cnf, literals, pureLiterals):
    for literal in pureLiterals.keys():
        if pureLiterals[literal]:
            i = 0
            while i < len(cnf):
                if literal in cnf[i] or -literal in cnf[i]:
                    cnf.pop(i)
                    continue
                i += 1

def findAndRemoveUnitClauses(cnf, literals):
    i = 0
    while i < len(cnf):
        if len(cnf[i]) == 1:
            print(cnf)
            removeUnitClause(cnf, cnf[i][0], literals)
            i = 0
        else:
            i += 1

def removeUnitClause(cnf, unit, literals):
    print(unit)
    print(literals)
    literals.remove(abs(unit))
    i = 0
    while i < len(cnf):
        if unit in cnf[i]:
            cnf.pop(i)
            continue
        if -unit in cnf[i]:
            cnf[i].remove(-unit)
        i += 1

if __name__ == '__main__':
    # cnf = [[1, 2, 3], [2, 3, 4]]
    # cnf = [[1], [2], [3, -2], [1, 2, 3, 4], [5, 6, -6], [6, 7]]
    cnf = [[1, 2, 3], [-1], [1, 2, -3], [1, -2], [2, -4]]
    # cnf = []
    print(solveCNF(cnf))
