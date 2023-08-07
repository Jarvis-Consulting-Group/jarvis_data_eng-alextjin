from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import sys 

def find_company_info(host, port, username, password, database, table, out_file):
 engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# metadata = MetaData(bind=None)

#table_name = Table(
#    f'{table}', 
#    metadata, 
#    autoload=True, 
#    autoload_with=engine
#)
 
 sql = f'SELECT * FROM {table}'
 df = pd.read_sql(sql, con=engine)
 df.to_csv(f'{out_file}')

find_company_info(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])

