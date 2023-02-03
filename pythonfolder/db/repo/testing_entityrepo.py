from db.models.testing_entity import Testing_entity
from db.session import get_session


def get_testing_entity():
    with get_session() as session:
        return session.query(Testing_entity).all()

def insert_testing_entity(testing_entity):
    with get_session() as session:
        session.add(testing_entity)
        session.commit()

def update_testing_entity(id, schema_testing_entity):
    with get_session() as session:
        testing_entity = session.get(Testing_entity, id)
        for key, value in schema_testing_entity.items():
            setattr(testing_entity, key, value)
        session.commit()

def delete_testing_entity(id):
    with get_session() as session:
        testing_entity = session.get(Testing_entity, id)
        session.delete(testing_entity)
        session.commit()
        
