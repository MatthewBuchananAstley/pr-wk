#!/usr/bin/python3
  
import os,sys
import datetime

a = sys.argv[1]
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

a14 = []
def prdat(self):
    
    d = []

    c = self[0]
    for j,i in enumerate(c):
        c1 = j - 1
        c2 = c[c1][0].split()
        c3 = i[0].split()
        c4 = i[1].split()
        c4_1 = c4[3].split(":")
        c5 = c[c1][1].split()
        a1 = c2[3].split(":")
        a2 = c3[3].split(":")
        a3 = a1[0] + a1[1] 
        a4 = a2[0] + a2[1]

        a5 = c5[3].split(":")
        a5_1 = ''.join(a5) 
        a6 = ''.join(c4_1) 

        if a3 != a4:  
            a5 = i[2].strip("()")
            a6 = a5.split(":")
            d.append(a6) 
        else:
            if a5_1 < a6:
                d.pop()
                e1 = i[2].strip("()")
                e2 = e1.split(":")
                d.append(e2)

    a7 = int()
    a8 = int()
    for i in d:
        a7 += int(i[0])
        a8 += int(i[1])
#    print("Ja", a7, a8) 
    if a8 > 60:
        a13_1 = round(a8 / 60,2)
    #else:
    #    a13_1 = a8
        a9 = str(a13_1).split(".") 
        a9_1 = str(0) + "." + str(a9[1])
        a9_2 = float(a9_1) * 60
        a9_3 = str(a9_2).split(".")
        a10 = a7 + int(a9[0])
        a12_1 = a9_3[0]
        a13 = str(a10) + ":" + str(a12_1) 
        a14.append(a13)
        print(self[2],self[1],a13)
        return([self[2],self[1],a13]) 
    else:
        a13_1 = a8
        a13 = str(0) + ":" + str(a13_1)
        print(self[2],self[1],a13)
        return([self[2],self[1],a13]) 
        

for i in a1:
    j = i.split()
    if len(j) == 15:
        year = int(j[7])
        month = int(d[j[4]])
        day = int(j[5])
        c1 = datetime.date(year,month,day) 
        c2 = c1.isocalendar()
        b = j[3] + " " + j[4] + " " + j[5] + " " + j[6] + " " + j[7]
        b1 = j[9] + " " + j[10] + " " + j[11] + " " + j[12] + " " + j[13]
        if j[0] == sys.argv[4] and j[7] == sys.argv[2]:
            c[str(c2[1])].append( [ b, b1, j[14] ] )  

#print(c)

c3 = sys.argv[2]
c4 = sys.argv[3]
#print(c[c4])

##for j,i in enumerate(c[c4]):
##    print(c[c4][j][2])

##self = [ c[c4], c4, sys.argv[4] ] 
##prdat(self)
##sys.exit()

a1 = c.keys() 
a2 = []
for i in a1:
    #self = [ c[i], c4, sys.argv[4] ]
    self = [ c[i], i, sys.argv[4] ]
    ii = prdat(self)
    a2.append(ii)

a3 = []
a3_1 = int()
a3_2 = int()

cnt = 0
for i in a2:
    if i[2] != '0:0':
        ii = i[2].split(":")
        cnt += 1
        a3_1 += int(ii[0])
        a3_2 += int(ii[1])

#print("Ja cnt", cnt)
a3_3 = round(float(a3_2) / 60, 2)  
a3_4 = str(a3_3).split(".")
a3_5 = a3_1 + int(a3_4[0]) 

a3_6 = '0.' + a3_4[1]
a3_7 = round(float(a3_6) * 60)

a3_8 = str(a3_5) + "." + str(a3_7)
a3_9 = round(float(a3_8) / 12,2) 
a3_10 = round(float(a3_9) / 4,2) 
a3_11 = round(float(a3_8) / cnt,2)
print("Uren ", c3, a3_8)
print("Uren per maand ", c3, a3_9)
print("Gemiddeld aantal uur per week op basis van de gewerkte weken", "("+ str(cnt) + ")", c3, a3_11)
