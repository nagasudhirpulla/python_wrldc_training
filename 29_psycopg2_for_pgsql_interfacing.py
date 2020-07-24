'''
Lesson 7 - Day 4 - using psycopg2 module to interface with a postgreSQL database
pip install psycopg2
'''
# %%
# import psycopg2 module
import pandas as pd
import datetime as dt
import psycopg2
import pandas as pd

# %%
# push data to a postgreSQL database
# create a connection object
conn = psycopg2.connect(host='localhost_or_ip', dbname='dbName',
                        user='db_username', password='db_password')

# get a cursor object from the connection
cur = conn.cursor()

# %%
# create sql for insertion
dataInsertionTuples = [
    ('asda', '2020-07-01 00:00:00.000', 25, 'urs', 102.5),
    ('khkjsdf', '2020-07-02 00:00:00.000', 26, 'sced', 50.7)
]
dataText = ','.join(cur.mogrify('(%s,%s,%s,%s,%s)', row).decode(
    "utf-8") for row in dataInsertionTuples)

sqlTxt = 'INSERT INTO public.schedules(\
        	sch_utility, sch_date, sch_block, sch_type, sch_val)\
        	VALUES {0} on conflict (sch_utility, sch_date, sch_block, sch_type) \
            do update set sch_val = excluded.sch_val'.format(dataText)

# %%
# execute the sql to perform insertion
cur.execute(sqlTxt)

# closing database connection and cursor
if(conn):
    cur.close()
    conn.close()

# %%
# get data from postgreSQL database

try:
    # get the connection object
    conn = psycopg2.connect(user="db_uname",
                            password="db_pass",
                            host="db_host",
                            port="db_post",
                            database="db_name")
    # get the cursor from connection
    cur = conn.cursor()
    # create the query
    postgreSQL_select_Query = "select sch_date + (15 * (sch_block-1) * interval '1 minute'), \
        sch_val from public.schedules where sch_utility=%s and sch_type=%s \
            and sch_date between %s and %s order by sch_date, sch_block"

    # execute the query
    cur.execute(postgreSQL_select_Query,
                ('schUtility', 'schType', 'startDate', 'endDate'))

    # fetch all the records from cursor
    records = cur.fetchall()
    # create a dataframe from the fetched records
    records = pd.DataFrame.from_records(records)
    # =============================================================================
    # iterate through all the fetched records
    # for row in records:
    #   print("datetime = ", row[0])
    #   print("value = ", row[1])
    # =============================================================================
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
    records = 0
finally:
    # closing database connection and cursor
    if(conn):
        cur.close()
        conn.close()
