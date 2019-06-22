from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///C:/webDev/pycharm/matchmaker/data/my_sqlite_db.db')
connection = engine.connect()
print(engine.table_names())

metadata = MetaData()
mushroom_meta = Table('mushroom_db', metadata, autoload=True, autoload_with= engine)