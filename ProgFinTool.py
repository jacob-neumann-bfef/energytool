'''
proj = raw_input('What type of energy project do you want to implement? ')
size = int(raw_input('What is the estimated size of the system? '))
sizeunit = raw_input('What unit is used in the system size? ')
eul = int(raw_input('What is the effective useful life of the project? '))
savings = int(raw_input('what are the estimated energy savings for the project? '))
eletriccost = int(raw_input('What is the estimated annual cost of electricity for the project site? '))
gascost = int(raw_input('What is the estimated annual cost of gas for the project? '))
'''
#test values
proj = 'solar'
size = 100
sizeunit = 'kW'
eul = 15
savings = 30000
electriccost = 20000
gascost = 5000
#End test values section
#END OF USER PROMPT INPUTS SECTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


import mysql.connector
conn=mysql.connector.connect(user='root',password='!zozo9280',host='localhost',database='DecisionTool')
mycursor=conn.cursor()
mycursor.execute("SELECT ProgCat_ID from FinProg where proj ")
print(mycursor.fetchall())