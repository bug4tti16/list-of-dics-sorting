def comp(d1,d2,item,list):
  get1=int(d1.get(item))
  get2=int(d2.get(item))
  x=list
  if get1 > get2:
    x.append(d2)
    x.append(d1)
   else:
    x.append(d1)
    x.append(d2)
  return(x)

#csv 저장
def save(list,filename):
    keys=list[0].keys()
    with open(filename,'w',newline='') as output:
        dict_writer = csv.DictWriter(output,keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)


path = pathlib.Path(__file__)
parent= path.parent.parent
os.chdir(parent)

fname=open("user_list_RFID.csv",'r')
dataa=list(csv.DictReader(fname))
fname.close()
x=1
count=0
result=[]
complist=dataa

while True:
  if complist[x] is None:
    x=1
    count=0
    complist=result
  else:
    result=comp(complist[x],complist[x-1],"Num",complist)
    x=x+1
    count=count+1
  if count==0:
    break
  
  save(result,"user_list_RFID.csv")
  
