#!/usr/bin/python3
#
# Een nieuw script om de totalen van de uren per week dat de computer aanstond te tonen.
# A new script to show the total number of hours the computer was on per week.
# Werkt op een ubuntu werkstation.
# Works on a ubuntu worstation.
#
# ./pwrt-local.py 
# ./pwrt-local.py 'weeknumber'
#
 
import os,sys
import time
import datetime
import pprint  
import subprocess 

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

def print_mijndate():
   from time import gmtime, strftime
   date = strftime("%Y%m%d.%H%M%S")
   return(date)

def gt(): 
    cmd = [ "/usr/bin/last", "-F" ] 
    output = subprocess.check_output(cmd)
    t = output.decode() 
    t1 = print_mijndate()  
    t2 = "/tmp/" + t1 + ".login_sessions.tct"
    t3 = open(t2, "w") 
    for i in t:
        t3.write(i) 
    t3.close()

def obt_b():
    import glob
    from operator import itemgetter
    a = glob.glob("/tmp/*login_sessions*") 
    b = [] 
    for i in a:
        ii = i.split(".")
        #print("Ja",ii)
        if ii[-2] == 'login_sessions': 
            b.append(ii) 
    c = sorted(b, key=itemgetter(0,1), reverse=True)
    return('.'.join(c[0]))


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


try:
    gt()
    a1 = open(obt_b(), "r")
except IndexError:
    print("    ./pwrt-local.py")
    print("    ./pwrt-local.py 'weeknumber'")
    sys.exit()


for i in a1:
    ii = i.split()
    if len(ii) == 16:
        d1 = ii[4:9] 
        d2 = ii[10:15]
        self = [ d1, d2 ] 
        a1 = pt(self,0) 
        a2 = pt(self,1) 
        year = int(ii[8])
        month = int(d[ii[5]])
        day = int(ii[6]) 
        c1 = datetime.date(year,month,day)
        c2 = c1.isocalendar()
        a3 = int(a2) - int(a1)
        if c2[1] != 53:
            c[str(c2[1])].append([ ' '.join(d1), ' '.join(d2), a3 ])

print("Ja",c)

a = 1

def rstr(e):

    for j,i in enumerate(c[str(e)]):
        a = j - 1 
        self = [ i[0].split(), i[1].split() ]
        a1 = pt(self,1)
        a2 = [] 
        if c[str(e)][j][1] == c[str(e)][a][1]:
            if c[str(e)][a][2] <= c[str(e)][j][2]:
                c[str(e)].remove(c[str(e)][a])
            else:
                c[str(e)].remove(c[str(e)][j])


def prwk(self):

    cc = []
    for i in c[str(self)]:
        cc.append(i)

    
    d1 = dict()
    cnt = 0
    for i in cc:
        for ii in c[str(self)]:
            if i[1] == ii[1] :
                cnt += 1
                d1[str(ii)] = cnt
        cnt = 0 

    d2 = sorted(d1.values())
    
    try:
        d3 = d2[-1]
    except IndexError:
        d3 = int() 

    if d3 >= 1:
        for i in range(1,d3):
            e = str(self)
            rstr(e)
    else:
        e = str(self)
        rstr(e)

    tt = int() 

    t2 = []
    if len(c[str(self)]) > 0: 
        a4 = c[str(self)][-1][0][0:10] + c[str(self)][-1][0][19:24]
        a5 = c[str(self)][0][1][0:10] + c[str(self)][0][1][19:24] 

        for i in c[str(self)]:
            tt += int(i[2]) 
  
        tt1 = "{0:.2f}".format((int(tt)/60/60))
        #print("JaAAA",tt1)
        tt2 = str(tt1).split(".")
        tt6 = '' 
        if int(tt2[1]) >= 60:
            tt3 = int(tt2[1]) - 60
            tt4 = int(tt2[0]) + 1
            tt6 = str(tt4) + "." + str(tt3) 
        else:
            tt6 = tt1
             
        #tt5 = int(tt4)
        #print("Jaa",tt5)
        #try:
        #print("JaA",len(str(tt5)))
        #    if len(str(tt5)) == 1:
        #        tt6 = tt2[0] + '.' +  '0' + str(tt5) 
        #    else:
        #tt6 = tt2[0] + "." + str(tt5)
        #        tt6 = tt2[0] + "." + str(tt5)

        t1 = "{0:.2f}".format((float(tt6)/7))
        #print("Jaaaa",round(float(t1),2))
        t3 = t1.split(".") 
        t3_3 = '' 
        if int(t3[1]) >= 60:
            t3_1 = int(t3[1]) - 60
            t3_2 = int(t3[0]) + 1
            t3_3 = str(t3_2) + "." + str(t3_1) 

        #print("JA", t3_3)

        if t3_3 != '': 
            t2.append([ self, a4, a5, "{0:.2f}".format(float(tt6)), t3_3 ] ) 
        else:
            t2.append([ self, a4, a5, "{0:.2f}".format(float(tt6)), t1 ] ) 
    
    print("ja",t2)
        

if __name__ == '__main__':

    try:
        #self = sys.argv[2]
        self = sys.argv[1]
        prwk(self)
    except IndexError:
        print("jaA:","Weeknumber,week startdate,week enddate,total hours,average daily hours") 
        for i in c.keys():
            self = i
            #print("Ja",i)
            prwk(self)

