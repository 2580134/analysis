import pandas as pd  #引入模块

def transform(excel):
   data = pd.read_excel(excel) #读取文件
   data1 = data.iloc[:, 0:5]  # 按位置取某五列
   #print(data1)
   df = pd.DataFrame(data1) #转化数据
   #print(df)
   return df

def main():
   #data = ["2020-河北-文科.xls","2020-河北-理科.xls"]
   #for i in data:
      #df_new = transform(i)
      #print(i)
      #df_new.to_excel(i)#写入文档
   df_new = transform("2020-安徽-文科.xls")
   df_new.to_excel("2020-安徽-文科-整理.xls")#写入文档
   df_new = transform("2020-安徽-理科.xls")
   df_new.to_excel("2020-安徽-理科-整理.xls")  # 写入文档
   df_new = transform("2020-福建-文科.xls")
   df_new.to_excel("2020-福建-文科-整理.xls")  # 写入文档
   df_new = transform("2020-福建-理科.xls")
   df_new.to_excel("2020-福建-理科-整理.xls")  # 写入文档
   df_new = transform("2020-甘肃-文科.xls")
   df_new.to_excel("2020-甘肃-文科-整理.xls")  # 写入文档
   df_new = transform("2020-甘肃-理科.xls")
   df_new.to_excel("2020-甘肃-理科-整理.xls")  # 写入文档
   df_new = transform("2020-广东-文科.xls")
   df_new.to_excel("2020-广东-文科-整理.xls")  # 写入文档
   df_new = transform("2020-广东-理科.xls")
   df_new.to_excel("2020-广东-理科-整理.xls")  # 写入文档
   df_new = transform("2020-广西-文科.xls")
   df_new.to_excel("2020-广西-文科-整理.xls")  # 写入文档
   df_new = transform("2020-广西-理科.xls")
   df_new.to_excel("2020-广西-理科-整理.xls")  # 写入文档
   df_new = transform("2020-贵州-文科.xls")
   df_new.to_excel("2020-贵州-文科-整理.xls")  # 写入文档
   df_new = transform("2020-贵州-理科.xls")
   df_new.to_excel("2020-贵州-理科-整理.xls")  # 写入文档
   df_new = transform("2020-河北-文科.xls")
   df_new.to_excel("2020-河北-文科-整理.xls")  # 写入文档
   df_new = transform("2020-河北-理科.xls")
   df_new.to_excel("2020-河北-理科-整理.xls")  # 写入文档
   df_new = transform("2020-河南-文科.xls")
   df_new.to_excel("2020-河南-文科-整理.xls")  # 写入文档
   df_new = transform("2020-河南-理科.xls")
   df_new.to_excel("2020-河南-理科-整理.xls")  # 写入文档
   df_new = transform("2020-黑龙江-文科.xls")
   df_new.to_excel("2020-黑龙江-文科-整理.xls")  # 写入文档
   df_new = transform("2020-黑龙江-理科.xls")
   df_new.to_excel("2020-黑龙江-理科-整理.xls")  # 写入文档
   df_new = transform("2020-湖北-文科.xls")
   df_new.to_excel("2020-湖北-文科-整理.xls")  # 写入文档
   df_new = transform("2020-湖北-理科.xls")
   df_new.to_excel("2020-湖北-理科-整理.xls")  # 写入文档
   df_new = transform("2020-湖南-文科.xls")
   df_new.to_excel("2020-湖南-文科-整理.xls")  # 写入文档
   df_new = transform("2020-安湖南-理科.xls")
   df_new.to_excel("2020-湖南-理科-整理.xls")  # 写入文档
   df_new = transform("2020-吉林-文科.xls")
   df_new.to_excel("2020-吉林-文科-整理.xls")  # 写入文档
   df_new = transform("2020-吉林-理科.xls")
   df_new.to_excel("2020-吉林-理科-整理.xls")  # 写入文档
   df_new = transform("2020-江西-文科.xls")
   df_new.to_excel("2020-江西-文科-整理.xls")  # 写入文档
   df_new = transform("2020-江西-理科.xls")
   df_new.to_excel("2020-江西-理科-整理.xls")  # 写入文档
   df_new = transform("2020-辽宁-文科.xls")
   df_new.to_excel("2020-辽宁-文科-整理.xls")  # 写入文档
   df_new = transform("2020-辽宁-理科.xls")
   df_new.to_excel("2020-辽宁-理科-整理.xls")  # 写入文档
   df_new = transform("2020-内蒙古-文科.xls")
   df_new.to_excel("2020-内蒙古-文科-整理.xls")  # 写入文档
   df_new = transform("2020-内蒙古-理科.xls")
   df_new.to_excel("2020-内蒙古-理科-整理.xls")  # 写入文档
   df_new = transform("2020-宁夏-文科.xls")
   df_new.to_excel("2020-宁夏-文科-整理.xls")  # 写入文档
   df_new = transform("2020-宁夏-理科.xls")
   df_new.to_excel("2020-宁夏-理科-整理.xls")  # 写入文档
   df_new = transform("2020-青海-文科.xls")
   df_new.to_excel("2020-青海-文科-整理.xls")  # 写入文档
   df_new = transform("2020-青海-理科.xls")
   df_new.to_excel("2020-青海-理科-整理.xls")  # 写入文档
   df_new = transform("2020-山西-文科.xls")
   df_new.to_excel("2020-山西-文科-整理.xls")  # 写入文档
   df_new = transform("2020-山西-理科.xls")
   df_new.to_excel("2020-山西-理科-整理.xls")  # 写入文档
   df_new = transform("2020-陕西-文科.xls")
   df_new.to_excel("2020-陕西-文科-整理.xls")  # 写入文档
   df_new = transform("2020-陕西-理科.xls")
   df_new.to_excel("2020-陕西-理科-整理.xls")  # 写入文档
   df_new = transform("2020-四川-文科.xls")
   df_new.to_excel("2020-四川-文科-整理.xls")  # 写入文档
   df_new = transform("2020-四川-理科.xls")
   df_new.to_excel("2020-四川-理科-整理.xls")  # 写入文档
   df_new = transform("2020-云南-文科.xls")
   df_new.to_excel("2020-云南-文科-整理.xls")  # 写入文档
   df_new = transform("2020-云南-理科.xls")
   df_new.to_excel("2020-云南-理科-整理.xls")  # 写入文档
   df_new = transform("2020-重庆-文科.xls")
   df_new.to_excel("2020-重庆-文科-整理.xls")  # 写入文档
   df_new = transform("2020-重庆-理科.xls")
   df_new.to_excel("2020-重庆-理科-整理.xls")  # 写入文档
main()

# import pandas as pd  #引入模块
#
# data = pd.read_excel("2020-河北-文科.xls") #读取文件
# data1 = data.iloc[:, 0:5]  # 按位置取某五列
# print(data1)
# df = pd.DataFrame(data1) #转化数据
#
# df.to_excel("2020-河北-文科-整理.xls") #写入文档
