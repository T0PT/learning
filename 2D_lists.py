
def swap_col(lst, a, b):
    edited=[[]]
    for y in range(len(lst)):
        for x in range(len(lst)):
            if x==a:
                edited[y].append(lst[y][b])
            elif x==b:
                edited[y].append(lst[y][a])
            else:
                edited[y].append(lst[y][x])
        edited.append([])
        print(edited[y])


def diag():
    r = int(input('width and height?'))
    for y in range(r):
        lst = ''
        for x in range(r):
            lst+=str(abs(x-y))+' '
        print(lst)



def snezh():
    r=int(input('width and height?'))
    for y in range(r):
        lst=''
        for x in range(r):
            if x==y or x==r-y-1:
                lst+=' *'
            elif x==int(r/2) or y==int(r/2):
                lst+=' *'
            else:
                lst+='  '
        print(lst)

swap_col([
    [11,12,13,14],
    [21,22,23,24],
    [31,32,33,34] ], 0,1)