#########################   QUESTIONS
q: int = int(input("How wide should matrix MxN be?"))
p: int = int(input("How tall should matrix MxN be?"))


##########################  CREATING ARRAY MxN
import random
array = list(range(0,q))
for l in array:
    array[l] = list(range(0,p))
    for u in array[l]:
        array[l][u] = random.randint(0,1)


############################### CHOOSING (xs,ys) and (xa,ya)
xs = random.randint(0,q-2)                                    #randomly choosing starting, ending points
ys = random.randint(0,p-2)
xa = random.randint(xs+1,q-1)
ya = random.randint(ys+1,p-1)


#############################CREATING D
d = list(range(0,(xa-xs+1)))
assert isinstance(d, object)
for i in d:
    d[i] = list(range(0,(ya-ys+1)))
d[0][0] = array[xs][ys]

###########################SOLVING FIRST COLUMN
x=1
colsum = array[xs][ys]
def firstcol(array, d, colsum, x):
    while x < len(d[0]):
        colsum = colsum + array[xs][ys+x]
        d[0][x] = colsum % 2    #sum of path modulus 2 = d[0][j]
        x = x + 1
        firstcol(array, d, colsum, x)

###########################SOLVING FIRST ROW
y: int = 1
rowsum = array[xs][ys]
def firstrow(array,d,rowsum,y):
    while y < len(d):
        rowsum = rowsum + array[xs+y][ys]
        d[y][0] = rowsum % 2  # sum of path modulus 2 = d[i][0]
        y = y + 1
        firstrow(array, d, rowsum, y)


####################    THE REST OF THE MATRIX
col = 1
row = 1
def definer2(array,d,col,row):                                  #only works for inside cols/rows
    if col == len(d) - 1 and row == len(d[0]) - 1:                          #last element? len(d) = width, len(d[0]) = height of the matrix
        if array[col+xs][row+ys] == 0:    #array[i][j] == even
            if d[col][row-1] == d[col-1][row]:                      #if neighboring cells of d[i][j] are equal
                    if d[col][row-1] == d[col-1][row] == 0:
                        d[col][row] = 0
                        ##
                    elif d[col][row-1] == d[col-1][row] == 1:
                        d[col][row] = 1
                        ##
                    elif d[col][row-1] == d[col-1][row] == 2:
                        d[col][row] = 2
                        ##
            else:   #if d[i-1][j] != d[i][j-1]
                d[col][row] = 2
                ##
        else:     #array[i][j] == odd
            if d[col][row-1] == d[col-1][row]:
                if d[col][row-1] == d[col-1][row] == 0:
                    d[col][row] = 1
                    ##
                elif d[col][row-1] == d[col-1][row] == 1:
                    d[col][row] = 0
                    ##
                elif d[col][row-1] == d[col-1][row] == 2:
                    d[col][row] = 2
                    ##
            else:   #if d[i-1][j] != d[i][j-1]
                d[col][row] = 2                                         ################
    else:                                                       #not on last element
        if array[col+xs][row+ys] == 0:    #array[i][j] == even
            if d[col][row-1] == d[col-1][row]:                      #if neighboring cells of d[i][j] are equal
                    if d[col][row-1] == d[col-1][row] == 0:
                        d[col][row] = 0
                        if row == len(d[0])-1:
                            row = 1
                            col = col + 1
                            definer2(array, d, col, row)
                        else:
                            row = row + 1
                            definer2(array, d, col, row)
                    elif d[col][row-1] == d[col-1][row] == 1:
                        d[col][row] = 1
                        if row == len(d[0])-1:
                            row = 1
                            col = col + 1
                            definer2(array, d, col, row)
                        else:
                            row = row + 1
                            definer2(array, d, col, row)
                    elif d[col][row-1] == d[col-1][row] == 2:
                        d[col][row] = 2
                        if row == len(d[0])-1:
                            row = 1
                            col = col + 1
                            definer2(array, d, col, row)
                        else:
                            row = row + 1
                            definer2(array, d, col, row)
            else:   #if d[i-1][j] != d[i][j-1]
                d[col][row] = 2
                if row == len(d[0])-1:
                    row = 1
                    col = col + 1
                    definer2(array, d, col, row)
                else:
                    row = row + 1
                    definer2(array, d, col, row)
        else:     #array[i][j] == odd
            if d[col][row-1] == d[col-1][row]:
                if d[col][row-1] == d[col-1][row] == 0:
                    d[col][row] = 1
                    if row == len(d[0])-1:
                        row = 1
                        col = col + 1
                        definer2(array, d, col, row)
                    else:
                        row = row + 1
                        definer2(array, d, col, row)
                elif d[col][row-1] == d[col-1][row] == 1:
                    d[col][row] = 0
                    if row == len(d[0])-1:
                        row = 1
                        col = col + 1
                        definer2(array, d, col, row)
                    else:
                        row = row + 1
                        definer2(array, d, col, row)
                elif d[col][row-1] == d[col-1][row] == 2:
                    d[col][row] = 2
                    if row == len(d[0])-1:
                        row = 1
                        col = col + 1
                        definer2(array, d, col, row)
                    else:
                        row = row + 1
                        definer2(array, d, col, row)
            else:   #if d[i-1][j] != d[i][j-1]
                d[col][row] = 2
                if row == len(d[0])-1:
                    row = 1
                    col = col + 1
                    definer2(array, d, col, row)
                else:
                    row = row + 1
                    definer2(array, d, col, row)


