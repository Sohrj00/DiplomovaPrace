import pandas as pd
def _create_dataframe_from_csv(path):   
    #return pd.read_csv(path, sep=";", header=None, names=['id', 'subject','body', 'url'])
    return pd.read_csv(path)

content=_create_dataframe_from_csv("./Test3.csv")
##TADY MENIT
#TODO: nacist cele csv i s labelama, nedelat to ve vice slozkach
bodys=[]
subjects=[]
URLS=[]
labels=[]
for i,x in enumerate(content.get("Body").values): 
    bodys.append(x)
for i,x in enumerate(content.get("Subject").values): 
    subjects.append(x)
for i,x in enumerate(content.get("URLs").values): 
    URLS.append(x)
for i,x in enumerate(content.get("Label").values): 
    labels.append(x)
print(f"{len(bodys),len(subjects),len(labels)}")
#for x in labels:
 #   if((str(x)!="nan")):print(x)
#for i,x in enumerate(content.values):
 #   print(x[3])
  #  if(str(x[4]=="nan")):break

try:
    moznosti={1:"Ads",2:"Health",3:"Products",4:"Adult",5:"Extortion",6:"Phishing",7:"Dating",8:"Scams",9:"Finance",10:"Jobs",11:"Malware",12:"Chain Letters"}
    for i in range(len(bodys)):
        if(str(labels[i])=="nan"):
            if(bodys[i]==None or bodys[i]==""):continue
            print(bodys[i])
            user_input=str(input("$"))
            if "konec" in user_input:
                df=pd.DataFrame({'Subject':subjects,'Body':bodys,'Label':labels,'URLs':URLS})
                df.to_csv(index=True,path_or_buf="./Test3.csv")
                break
            elif "moznosti" in user_input:
                print(moznosti)
            elif "uloz" in user_input:
                df=pd.DataFrame({'Subject':subjects,'Body':bodys,'Label':labels,'URLs':URLS})
                df.to_csv(index=True,path_or_buf="./Test3.csv")
            else:
                labels[i]=moznosti[int(user_input)]
finally:
    df=pd.DataFrame({'Subject':subjects,'Body':bodys,'Label':labels,'URLs':URLS})
    df.to_csv(index=True,path_or_buf="./Test3.csv")         


