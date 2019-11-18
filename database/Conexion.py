import sqlalchemy as db

engine = db.create_engine('postgresql://fbriones:fbriones@localhost/txt_speech')
connection = engine.connect()
metadata = db.MetaData()

print(connection)
class Connect():
    def init_db():
    Model.metadata.create_all(bind=engine)

    Model = declarative_base(name='Model')
    Model.query = db_session.query_property()    