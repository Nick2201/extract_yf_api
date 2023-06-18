import psycopg2
from sqlalchemy import ( create_engine,
    MetaData, Table,Column,
    String, DateTime,Integer,Text)
from sqlalchemy.orm import sessionmaker

dialect = 'postgresql'
unpack_conf = dialect + '://{user}:{password}@{host}:{port}/{database}'.format(**DB_CONFIG)

engine = create_engine(unpack_conf)

print(unpack_conf)


metadata = MetaData()

descriptive_info = Table (
    'descriptive_info', metadata,
    Column('id', Integer(), primary_key=True),
    Column('symbol', String(5)),
    Column('longName', String(100)),
    Column('sector', String(30)),
    Column('industry', String(50)),
    Column('country', String(80)),
    Column('longBusinessSummary', Text()),
    Column('fullTimeEmployees', Integer()),
    Column('website', Text()),
    Column('logo_url', Text()),
    Column('exchange', String(7)),
)

conn = engine.connect()
metadata.create_all(engine)