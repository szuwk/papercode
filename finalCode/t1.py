import os
import pandas as pd
def eachFile(filepath,fileName):
    pathDir = os.listdir(filepath)
    newDir = os.path.join(filepath, fileName)
    if fileName not in pathDir:
        data =pd.DataFrame(columns=['1','2','3'])
        data.to_csv(newDir,sep='\t',index=False)
    else:
        print(fileName)
        data = pd.read_csv(newDir,sep='\t')
    return data
    #获取当前路径下的文件名，返回List
    # for s in pathDir:
    #     newDir=os.path.join(filepath,s)     #将文件命加入到当前文件路径后面
    #     if os.path.isfile(newDir):         #如果是文件
    #         if os.path.splitext(newDir)[1]==".txt":  #判断是否是txt
    #             readFile(newDir)
    #             count+=1#读文件
    #             pass
    #     else:
    #         eachFile(newDir)
a = eachFile('./','wwwwghhjfgjgjww.txt')
print(a)