#####################################           FINDING THE PATH            ########################################

########################## SET UP VARIABLES AND ARRAYS
path = list(range(0,int(len(d)+len(d[0])-1)))
for r in path:
    path[r] = [0,0,5]
ticker = int(len(d))+int(len(d[0]))-2               #counts which cell we're checking
path[int(len(d)+len(d[0])-2)][0] = xa               #address of the final cell is (xa,ya)
path[int(len(d)+len(d[0])-2)][1] = ya               #   ^^^^                          ^^
path[int(len(d)+len(d[0])-2)][2] = 0
m = 0
n = 0



def path_finder(array, d, ticker, path, m, n, xa, ya, xs, ys):
    if ticker == 0:                                                         # if we're on (xs,ys)
        first_cell(path, xs, ys, d)
    elif d[int(len(d)) - int(m) - 1][int(len(d[0])) - int(n) - 1] == 2:
        if (d[int(len(d)) - m - 2][int(len(d[0])) - n - 1] + array[xa - m][ya - n]) % 2 == path[ticker][2] and d[int(len(d)) - m - 2][int(len(d[0])) - n - 1] != 2:         #if left-neighbor != 2 AND == what we need it to equal (path[ticker][2])
            GoLeft(d, array, path, ticker, m, n, xa, ya)
        elif (d[int(len(d)) - m - 1][int(len(d[0])) - n - 2] + array[xa - m][ya - n]) % 2 == path[ticker][2] and d[int(len(d)) - m - 1][int(len(d[0])) - n - 2] != 2:       #if up-neighbor != 2 AND == what we need it to equal (path[ticker][2])
            GoUp(d, array, path, ticker, m, n, xa, ya)
        elif d[int(len(d)) - m - 2][int(len(d[0])) - n - 1] == 2:                     #if left-neighbor == 2
            GoLeft(d, array, path, ticker, m, n, xa, ya)
        elif d[int(len(d)) - m - 1][int(len(d[0])) - n - 2] == 2:                     #if up-neighbor ==2
            GoUp(d, array, path, ticker, m, n, xa, ya,)
        else:                                                       #no neighbors are == 2 or are part of OUR correct path
            backtrack(d, path, ticker, backtrack_right, backtrack_down, m, n)
    elif d[int(len(d)) - m - 1][int(len(d[0])) - n - 1] != 2 and d[int(len(d)) - m - 1][int(len(d[0])) - n - 1] != 99:  #solving when current cell != 2, hasn't been not backtracked from
        if m == len(d) - 1:                                     #if we're in the first column
            n = n + 1                                               #go up an element
            ticker = ticker - 1
            path[ticker][1] = int(ya - n)
            path[ticker][0] = int(xs)
            path_finder(array, d, ticker, path, m, n, xa, ya, xs, ys)
        elif n == int(len(d[0]) - 1):                                #if we're in the first row
            m = m + 1                                                   #go left an element
            ticker = ticker - 1
            path[ticker][0] = int(xa - m)
            path[ticker][1] = int(ys)
            path_finder(array, d, ticker, path, m, n, xa, ya, xs, ys)
        else:                                                   #if we're anywhere else
            m = m + 1                                               #go left an element
            ticker = ticker - 1
            path[ticker][0] = int(xa - m)
            path[ticker][1] = int(ya - n)
            path_finder(array, d, ticker, path, m, n, xa, ya, xs, ys)


