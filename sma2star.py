#! /usr/bin/python

import sys

#-- setup of the shift for lower-left corner-----------------
#-- put 0 if not shift is wanted
MINX = 0 #82000
MINY = 0 #445000
#------------------------------------------------------------

def format_star(ls):
    h = {}
    for i in range(0, len(ls), 2):
        h[ls[i]] = ls[i+1]
    sid = iter(h).next()
    star = [sid]
    i = h[sid]
    while i != sid:
        star.append(i)
        try:
            i = h[i]
        except KeyError:
            for i in range(0, len(ls), 2):
                if ls.count(ls[i]) != 2:
                    sid = ls[i]
                    break
            star = [0, sid] #-- 0 always first id in a CH star
            i = h[sid]
            while 1:  
                star.append(i)
                try:
                    i = h[i]
                except KeyError:
                    break
            break
    #print "STAR", star
    return star

def main():
    d = {}
    sys.stdin.readline() #-- bb_min
    sys.stdin.readline() #-- bb_max
    i = 1
    while 1:
        line = sys.stdin.readline()
        if line != '':
            if line[0] == 'v':
                xyz = map(float, line[2:].split(' '))
                d[i] = [(xyz[0], xyz[1], xyz[2]), []]
                i += 1
            
            elif line[0] != '#': #-- 'f' is the first char
                ids = map(int, line[2:].split(' '))
                
                for j in range(3):
                    if ids[j] < 0:
                        ids[j] = ids[j] + i
                id = ids[0]
                d[id][1].append(ids[1])
                d[id][1].append(ids[2])
                id = ids[1]
                d[id][1].append(ids[2])
                d[id][1].append(ids[0])
                id = ids[2]
                d[id][1].append(ids[0])
                d[id][1].append(ids[1])
                    
                ids = map(int, line[2:].split(' '))
                for id in ids: #-- delete the finalised vertex
                    if id < 0: 
                        gid = i + id
                        star = format_star(d[gid][1])
                        sys.stdout.write(str(gid) + "\t" + str(d[gid][0][0] + MINX) + "\t" + str(d[gid][0][1] + MINY) + 
                        "\t" + str(d[gid][0][2]) + "\t{" + ",".join(map(str, star)) + "}\n")
#                        sys.stdout.write(str(gid) + "\t" + "\t".join(map(str,d[gid][0])) + 
#                        "\t{" + ",".join(map(str, star)) + "}\n")
                        del d[gid]
                        
        else:
            iterd = iter(d)
            for id in iterd:
                star = format_star(d[id][1])
                sys.stdout.write(str(id) + "\t" + str(d[id][0][0] + MINX) + "\t" + str(d[id][0][1] + MINY) + 
                "\t" + str(d[id][0][2]) + "\t{" + ",".join(map(str, star)) + "}\n")
#                sys.stdout.write(str(id) + "\t" + "\t".join(map(str,d[id][0])) +
#                "\t{" + ",".join(map(str, star)) + "}\n")
     
            sys.stdout.flush()
            break
            
if __name__ == "__main__":
    main()   
