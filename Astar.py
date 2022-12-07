lis=[]
def astar(s,e):
    op_set=set(s)
    cl_set=set()
    g={}
    p={}
    g[s]=0
    p[s]=s
    while(len(op_set)>0):
        n=None
        for v in op_set:
            if(n==None):
                n=v
        if n==e or graph[n]==None:
            pass
        else:
            for (m,w) in get_neighbour(n):
                if m not in op_set and m not in cl_set :
                    op_set.add(m)
                    p[m]=n
                    g[m]=g[n]+w
                else:
                    if g[m]>g[n]+w:
                        g[m]=g[n]+w
                        p[m]=n
                        
                    if m in cl_set:
                        cl_set.remove(m)
                        cl_set.add(m)
        if n==None:
              print("not exist")
              return None
        if n==e:
            path=[] 
            while(p[n]!=n):
                path.append(n)
                n=p[n]
            path.append(s)
            path.reverse()
            lis=path
            print(lis)
            print("path is ",path)
            return path
        op_set.remove(n)
        cl_set.add(n)
    return None
        
def get_neighbour(v):
    if v in graph:
        return graph[v]
    else:
        return None
graph={'A':[('B',2),('E',10)],
       'B':[('A',10),('C',5),('G',1)],
       'C':[('B',1)],
       'E':[('D',6),('A',3)],'D':[('G',9),('E',1)],
       'G':[('D',1),('B',9)]
       }

astar('E','C')