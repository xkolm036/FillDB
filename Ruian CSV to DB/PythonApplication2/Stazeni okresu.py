import csv,operator,os
import pyodbc

class Geo(object):
   def __init__(self,Kod,nazevObce,statusObce,kodPOU,nazevPOU,kodORP,nazevORP,kodOkres,nazevOkresu,kodKraje,nazevKraje):
       self.Kod = Kod
       self.nazevObce = nazevObce
       self.statusObce = statusObce
       self.kodPOU = nazevPOU
       self.nazevPOU = NazevObce
       self.kodORP = kodORP
       self.nazevORP = nazevORP
       self.kodOkres = kodOkres
       self.nazevOkresu = nazevOkresu
       self.kodKraje = kodKraje
       self.nazevKraje = nazevKraje
 



os.chdir("D://regions")
#
#conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
#                     'Server=(localdb)\MSSQLLocalDB;'
#                     'Database=DP;'
#                    'Trusted_Connection=yes;')


connstr = (
    "DRIVER={PostgreSQL Unicode};"
    "DATABASE=Geography;"
    "UID=postgres;"
    "PWD=polav1994;"
    "SERVER=localhost;"
    "PORT=5432;"
    )


for file in os.listdir("./"): #
  
    file = open(file,newline='')
    csv1 = csv.reader(file)
    print("{} CityID: {} CytyPart: {} StreetId: {} HouseId: {}".format(file.name,cityId,cityPartId,StreetId,houseId));
    rows = []
    rows.clear()
    header = next(csv1)
    #Vytvorim si pole trid s jednotlivyma argumentama cvs
    for line in csv1:
        arg = str(line).split(";")
        radek = Geo(arg[0],arg[1],arg[2],arg[7],arg[8],arg[9],arg[10],arg[11])
        cursor.execute("INSERT into city(region) where number='?' VALUES(?)",radek.kod,radek.nazevOkresu)
 

    #Vytvorim mesto
    

                    

         
    cursor.commit()

cursor.close();
    
   

 
       