#################SUB-FUNCTIONS


def GoLeft(d, array, path, ticker, m, n, xa, ya):
    ticker = ticker - 1
    m = m + 1
    path[ticker][0] = int(xa - m)  # maybe +- 1 here
    path[ticker][1] = int(ya - n)
    path[ticker][2] = (((path[ticker + 1][2]) + (array[xa - m + 1][ya - n])) % 2)         ####CHANGED "ya-n-1" TO "ya-n"
    path_finder(array, d, ticker, path, m, n, xa, ya, xs, ys)

def GoUp(d, array, path, ticker, m, n, xa, ya):
    ticker = ticker - 1
    n = n + 1
    path[ticker][0] = int(xa - m)
    path[ticker][1] = int(ya - n)  # maybe +- 1 here
    path[ticker][2] = ((path[ticker + 1][2]) + (array[xa - m][ya - n + 1])) % 2          ####CHANGED "xa - m -1" TO "xa - m"
    path_finder(array, d, ticker, path, m, n, xa, ya, xs, ys)

############BACKTRACKING
def backtrack(d, path, ticker, backtack_right, backtrack_down, m, n):
    d[int(len(d)) - m - 1][int(len(d[0])) - n - 1] = 99                   #mark this  cell as a dead end
    if path[ticker][0] == path[ticker - 1][0]:         #if the previous cell was to the right
        backtack_right(path, ticker, m)
    else:                                             #if previous cell was downward
        backtrack_down(path, ticker, n)

def backtrack_right(path, ticker, m):
    m = m + 1
    ticker = ticker - 1
    path_finder(array, d, ticker, path, m, n, xa, ya, xs, ys)
def backtrack_down(path,ticker,n):
    n = n + 1
    ticker = ticker - 1
    path_finder(array, d, ticker, path, m, n, xa, ya, xs, ys)


#######################CONVERTING THE LIST OF COORDINATES INTO A LEGIBLE FORMAT
def first_cell(path,xs,ys,d):
    path[0][0] = xs
    path[0][1] = ys
    t = 0
    while t < int(len(d)) + int(len(d[0])) - 1:                     #cleaning up path[][] into printable array of coordinates
        del path[t][2]
        t = t + 1
    print("The path is: " + str(path))

###################ALL-ENCOMPASSING FUNCTION
def final(array,d,col,row,colsum,rowsum,x,y):
    firstcol(array,d,colsum,x)
    firstrow(array,d,rowsum,y)
    definer2(array,d,col,row)
    print("MxN = " + str(array))
    print("(xs,ys) = (" + str(xs) + "," + str(ys) + ")")
    print("(xa,ya) = (" + str(xa) + "," + str(ya) + ")")
    #print(d)
    if d[int(len(d))-1][int(len(d[0])-1)] == 2 or d[int(len(d))-1][int(len(d[0])-1)] == 0:
        print("There IS an even path from (" + str(xs) + "," + str(ys) + ") to " + "(" + str(xa) + "," + str(ya) + ")")
        path_finder(array, d, ticker, path, m, n, xa, ya, xs, ys)
    else:
        print("There IS NOT an even path from (" + str(xs) + "," + str(ys) + ") to " + "(" + str(xa) + "," + str(ya) + ")")


######################################      RUN THE FINAL FUNCTION      ################################
final(array,d,col,row,colsum,rowsum,x,y)