import pytest
import boto3
from moto import mock_aws

TABLE_SCHEMA = {
    "AttributeDefinitions": [
        {"AttributeName": "PK", "AttributeType": "S"},
        {"AttributeName": "SK", "AttributeType": "S"},
    ],
    "TableName": "example-table",
    "KeySchema": [
        {"AttributeName": "PK", "KeyType": "HASH"},
        {"AttributeName": "SK", "KeyType": "RANGE"},
    ],
    "BillingMode": "PAY_PER_REQUEST",
}


INITIAL_ITEMS = [
    {
        "PK": "ITEM_ID#1",
        "SK": "ITEM#1",
        "name": "Item 1",
        "description": "Description of item 1",
        "price": 100,
    },
    {
        "PK": "ITEM_ID#2",
        "SK": "ITEM#2",
        "name": "Item 2",
        "description": "Description of item 2",
        "price": 200,
    },
    {
        "PK": "ITEM_ID#3",
        "SK": "ITEM#3",
        "name": "Item 3",
        "description": "Description of item 3",
        "price": 300,
    },
    {
        "PK": "ITEM_ID#4",
        "SK": "ITEM#4",
        "name": "Item 4",
        "description": "Description of item 4",
        "price": 400,
    },
    {
        "PK": "ITEM_ID#5",
        "SK": "ITEM#5",
        "name": "Item 5",
        "description": "Description of item 5",
        "price": 500,
    },
]


@pytest.fixture
def mock_dynamodb_resource():
    with mock_aws():
        yield boto3.resource("dynamodb")


@pytest.fixture
def mock_dynamo_table(mock_dynamodb_resource):
    table = mock_dynamodb_resource.create_table(**TABLE_SCHEMA)
    for item in INITIAL_ITEMS:
        table.put_item(Item=item)
    yield table
