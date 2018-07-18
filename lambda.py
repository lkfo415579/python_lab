list = [[1,1],[5,-5],[7,3],[4,43],[0,23],[0,5],[3,6],[1,7]]
list2 = [[3,5555],[4,4]]
#find max index

#print max(list,key=lambda x : x)
print list.index(max(list,key=lambda x: x[1]))
# print "index_max", max(xrange(len(list)), key=lambda x: x[1])
# print list.__getitem__


def second(list):
    return list[1]
#
def new_second(index,a):
    return a[index][1]
#print max(xrange(len(list)),key=new_second(list))

#print max(list,list2,key=lambda x : x)

#print min(xrange(len(list)),key=lambda x : list[x][1])
