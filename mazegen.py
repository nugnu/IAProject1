import numpy as np

def generate_maze(path):
    maze = open(path, 'r')
    ret = []
    spots = { 
        " ": 4, 
        "-": 4,
        "_": 4,
        ".": 5, 
        "|": 6, 
        "o": 7, 
    }
    
    count_prev = 0
    count = 0
    for line in maze:
        if (count != count_prev and count_prev != 0): 
            assert 0 # its must be a grid
        count_prev = count
        count = 0
        for x in line:
            if x in spots.keys():
                ret.append(spots[x])
                count = count + 1
    
    ret = np.array(ret).reshape(len(ret)//count, count)    
    ret = ret.tolist()
    return ret
