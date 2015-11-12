state = 'FL'
projtype = 'Solar'
tech = 'SolarPv'
projcost = 20000
eul = 18
size = 50
sizeunit = 'kW'
sector = 'Commercial'
electricbill = 20000
gasbill = 15000
savings = 60000
#End test values

ProgCat = {1:'RevolvingLoan', 2:'CreditEnhancedPrivateLoan',3:'PACE',4:'OnBillRepayment',5:'EnergyEfficientMortgage',6:'PerformanceContracting',7:'Rebates',8:'PPAOrSolarLease',9:'HUDPowerSaver'}
ProgCat = {value:key for key,value in ProgCat.items() }
Sect = {1:'Commercial', 2:'Residential', 3:'Public', 4:'NonProfit'}
Sect = {value:key for key,value in Sect.items() }

import mysql.connector
conn=mysql.connector.connect(user='root',password='!zozo9280',host='localhost',database='DecisionTool')
mycursor=conn.cursor()


def PaceLocale(state):
    mycursor.execute("""SELECT * FROM ProgLocale where ProgCat_ID = 3 and State LIKE '%{state}%'""".format(state = state))
    locale = mycursor.fetchall()
    if len(locale)== 0:
        del ProgCat['PACE']
        return ProgCat
    else:
        return ProgCat
pacelocale = PaceLocale(state)

def PpaLocale(state):
    mycursor.execute("""SELECT * FROM ProgLocale where ProgCat_ID = 8 and isEligible = 0 and State LIKE '%{state}%'""".format(state = state))
    locale = mycursor.fetchall()
    if len(locale)> 0:
        del ProgCat['PPAOrSolarLease']
        return ProgCat
    else:
        return ProgCat
ppalocale = PpaLocale(state)

def ProjCheck(projtype):
    mycursor.execute("""SELECT Distinct ProgCatId FROM FinProg where Tech LIKE '%{projtype}%'""".format(projtype = projtype))
    typecheck = mycursor.fetchall()
    for i in ProgCat:
        if i in typecheck:
            return i
projcheck = ProjCheck(projtype)

def SectorCheck(sector):	
    mycursor.execute("""SELECT DISTINCT ProgCatId FROM FinProg WHERE Sector LIKE '%{sector}%'""".format(sector = sector))
    sectcheck = [mycursor.fetchall()]
    for sector in ProgCat:
        if sector in sectcheck:
            return i
sectorcheck = SectorCheck(sector)
