import numpy as np
import pandas as pd
import xlrd

import pymssql
import sys
import os

from scipy import stats
from scipy.stats import ttest_ind
from scipy.stats import ttest_rel

import sklearn
from sklearn.model_selection import train_test_split


##### Pandas 直接读取 SQL Server 数据 
import pandas_profiling
sSql = "SELECT a.RPT_PERIOD_NAME_WEEK, "\
        "round(cast(sum(case when a.RESPONSE_VALUE in ('N') then 1 else 0 end) as float)/nullif(count(distinct(a.RSVP_POLL_ID)),0),6) as EDR,  "\
        "round(cast(sum(case when a.RESPONSE_VALUE = 'Y' then 1 else 0 end) as float)/nullif(sum(case when a.RESPONSE_VALUE in ('Y','N') then 1 else 0 end),0),4) as PRR  "\
        "FROM [oreport].[dbo].[prrcaserawdata] as a where  a.RPT_PERIOD_NAME_YEAR = '2019' and a.support_type = 'Seller' and substring(a.RPT_PERIOD_NAME_WEEK,11,2) != 36 "\
        "group by a.RPT_PERIOD_NAME_WEEK order by a.RPT_PERIOD_NAME_WEEK"  
conn = pymssql.connect(host='EC2AMAZ-N6JKUAF', server='MSSQLSERVER', port='1433', user='sa', password='Xyz@19821121', database='oreport', charset='utf8')
df = pd.read_sql(sSql, con=conn)
print(df)

# EDR = df.reindex(columns = ['EDR'])
# PRR = df.reindex(columns = ['PRR'])



exam_X = df.loc[:,"EDR"]
exam_y = df.loc[:,"PRR"]

X_train, X_test, y_train, y_test = train_test_split(exam_X, exam_y, train_size = .8)
print(exam_X.shape, X_train.shape, X_test.shape)

print("this is a testing file to compare with yours")
print("this is not a good guy")
print("this is your dreamcat")

# from sklearn.linear_model import LogisticRegression
# modle = LogisticRegression()
# modle.fit(X_train, y_train)
# a = modle.score(X_test, y_test)
# print(a)

print("good, this is god model")