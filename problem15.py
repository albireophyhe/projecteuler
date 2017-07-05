#-coding- unicode

if __name__ == "__main__":
    #set goal
    goal = (20,20)
    #set initial position and grid
    totalsteps = goal[0]+goal[1]
    Num = 1.
    Deno = 1.
    for i in range(0,goal[0]):
        Num = Num*(totalsteps-i)
    for j in range(1,goal[1]+1):
        Deno = Deno*j
    totalroutes = Num/Deno
    print totalroutes
