import csv,operator,os
import pyodbc

class Geo(object):
   def __init__(self,Kod,nazevObce,statusObce,kodPOU,nazevPOU,kodORP,nazevORP,kodOkres,nazevOkresu,kodKraje,nazevKraje):
       self.Kod = Kod
       self.nazevObce = nazevObce
       self.statusObce = statusObce
       self.kodPOU = nazevPOU
       self.nazevPOU = nazevPOU
       self.kodORP = kodORP
       self.nazevORP = nazevORP
       self.kodOkres = kodOkres
       self.nazevOkresu = nazevOkresu
       self.kodKraje = kodKraje
       self.nazevKraje = nazevKraje
 



os.chdir("D:\\regions")
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
cursor = pyodbc.connect(connstr);


for file in os.listdir("./"): #
  
    file = open(file,newline='',encoding="UTF-8 ")
    csv1 = csv.reader(file)
    header = next(csv1)
  
    for line in csv1:
        arg = str(line).split(";");
        radek = Geo(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],arg[6],arg[7],arg[8],arg[9],arg[10]);
        radek.Kod=  str(radek.Kod).replace("['","");
        print("{} Vesnice: {} Okres: {} Kod: {}".format(file.name,radek.nazevObce,radek.nazevOkresu,radek.Kod));
        cursor.execute("UPDATE city SET region=? WHERE number=?;",radek.nazevOkresu,radek.Kod)
   
    #Vytvorim mesto
   

                    

         
    cursor.commit()

cursor.close();
    
   

 
       



