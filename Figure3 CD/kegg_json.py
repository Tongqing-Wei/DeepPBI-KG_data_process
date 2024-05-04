import json
import re
with open("C:/Users/未同庆/Desktop/富集分析/ko00001.json","r") as f:    
    fj = f.read()    
    kojson = json.loads(fj)
    with open("C:/Users/未同庆/Desktop/富集分析/newKegg.tsv", "w") as k:    
        for i in kojson['children']:                
            ii = i['name'].replace(" ", "\t", 1)        
            for j in i['children']:                        
                jj = j['name'].replace(" ", "\t", 1)            
                for m in j['children']:                                
                    if re.findall(r"ko\d{5}",m['name']):                    
                        mm = "ko" + m['name'].replace(" ", "\t", 1)                
                    else :                    
                        mm = m['name'].replace(" ", "\t", 1)                
                    try :                    
                        for n in m['children']:                                                
                            if ";" in n['name']:                            
                                nn = n['name'].replace(" ", "\t", 1).replace("; ", "\t", 1)                        
                            else:                            
                                nn = n['name'].replace(" ", "\t \t", 1)                        
                            k.write(ii + "\t" + jj + "\t" + mm + "\t" + nn + "\n")                
                    except :                                        
                        nn = " \t \t "                    
                        k.write(ii + "\t" + jj + "\t" + mm + "\t" + nn + "\n")