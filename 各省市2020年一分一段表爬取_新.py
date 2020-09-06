import pandas as pd  #引入模块
import os
#file_path = "D:/test/test.py"
def transform(excel):
   data = pd.read_excel(excel) #读取文件
   data1 = data.iloc[:, 0:5]  # 按位置取某五列
   #print(data1)
   df = pd.DataFrame(data1) #转化数据
   #print(df)
   return df

def main():

   data = ["2020-安徽-文科.xls","2020-安徽-理科.xls","2020-福建-文科.xls","2020-福建-理科.xls","2020-甘肃-文科.xls","2020-甘肃-理科.xls",
           "2020-广东-文科.xls","2020-广东-理科.xls","2020-广西-文科.xls","2020-广西-理科.xls","2020-贵州-文科.xls","2020-贵州-理科.xls",
           "2020-河北-文科.xls","2020-河北-理科.xls","2020-河南-文科.xls","2020-河南-理科.xls","2020-黑龙江-文科.xls","2020-黑龙江-理科.xls",
           "2020-湖北-文科.xls","2020-湖北-理科.xls","2020-湖南-文科.xls","2020-湖南-理科.xls","2020-吉林-文科.xls","2020-吉林-理科.xls",
           "2020-江西-文科.xls","2020-江西-理科.xls","2020-辽宁-文科.xls","2020-辽宁-理科.xls","2020-内蒙古-文科.xls","2020-内蒙古-理科.xls",
           "2020-宁夏-文科.xls","2020-宁夏-理科.xls","2020-青海-文科.xls","2020-青海-理科.xls","2020-山西-文科.xls","2020-山西-理科.xls",
           "2020-陕西-文科.xls","2020-陕西-理科.xls","2020-四川-文科.xls","2020-四川-理科.xls","2020-云南-文科.xls","2020-云南-理科.xls",
           "2020-重庆-文科.xls","2020-重庆-理科.xls"]
   for i in data:
      #df_new = transform(i)
      print(i)
      file_path = "E:/课程设计/2020-2021-1数据采集课设/高考数据分析/各省高考一分一段表数据/文理科省市/" + i #获得文件路径
      df_new = transform(file_path)
      (filepath, tempfilename) = os.path.split(file_path)
      (filename, extension) = os.path.splitext(tempfilename)  #获得文件名和扩展名
      filename_new = filename + "-整理" + extension #修改文件名
      df_new.to_excel("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/各省高考一分一段表汇总/文理科省市/" + filename_new)#写入文档

main()

