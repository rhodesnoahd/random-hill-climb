import numpy as np

class Info:
    def __init__(self):
        self.sol = None
        self.fOfSol = None
        self.numSolSearched = 0

f = lambda x,y : ((((1.5-x) + (x*y))**2) + (((2.25-x) + (x*y*y))**2) + (((2.625-x) + (x*y*y*y))**2))
# TODO
# inRange = lambda p : ((p >= -4.5 and p <= 4.5)) 


def RHC(sp, p, z, seedValue):
    ans = Info() # to return answer
    ans.sol = sp
    ans.fOfSol = f(ans.sol[0], ans.sol[1])

    # create generator
    rng = np.random.default_rng(seed=seedValue)
    
    # simulate do-while
    while True: 
        # initialize neighborhood array with current best solution (all p elements)
        neighborhood = np.array([[ans.sol[0], ans.sol[1]]] * p)
        # randomly sample p points in the neighborhood
        neighborhood =  neighborhood + np.array(rng.uniform(low=(-1.0*z), high=z, size=2*p)).reshape(p,2)
        # determine best solution of sampled points
        bestSol_ofSample = neighborhood[np.argmin(np.array(f(neighborhood[:,0], neighborhood[:,1]))),:]
        fOf_bestSol_ofSample = f(bestSol_ofSample[0], bestSol_ofSample[1])

        # iterate until no better solution found
        if fOf_bestSol_ofSample >= ans.fOfSol:
            break

        # update results
        ans.sol = bestSol_ofSample
        ans.fOfSol = fOf_bestSol_ofSample
        ans.numSolSearched += p

    return ans

def main():
    startingPoints = [[2,2], [1,4], [-2,-3], [1,-2]]
    numNeighbors = [80, 500]
    neighborhoodSizes = [0.1, 0.02]
    seedValue = [42, 77977]
    
    #  run RHC twice w/ given parameters -> 32 total runs
    run = 0
    for i in range(2):
        print("Seed =", seedValue[i])
        for sp in startingPoints:
            print("    " + "Starting point:", sp)
            for p in numNeighbors:
                print("    " + "    " + "Number of neighbors:", p)
                for z in neighborhoodSizes:
                    print("    " + "    " + "    " + "Neighborhood size:", z)
                    run += 1
                    print("    " + "    " + "    " + "    " + "Run", run)
                    answer = RHC(sp, p, z, seedValue[i])
                    print("    " + "    " + "    " + "    " + "# of sol searched:",answer.numSolSearched)
                    print("    " + "    " + "    " + "    " + "sol:", answer.sol)
                    print("    " + "    " + "    " + "    " + "f(sol):", answer.fOfSol)

    # 33rd run
    mySp = [2.99966961, 0.49989166]
    myP = 50
    myZ = 0.00000001
    mySeedValue = 22
    print("\n33rd run")
    print("    " + "Seed =", mySeedValue)
    print("    " + "Starting point:", mySp)
    print("    " + "Number of neighbors:", myP)
    print("    " + "Neighborhood size:", myZ)
    myAnswer = RHC(mySp, myP, myZ, mySeedValue)
    print("    " + "    " + "# of sol searched:", myAnswer.numSolSearched)
    print("    " + "    " + "sol:", myAnswer.sol)
    print("    " + "    " + "f(sol):", myAnswer.fOfSol)

if __name__ == "__main__":
    main()