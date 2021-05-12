#!/usr/bin/python3
# 
# Een nieuw script om de totalen van de uren per week dat de computer aanstond te tonen.
# A new script to show the total number of hours the computer was on per week.
# Werkt op een ubuntu werkstation.
# Works on a ubuntu worstation.
#
# last -F > last.out 
# ./pwrt_local.py last.out
# ./pwrt_local.py last.out 'weeknumber'
# 2021 Matthew Buchanan Astley
 
import os,sys
import time
import datetime
import pprint  

try:
    a = sys.argv[1]
    #e1 = os.stat(a)
    #print(e1)
except IndexError:
    print("Provide last -F filename")
    print("    last -F > last.out")
    print("    ./pwrt_local.py last.out")
    print("    ./pwrt_local.py last.out 'weeknumber'")
    sys.exit()

a1 = open(a, "r")

c = { "1" : [], "2" : [], "3" : [], "4" : [], "5" : [], 
      "6" : [], "7" : [], "8" : [], "9" : [], "10" : [], 
      "11" : [], "12" : [], "13" : [], "14" : [], "15" : [],
      "16" : [], "17" : [], "18" : [], "19" : [], "20" : [],
      "21" : [], "22" : [], "23" : [], "24" : [], "25" : [],
      "26" : [], "27" : [], "28" : [], "29" : [], "30" : [],
      "31" : [], "32" : [], "33" : [], "34" : [], "35" : [],
      "36" : [], "37" : [], "38" : [], "39" : [], "40" : [],
      "41" : [], "42" : [], "43" : [], "44" : [], "45" : [],
      "46" : [], "47" : [], "48" : [], "49" : [], "50" : [],
      "51" : [], "52" : [] }

