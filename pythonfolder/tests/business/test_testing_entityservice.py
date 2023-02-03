import unittest
from unittest import mock
from schema.testing_entity import Testing_entity as Testing_entitySchema
from api.routes import app
from business import testing_entityservice

ENDPOINT = '/testing_entity'
SUCCESS_MSG = '"success"'


class TestTesting_entityService(unittest.TestCase):

    def setUp(self) -> None:
        self.testing_entity = {
            'id': 1,
            'name': 'uWlha',
            'number': 43
        }
        self.testing_entity_list = [self.testing_entity]
        self.testing_entity_schema_obj = Testing_entitySchema(**self.testing_entity)
    
    @mock.patch('business.testing_entityservice.testing_entityrepo.get_testing_entity')
    def test_fetch_testing_entity(self, mock_fetch):

        mock_fetch.return_value = self.testing_entity_list

        out = testing_entityservice.fetch_testing_entity()
        
        assert out == self.testing_entity_list
        assert mock_fetch.called

    @mock.patch('business.testing_entityservice.testing_entityrepo.insert_testing_entity')
    def test_api_insert_testing_entity(self, mock_insert):

        mock_insert.return_value = None

        out = testing_entityservice.insert_testing_entity(self.testing_entity_schema_obj)
        
        assert mock_insert.called
        assert out == None


    @mock.patch('business.testing_entityservice.testing_entityrepo.update_testing_entity')
    def test_api_update_testing_entity(self, mock_update):

        mock_update.return_value = None

        out = testing_entityservice.update_testing_entity(1, self.testing_entity_schema_obj)
        
        assert mock_update.called
        assert out == None

    @mock.patch('business.testing_entityservice.testing_entityrepo.delete_testing_entity')
    def test_api_delete_testing_entity(self, mock_delete):

        mock_delete.return_value = None

        out = testing_entityservice.delete_testing_entity(1)
        
        assert mock_delete.called
        assert out == None
