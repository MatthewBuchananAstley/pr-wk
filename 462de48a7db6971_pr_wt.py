#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-2.0
#
# Waarachtig een relatief eenvoudig script om snel per week van het jaar 
# de gewerkte uren van een gebruikersnaam te genereren.
# Er voor het gemak even vanuitgaand dat er tijdens die login 
# sessies echt gewerkt is.
# In mijn geval wel, je kunt nu teksten en ebooks kopen
# op astley.nl.
#
# Het script gebruikt daarvoor de output van het commando 'last -F'.
# De output daarvan is zo te verkrijgen: last -F > last.out 
#
# ./pr_wt.py 'last.out' 'jaar' 'weeknummer' 'gebruikersnaam' 
#
# for i in `seq 1 52` ; do ./pr_wt.py last.out 2020 $i username ; done   
#
# 2021 Matthew Buchanan Astley 
  
import os,sys
import datetime
#import ttt

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

#d = { 'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Okt' : 10, 'Nov' : 11, 'Dec' : 12 }
d = { 'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12 }

a14 = []
def prdat(self):
    
    d = []

    #print("Ja", c)
    #print("Ja", self)
    #c = self
    c = self[0]
    #sys.exit()
    #c1 = 1
    for j,i in enumerate(c):
    #for j,i in enumerate(self):
        #c1 = int() 
        #if j != 0:
        c1 = j - 1
        #else:
        #    c1 = 0 
        #c2 = j + 2
        #print("Ja, c1)
        #print("Ja", c1)
        #print("JA",c[c1][4])
        #print("JA",c[c1][5])
        #print("JA",c[c1][3])
        #print("JA",c[c1])
        #print("Ja",j,i)
        #print("Ja",c[c1][3],j,i)
        #print("Ja",c[c1][3],j,i[7])
        #print("Ja",c[c1][3],j,i[8])
        #print("Ja",c[c1][3],j,i[3])
        #print("Ja",c[c1][3],j,i[3],i[15])
        #print("Ja",c[c1][3],j,i[3],i[14])
        #print("Ja",c[c1][3],j,i[3],i[13])
        #print("Ja",c[c1][3],j,i[3],i[11])
        #print("Ja",c[c1][3],j,i[0][3],i[2])
        c2 = c[c1][0].split()
        c3 = i[0].split()
        c4 = i[1].split()
        c4_1 = c4[3].split(":")
        c5 = c[c1][1].split()
        #print("Ja",c[c1][3],j,i[0][3],i[2])
        #print("Ja",c2[3],j,i[0][3],i[2])
        #print("Ja",c2[3],j,i[0],i[2])
        #print("Ja",c2[3],j,c3[3],i[2])
        #a1 = c[c1][3].split(":")
        a1 = c2[3].split(":")
        #a2 = i[3].split(":")
        #a2 = i[0][3].split(":")
        a2 = c3[3].split(":")
        a3 = a1[0] + a1[1] 
        a4 = a2[0] + a2[1]

        a5 = c5[3].split(":")
        a5_1 = ''.join(a5) 
        a6 = ''.join(c4_1) 

        #print("a", a5_1, "b", a6)

        if a3 != a4:  
            #print("Ja",c[c1][3],j,i[3],i[10])
            #print("Ja",c[c1][3],j,i[3],i[8],i[10])
            #print("Ja",c2[3],j,i[0][3],i[0][8],i[10])
            #print("Ja",c2[3],j,c3[3],i[0][8],i[10])
            #if a5_1 > a6:  
            #if a5_1 < a6:  
            #print("Ja",c2[3],j,c3[3],c4[3],i[2])
            ###print("Ja e",c2[3],j,c3[3],c4[3],i[2])
            #a5 = i[10].strip("()")
            a5 = i[2].strip("()")
            a6 = a5.split(":")
            d.append(a6) 
            #print(a5)
        else:
            #print("Ja",c[c1][3],j,i[3])
            #print("Ja",c[c1][3],j,i[3],i[8])
            #print("Ja",c2[3],j,i[0][3],i[8])
            #if a5_1 < a6:
            #print("JAA",d.pop())
            #d.pop()
            #if a5_1 > a6:
            if a5_1 < a6:
                d.pop()
                e1 = i[2].strip("()")
                e2 = e1.split(":")
                #d.append(i[2])
                d.append(e2)
                ###print("Ja dubbel",c2[3],j,c3[3],c4[3],i[2])

        #print("Ja",c2)
        #print(c)
    #print(d)
    #sys.exit() 
    ##print(d)
    #a7 = ''
    a7 = int()
    a8 = int()
    for i in d:
        #print(i[0],1[1])
        #a += i[1]
        #a7 += i[1]
        #if a7 != 60:
        #a7 += int(i[1])
        a7 += int(i[0])
        a8 += int(i[1])
        #print(i[0],i[1])
        #print(i[0],a)
        ###print(i[0],a7)
    #print(a7,(a8 / 60))
    a13_1 = round(a8 / 60,2)
    #a9 = str(a8 / 60).split(".")
    a9 = str(a13_1).split(".") 
    #print("Ja", a9)
    a9_1 = str(0) + "." + str(a9[1])
    #print("Ja", (float(a9_1) * 60))
    a9_2 = float(a9_1) * 60
    a9_3 = str(a9_2).split(".")
    #print("Ja", a9_3)
    #print(a7,(a8 / 60))
    #a10 = a7 + int(a9[0])
    a10 = a7 + int(a9[0])
    #a11 = str(a10) + ":" + str(a9[1])
    #a13 = "{0:.2f}".format(int(a9[1])) 
    ##a11 = str(a10) + ":" + str(a9[1][0]) + str(a9[1][-1]) 
    #a11 = str(a10) + ":" + str(a9[1]) 
    #a12 = str(a10) + ":" + str(a9[1]) 
    ##a12 = str(a10) + ":" + str(a9_3[0]) 
    #a13 = str(a10) + ":" + str(a9[1][0:2]) 
    #a12_1 = a9[1]
    a12_1 = a9_3[0]
    a13 = str(a10) + ":" + str(a12_1) 
    #print(a7,a9)
    #print(a7,a11)
    #a12 = "{0:.2f}".format(a11)
    #print(self[2],self[1],a12)
    #print(self[2],self[1],a11)
    #a14 = []
    a14.append(a13)
    print(self[2],self[1],a13)
    return([self[2],self[1],a13]) 
    #print(self[2],self[1],a12)

#print(a14)
#print(d)

#for i in range(60,a7): 
#print(i[0],a7)


#j = ii[4].split(":")
#j = ii[3].split(":")
#jj = ii[7].split(":")
#jj = ii[8].split(":")
#print("Ja", j, jj) 
#print(j[0],j[1], jj[0],jj[1]) 
#c.append(j)
#print("Ja", j[0], j[1], c[0], c[1]) 
#if j[0] != c[0] and j[1] != c[0]: 
#print("Ja",ii)
#print(j)
 
for i in a1:
    #print(i)
    j = i.split()
    #if len(j) == 14:
    #print(len(j),j)
    #if len(j) == '14':
    #if len(j) == '15':
    #if len(j) = '15':
    #if len(j) == '15':
    if len(j) == 15:
        #print(j) 
        #b = j[3] + " " + j[4] + " " + j[5] + " " + j[6]
        #year = j[6]
        #year = int(j[6])
        year = int(j[7])
        month = int(d[j[4]])
        day = int(j[5])
        #c = datetime.date(year,month,day) 
        c1 = datetime.date(year,month,day) 
        #c1 = c.isocalendar()
        c2 = c1.isocalendar()
        b = j[3] + " " + j[4] + " " + j[5] + " " + j[6] + " " + j[7]
        #b1 = j[9] + " " + j[10] + " " + j[11] + " " + j[12]
        b1 = j[9] + " " + j[10] + " " + j[11] + " " + j[12] + " " + j[13]
        #print(j[0], " ",b,b1)
        #c[str(c2[1]].append( [ b, b1, j[15])  
        #c[str(c2[1])].append( [ b, b1, j[15])  
        #c[str(c2[1])].append( [ b, b1, j[15] ] )  
        #if j[0] == sys.argv[4]:
        #if j[0] == sys.argv[4] and j[8] == sys.argv[2]:
        #if j[0] == sys.argv[4] and j[9] == sys.argv[2]:
        if j[0] == sys.argv[4] and j[7] == sys.argv[2]:
            c[str(c2[1])].append( [ b, b1, j[14] ] )  
        #print(c1) 
        #print("Ja",c1[1]) 

##try:
c3 = sys.argv[2]
c4 = sys.argv[3]
#c = c[c4]
#c1 = c[c4]
#print("Ja", c3, c4) 
#print("Ja", c3, c4, c[c4]) 
#print("Ja", c[c4])
#ttt.prdat(c[c4])
#ttt.prdat(c[c4],c4,sys.argv[1])
#self = [ c[c4], c4, sys.argv[1] ] 
self = [ c[c4], c4, sys.argv[4] ] 
#ttt.prdat(self)
prdat(self)
#ttt.prdat(c[c])
#ttt.prdat(c[c1])
#print(c[c3])
#for i in c[c3]:
#for i in c[c4]:
##for j,i in enumerate(c[c4]):
    #ii = i.split()
    ##ii = i[0].split()
    #c1 = j - 1
    #a1 = c[c4][c1][3].split(":")
    #a2 = i[3].split(":")
    #a3 = a1[0] + a1[1]
    #a4 = a2[0] + a2[1]

    ##if ii[4] == c3:
    ##    print(i[0], " ",i[1], " ",i[2])
#except KeyError:
#except IndexError:
#print("Ja", "IndexError")
#print(c)

a1 = c.keys() 
#print(a1)
a2 = []
for i in a1:
    self = [ c[i], c4, sys.argv[4] ]
    #print(c[i])
    ii = prdat(self)
    a2.append(ii)

#print(a2)
a3 = []
a3_1 = int()
a3_2 = int()

for i in a2:
    #print(i[2])  
    ii = i[2].split(":")
    #print(ii)
    #a3_1 += ii[0]
    if int(ii[0]) != 0 and int(ii[1]) != 0:
        a3_1 += int(ii[0])
    #a3_2 += ii[2]
        #a3_2 += int(ii[2])
        a3_2 += int(ii[1])

#print("Ja",a3_1,a3_2)

#a3_3 = float(a3_2) * 60  
#a3_3 = float(a3_2) / 60  
a3_3 = round(float(a3_2) / 60, 2)  
a3_4 = str(a3_3).split(".")
a3_5 = a3_1 + int(a3_4[0]) 

a3_6 = '0.' + a3_4[1]
#a3_7 = int(a3_6) * 60
#a3_7 = round(float(a3_6) * 60,0)
a3_7 = round(float(a3_6) * 60)
#a3_7 = round(int(a3_6) * 60,0)

#print("Ja", a3_1)
#print("JA", a3_2)
#print("JAA", a3_3)
#print("JAAA", a3_7)
#print("Ja", a3_5)
#a3_8 = a3_5 + "." + a3_7
a3_8 = str(a3_5) + "." + str(a3_7)
#a3_9 = int(a3_8) / 60
#a3_9 = float(a3_8) / 60
#a3_9 = float(a3_8) / 12 
a3_9 = round(float(a3_8) / 12,2) 
a3_10 = round(float(a3_9) / 4,2) 
#print("JA", a3_8)
#print("Uren ", a, a3_8)
print("Uren ", c3, a3_8)
print("Uren per maand ", c3, a3_9)
print("Uren per week ", c3, a3_10)
