#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 08:41:11 2020

@author: msvmuthu
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:25:00 2020

@author: msvmuthu
"""

#Parameters
OAIR=2.5
SAIR=4
MAIR=4
BonusStopAge=55
ContStopAge=55
fullcontkickin=40
topupstopage=39
age=40

#current balance as of age 40
OA=853
SA=96654
MA=56661

#bonus proposition
OAB=5000
SAB=2200
MAB=2500

maturityage=55



topup=7000


while age<=maturityage:
   Q1=1
   while Q1<5:
        Q1OA=1260
        Q1SA=419
        Q1MA=539
        
        if age<fullcontkickin:
            Q1OA=0
            
            
        if age>ContStopAge:
            Q1OA=0
            Q1SA=0
            Q1MA=0
            
        Q1OA=(Q1OA*3)
        Q1SA=(Q1SA*3)
        Q1MA=(Q1MA*3)
        
        if age>topupstopage:
            topup=0
        
        if age>BonusStopAge:
            OAB=0
            SAB=0
            MAB=0
            #topup=0
        
        if age<fullcontkickin:
            OAB=0
            
        if (Q1==1):
            Q1OA=Q1OA+OAB
            Q1SA=Q1SA+SAB+topup
            Q1MA=Q1MA+MAB    
           
        if age>ContStopAge:
            print(str.format("no money {} {} {}", Q1OA,Q1SA,Q1MA))
            
        OA=OA+Q1OA
        SA=SA+Q1SA
        MA=MA+Q1MA
        
        print(str.format("{},{},{},{},{}",age,Q1,round(OA),round(SA),round(MA)))  
        Q1+=1
        
   OAI=((OA*OAIR)/100)
   SAI=((SA*SAIR)/100)
   #print(str.format("interest {}",SAI))
   MAI=((MA*MAIR)/100)
   OA=OA+OAI
   SA=SA+SAI
   MA=MA+MAI
   print(str.format("{},{},{},{},{}",age,Q1,round(OA),round(SA),round(MA)))     
   age+=1
total=OA+SA+MA
print(round(total))

#scenario 1: full until 55, OA contrib full from this year, no topup:1,055,687.0