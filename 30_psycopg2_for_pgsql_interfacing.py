'''
Using psycopg2 module to interface with a postgreSQL database
pip install psycopg2
'''
# %%
# import psycopg2 module
import pandas as pd
import datetime as dt
import psycopg2

# get these variables from some config mechanism so that connection is not exposed and hardcoded
hostStr = 'x.x.x.x'
dbStr = 'hrd_training'
uNameStr = 'hrd_training'
dbPassStr = 'hrd#456'

# %%
# push data into a postgreSQL database

# create a connection object
conn = psycopg2.connect(host=hostStr, dbname=dbStr,
                        user=uNameStr, password=dbPassStr)

# get a cursor object from the connection
cur = conn.cursor()

# create sql for insertion
dataInsertionTuples = [
    ('util1', '2020-07-01 00:00:00.000', 25, 'urs', 102.5),
    ('util2', '2020-07-02 00:00:00.000', 26, 'sced', 50.7)
]
dataText = ','.join(cur.mogrify('(%s,%s,%s,%s,%s)', row).decode(
    "utf-8") for row in dataInsertionTuples)

sqlTxt = 'INSERT INTO public.schedules(\
        	sch_utility, sch_date, sch_block, sch_type, sch_val)\
        	VALUES {0} on conflict (sch_utility, sch_date, sch_block, sch_type) \
            do update set sch_val = excluded.sch_val'.format(dataText)

# execute the sql to perform insertion
cur.execute(sqlTxt)

# commit the changes
conn.commit()

# closing database connection and cursor
if(conn):
    # close the cursor object to avoid memory leaks
    cur.close()
    # close the connection object also
    conn.close()

# %%
# extract data from postgreSQL database

try:
    # get the connection object
    conn = psycopg2.connect(host=hostStr, dbname=dbStr,
                            user=uNameStr, password=dbPassStr)
    # get the cursor from connection
    cur = conn.cursor()
    # create the query
    postgreSQL_select_Query = "select sch_date + (15 * (sch_block-1) * interval '1 minute') as sch_time, \
        sch_val from public.schedules where sch_utility=%s and sch_type=%s \
            and sch_date between %s and %s order by sch_date, sch_block"

    # execute the query
    cur.execute(postgreSQL_select_Query,
                ('util1', 'urs', dt.datetime(2020, 7, 1), dt.datetime(2020, 7, 1)))

    # fetch all the records from cursor
    records = cur.fetchall()

    # get the column names returned from the query
    colNames = [row[0] for row in cur.description]

    # create a dataframe from the fetched records
    records = pd.DataFrame.from_records(records, columns=colNames)
    # =============================================================================
    # iterate through all the fetched records
    # for rowIter in range(records.shape[0]):
    #   print("datetime = ", records['sch_time'].iloc[rowIter])
    #   print("value = ", records['sch_val'].iloc[rowIter])
    # =============================================================================
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
    records = 0
finally:
    # closing database connection and cursor
    if(conn):
        # close the cursor object to avoid memory leaks
        cur.close()
        # close the connection object also
        conn.close()

# %%
