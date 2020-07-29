'''
using cx_oracle module to bulk insert into oracle db
pip install cx_oracle
'''
# %%
# import cx_Oracle module
import cx_Oracle
import pandas as pd
import datetime as dt
import pandas as pd

# %%
# get this from some config mechanism so that connection is not exposed and hardcoded
connStr = ''
# create a connection object
conn = cx_Oracle.connect(connStr)

# %%
# insertion bacth size
rowBatchSize = 100

# consider this as the data insertion rows, this might even have 1000 rows
dataInsertionTuples = [
    ('asda', '2020-07-01 00:00:00.000', 25, 'urs', 102.5),
    ('khkjsdf', '2020-07-02 00:00:00.000', 26, 'sced', 50.7)
]

# get a cursor object from the connection
cur = conn.cursor()

try:
    for batchStartItr in range(0, len(dataInsertionTuples), rowBatchSize):
        # deive the endIterator of the batch
        # also avoid end index overflow by comparing with data array length
        batchEndItr = min(len(dataInsertionTuples)-1, batchStartItr+rowBatchSize-1)

        dataTextInSql = ','.join(['(\'{0}\',\'{1}\',{2},\'{3}\',{4})'.format(dataTup[0], dataTup[1], dataTup[2],
                                                                dataTup[3], dataTup[4]) for dataTup in dataInsertionTuples[batchStartItr: batchEndItr+1]])

        # create sql for insertion
        # you can also use UPSERT for updating existing data on conflict
        sqlTxt = 'INSERT INTO public.schedules(\
                    sch_utility, sch_date, sch_block, sch_type, sch_val)\
                    VALUES {0}'.format(dataTextInSql)

        # execute the sql to perform insertion
        cur.execute(sqlTxt)
except:
    print('Error while bulk insert into db')
finally:
    # closing database cursor and connection
    if cur is not None:
        cur.close()
    conn.close()