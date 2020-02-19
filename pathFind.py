import math
import mysql.connector

menArray=[[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
stationArray=[[],[],[],[],[],[]]
stationList=[]
#my map is 0,1,2 align from that 3 and 4 are separate lines

#menArray[0][1]=[0,1]
#menArray[0][3]=[0,2,3]
menArray[1][1]=[1]
menArray[1][2]=[1,2]
menArray[1][3]=[1,3]
menArray[1][4]=[1,3,4]
menArray[2][2]=[2]
menArray[2][4]=[2,3,4]
menArray[3][3]=[3]
menArray[3][4]=[1,2,3,4]
menArray[4][4]=[1,2,3]

mydb = mysql.connector.connect(
  host="sql12.freemysqlhosting.net",
  user="sql12322378",
  passwd="dBbRczdtnt",
  database="sql12322378"
)

mycursor = mydb.cursor()

mycursor.execute("select MENCode, S_Name from station")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0]," ",end="")
  
print()

 
  ###########################################################
  
  
def setstationList():   #ffill stationList Array from data
  mycursor.execute("select MENCode from station")
  dbresult = mycursor.fetchall()
  for x in dbresult:
    y=math.floor(int(x[0])/10000)
    stationArray[y].append(int(x[0]))
    
setstationList()

def MFind(start, end):
  startMen=math.floor(start/10000);
  endMen=math.floor(end/10000);
  return [startMen,endMen];



def findRegionMap(start,end):
  men=MFind(start, end)
  return menArray[men[0]][men[1]];
    
#findRegionMap(11000,27000)


def findMiddleStations(start,end):
    #stationList=new Array();
    regions = findRegionMap(start,end)  #the region map is stored in the regions variable as a list.
    if(len(regions)>1):                                                              #if more than one region exists
        fetchStations(start,stationArray[regions[0]][len(stationArray[regions[0]])-1]);   ##changed first index 1 to 0                               #fetch stations in first region
        for i in range(1 , len(regions)-1 ):  #fetch all stations in middle region
          fetchStations(stationArray[regions[i]][0],stationArray[regions[i]][len(stationArray[regions[i]])-1]);  
          
        fetchStations(stationArray[regions[len(regions)-1]][0],end);

    else:                                                                             #if a journey within one region
        fetchStations(start,end)
    
    return stationList;

def indexOf(station):
    m=math.floor(station/10000)
    for i in range(0 ,len(stationArray[m])):
      if(stationArray[m][i]==station):
        return i
    return 0;



def fetchStations(startStation,endStation):
  flag=0; stationListTemp=[];
  if(startStation>endStation):
        temp=startStation
        startStation=endStation
        endStation=temp
        flag=1
        
  for i in range (indexOf(startStation) , indexOf(endStation)+1):
      stationListTemp.append(stationArray[math.floor(startStation/10000)][i])
  if(flag==1):
    stationListTemp=stationListTemp.reverse()
  for x in stationListTemp:
    stationList.append(x)
    

#fetchStations(21000,41000);
#print(indexOf(10000))
findMiddleStations(41000,10000)
print(stationList)
def pathFind(startStation,EndStation):
  findMiddleStations(startStation,EndStation)
  return stationList