d = { 'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12 }

def pt(self,b):
    a = self[int(b)][3].split(":")
    tm_year = int(self[int(b)][4])
    tm_mon = int(d[self[int(b)][1]])
    tm_mday = int(self[int(b)][2])
    tm_hour = int(a[0])
    tm_min = int(a[1])
    tm_sec = int(a[2])
    tm_wday = int() 
    tm_yday = int() 
    tm_isdst = int()
    t = (tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst)
    e = time.mktime(t)
    return(e)

#c = dict()

#for i in a:
for i in a1:
    #print(i)
    ii = i.split()
    if len(ii) == 16:
        #print(ii)
        #d1 = ' '.join(ii[4:9]) 
        d1 = ii[4:9] 
        #d2 = ' '.join(ii[10:15]) + ii[-1]
        d2 = ii[10:15]
        #a1 = pr(d1,1) 
        self = [ d1, d2 ] 
        #a1 = pt(self,1) 
        a1 = pt(self,0) 
        #a2 = pr(d1,2) 
        #a2 = pt(self,2) 
        a2 = pt(self,1) 
        #print(d1, d2)
        #print(d1, d2, a1, a2)
        year = int(ii[8])
        month = int(d[ii[5]])
        day = int(ii[6]) 
        c1 = datetime.date(year,month,day)
        c2 = c1.isocalendar()
        #c[str(c2[1])] = [] 
        a3 = int(a2) - int(a1)
        if c2[1] != 53:
            #print(c2)
            c[str(c2[1])].append([ ' '.join(d1), ' '.join(d2), a3 ])
        #print(d1, d2, int(a1), int(a2))

#print(pprint.pprint(c))

a = 1
#for j,i in enumerate(c[str(50)]):

#a2 = sys.argv[2]
def rstr(e):

    #for j,i in enumerate(c[str(49)]):
    #for j,i in enumerate(c[str(sys.argv[2])]):
    #for j,i in enumerate(c[str(sys.argv[2])]):
    for j,i in enumerate(c[str(e)]):
        a = j - 1 
        self = [ i[0].split(), i[1].split() ]
        a1 = pt(self,1)
        a2 = [] 
        #if c[str(50)][j][1] == c[str(50)][a][1]:
        #if c[str(49)][j][1] == c[str(49)][a][1]:
        #if c[str(sys.argv[2])][j][1] == c[str(sys.argv[2])][a][1]:
        if c[str(e)][j][1] == c[str(e)][a][1]:
            #print("Ja", c[str(50)][j][1], c[str(50)][j][2] )
            #print("Ja", c[str(49)][j][1], c[str(49)][j][2] )
            #if c[str(49)][a][2] <= c[str(49)][j][2]:
            #if c[str(sys.argv[2])][a][2] <= c[str(sys.argv[2])][j][2]:
            if c[str(e)][a][2] <= c[str(e)][j][2]:
                #c.remove(c[str(49)][a][2])
                #print("JA",c[str(49)][a][2])
                #print("JA",c[str(sys.argv[2])][a][2])
                #c[str(49)].remove(c[str(49)][a])
                #c[str(sys.argv[2])].remove(c[str(sys.argv[2])][a])
                c[str(e)].remove(c[str(e)][a])
            else:
                #c.remove(c[str(49)][a][2])
                #print("JaA",c[str(49)][j][2])
                #print("JaA",c[str(sys.argv[2])][j][2])
                #c[str(49)].remove(c[str(49)][j])
                #c[str(sys.argv[2])].remove(c[str(sys.argv[2])][j])
                c[str(e)].remove(c[str(e)][j])
     
        #print(j,i,int(a1))

#print('\n\n')
#for j,i in enumerate(c[str(49)]):
#    print(j,i) 


def prwk(self):

    cc = []
    #for i in c[str(49)]:
    #for i in c[str(sys.argv[2])]:
    for i in c[str(self)]:
        #cc.append(i[1])
        cc.append(i)

    
    d1 = dict()
    cnt = 0
    for i in cc:
        #for ii in c[str(49)]:
        #for ii in c[str(sys.argv[2])]:
        for ii in c[str(self)]:
            #print(ii,cc.count(ii))
            if i[1] == ii[1] :
                cnt += 1
                d1[str(ii)] = cnt
        cnt = 0 

    #print(pprint.pprint(d1))
    d2 = sorted(d1.values())
    #print(d2[-1])
    try:
        d3 = d2[-1]
    except IndexError:
        d3 = int() 
        #next

    #for i in range(1,3):
    if d3 >= 1:
        for i in range(1,d3):
            #rstr(c[sys.argv[2]])
            #rstr(c[str(self)])
            e = str(self)
            rstr(e)
    else:
        e = str(self)
        rstr(e)

    #pprint.pprint(c[sys.argv[2]])
    #pprint.pprint(c[str(self)])

    tt = int() 

    #a4 = c[sys.argv[2]][-1][0][0:10] 
    if len(c[str(self)]) > 0: 
        a4 = c[str(self)][-1][0][0:10] + c[str(self)][-1][0][19:24]
        #a5 = c[sys.argv[2]][0][1][0:10] 
        a5 = c[str(self)][0][1][0:10] + c[str(self)][0][1][19:24] 

    #for i in c[sys.argv[2]]:
        for i in c[str(self)]:
            tt += int(i[2]) 
  
    #print("Ja","Week:",",", sys.argv[2],",",a4," - ",a5,",", "loginduur:", "{0:.2f}".format((int(tt)/60/60)))
        #print("Ja","Week:",",", self,",",a4," - ",a5,",", "loginduur:", "{0:.2f}".format((int(tt)/60/60)))

        tt1 = "{0:.2f}".format((int(tt)/60/60))
        tt2 = str(tt1).split(".")
        tt3 = "0." + tt2[1]
        tt4 = float(tt3) * 60
        tt5 = int(tt4)
        tt6 = tt2[0] + "." + str(tt5)
        #print(tt6)
        #print("Week:",",", self,",",a4," - ",a5,",", "loginduur:", "{0:.2f}".format((int(tt)/60/60)))
        print("Week:",",", self,",",a4," - ",a5,",", "loginduur:", tt6)

if __name__ == '__main__':

    try:
        self = sys.argv[2]
        prwk(self)
    except IndexError:
        for i in c.keys():
            self = i
            #print("Ja",i)
            prwk(self)

