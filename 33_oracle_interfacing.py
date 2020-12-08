'''
using cx_oracle module to bulk insert into oracle db
pip install cx_oracle
'''
# %%
# import cx_Oracle module
import cx_Oracle
import datetime as dt

# %%
# get this from some config mechanism so that connection is not exposed and hardcoded
# connection string format = <username>/<password>@<database_ip>/<database_service_name>
connStr = 'hrd_training/hrd#456@x.x.x.x:1521/ORCL'


# %%
## data rows insertion into oracle database table

# consider this as the data insertion rows, this might even have 1000 rows
dataInsertionTuples = [
    ('util1', dt.datetime(2020, 7, 1), 25, 'urs', 102.5),
    ('util2', dt.datetime(2020, 7, 2), 26, 'sced', 50.7)
]

# create a connection object
conn = cx_Oracle.connect(connStr)

# get a cursor object from the connection
cur = conn.cursor()

try:
    # create sql for deletion
    sqlTxt = "DELETE from hrd_training.schedules where\
                (sch_utility=:1) and (sch_date=:2)\
                and (sch_block=:3) and (sch_type=:4)"
    # execute the sql to perform deletion
    cur.executemany(sqlTxt, [x[:-1] for x in dataInsertionTuples])
    
    # create sql for insertion
    sqlTxt = "INSERT INTO hrd_training.schedules\
                (sch_utility, sch_date, sch_block, sch_type, sch_val)\
                VALUES (:1, :2, :3, :4, :5)"
    # execute the sql to perform insertion
    cur.executemany(sqlTxt, dataInsertionTuples)

    # commit the changes
    conn.commit()
except Exception as err:
    print('Error while bulk insert into db')
    print(err)
finally:
    # closing database cursor and connection
    if cur is not None:
        cur.close()
    conn.close()

print('script execution done')

# %%
## data rows extraction from oracle database table example

# create a connection object
conn = cx_Oracle.connect(connStr)

# get a cursor object from the connection
cur = conn.cursor()

try:
    # create sql for querying data
    sqlTxt = "SELECT sch_utility, sch_date, sch_block, sch_type, sch_val\
                from hrd_training.schedules where sch_utility = :1"
    # execute the sql to perform data extraction
    cur.execute(sqlTxt, ("util1",))

    # get the column names returned from the query
    colNames = [row[0] for row in cur.description]

    # fetch all rows from query
    dbRows = cur.fetchall()
    
except Exception as err:
    print('Error while querying data from db')
    print(err)
finally:
    # closing database cursor and connection
    if cur is not None:
        cur.close()
    conn.close()
# %%
