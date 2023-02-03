import json
import unittest
from unittest import mock
from fastapi.testclient import TestClient
from api.routes import app
from schema.testing_entity import Testing_entity
from core.logger import logger

ENDPOINT = '/testing_entity'
SUCCESS_MSG = '"success"'


class TestTesting_entityAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.testing_entity = {
            'id': 1,
            'name': 'hf2t0',
            'number': 34
        }
        self.testing_entity_list = [self.testing_entity]
        self.client = TestClient(app)
        logger.disabled = True

    @mock.patch('api.testing_entityapi.testing_entityservice.fetch_testing_entity')
    def test_api_fetch_testing_entity(self, mock_fetch):

        mock_fetch.return_value = self.testing_entity_list

        response = self.client.get(ENDPOINT)
        response_content = json.loads(response.content.decode('utf-8'))

        assert response.status_code == 200
        assert response_content == self.testing_entity_list

    @mock.patch('api.testing_entityapi.testing_entityservice.insert_testing_entity')
    def test_api_insert_testing_entity(self, mock_insert):

        mock_insert.return_value = self.testing_entity_list
        testing_entity = Testing_entity(**self.testing_entity)
        print(testing_entity)

        response = self.client.post(ENDPOINT, data = json.dumps(self.testing_entity))
        response_content = response.content.decode('utf-8')

        assert response_content == SUCCESS_MSG
        assert mock_insert.called

    @mock.patch('api.testing_entityapi.testing_entityservice.update_testing_entity')
    def test_api_update_testing_entity(self, mock_update):

        mock_update.return_value = self.testing_entity_list

        response = self.client.put(f'{ENDPOINT}/1', data = json.dumps(self.testing_entity))
        response_content = response.content.decode('utf-8')

        assert response_content == SUCCESS_MSG
        assert mock_update.called

    @mock.patch('api.testing_entityapi.testing_entityservice.delete_testing_entity')
    def test_api_delete_testing_entity(self, mock_delete):

        mock_delete.return_value = self.testing_entity_list

        response = self.client.delete(f'{ENDPOINT}/1')
        response_content = response.content.decode('utf-8')

        assert response.status_code == 200
        assert response_content == SUCCESS_MSG
        assert mock_delete.called
