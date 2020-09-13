import pandas as pd  #引入模块
import os
#file_path = "D:/test/test.py"
def transform(excel):
   data = pd.read_excel(excel,header=None) #读取文件
   data1 = data.iloc[:, 0:5]  # 按位置取某五列
   #print(data1)
   df = pd.DataFrame(data1) #转化数据
   df.dropna(axis=0, how='any', inplace=True)
   #print(df)
   return df

def main():

   data = ["2020-北京-不分科.xls","2020-海南-不分科.xls","2020-上海-不分科.xls","2020-天津-不分科.xls","2020-浙江-不分科.xls"]
   for i in data:
      #df_new = transform(i)
      print(i)
      file_path = "E:/课程设计/2020-2021-1数据采集课设/高考数据分析/各省高考一分一段表数据/不分科省市/" + i #获得文件路径
      df_new = transform(file_path)
      (filepath, tempfilename) = os.path.split(file_path)
      (filename, extension) = os.path.splitext(tempfilename)  #获得文件名和扩展名
      filename_new = filename + "-整理" + extension #修改文件名
      df_new.to_excel("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/各省高考一分一段表汇总/不分科省市/" + filename_new)#写入文档

main()

