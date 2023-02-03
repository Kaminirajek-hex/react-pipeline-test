import traceback
from fastapi import APIRouter, HTTPException
from business import testing_entityservice
from schema.testing_entity import Testing_entity

router = APIRouter(prefix="/testing_entity")


@router.get('')
def api_fetch_testing_entity():
    return testing_entityservice.fetch_testing_entity()

@router.post('')
def api_insert_testing_entity(testing_entity: Testing_entity):
    testing_entityservice.insert_testing_entity(testing_entity)
    return "success"

@router.put('/{id}')
def api_update_testing_entity(id: int, testing_entity: Testing_entity):
    testing_entityservice.update_testing_entity(id, testing_entity)
    return "success"

@router.delete('/{id}')
def api_delete_testing_entity(id: int):
    testing_entityservice.delete_testing_entity(id)
    return "success"