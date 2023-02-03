from schema import testing_entity as SchemaTesting_entity
from db.models.testing_entity import Testing_entity
from db.repo import testing_entityrepo


def fetch_testing_entity():
    return testing_entityrepo.get_testing_entity()

def insert_testing_entity(schema_testing_entity):
    testing_entity = Testing_entity(**schema_testing_entity.dict())
    testing_entityrepo.insert_testing_entity(testing_entity)

def update_testing_entity(id, schema_testing_entity):
    testing_entity = schema_testing_entity.dict()
    del testing_entity['id']
    testing_entityrepo.update_testing_entity(id, testing_entity)

def delete_testing_entity(id):
    testing_entityrepo.delete_testing_entity(id)