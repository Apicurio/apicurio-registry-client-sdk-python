#!/usr/bin/env python
import json
import os
import pprint
from time import time
import apicurioregistryclient
from apicurioregistryclient.api import artifacts_api
from artifact_validator import RegistryArtifactValidator
from utils import seed_schema_from_file

from dotenv import load_dotenv

load_dotenv()

configuration = apicurioregistryclient.Configuration(
    host=os.environ['SERVICE_REGISTRY_URL'],
    username=os.environ['SERVICE_ACCOUNT_CLIENT_ID'],
    password=os.environ['SERVICE_ACCOUNT_CLIENT_SECRET'],
)

# Enable debug mode that prints the request and response
# configuration.debug = True

# Change if your registry instance using different group
# We recommend to use the same group for your artifact types
group_id = "example"
artifact_id = "message_" + str(int(time()))
proto_artifact_id = "person_" + str(int(time()))

valid_object = {
    "message": "Hello World",
    "time": 1648052275
}

invalid_object = {
    "message": "Hello World",
    "time": "1648052275"
}

with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifacts_api.ArtifactsApi(api_client)

    seed_schema_from_file(api_instance, group_id, artifact_id, "./schemas/message.json")
    seed_schema_from_file(api_instance, group_id, proto_artifact_id,
                          "./schemas/person.proto", "PROTOBUF")

    # Validate schema
    validator = RegistryArtifactValidator(group_id)
    # Initiallize the cache from API
    validator.build_artifacts_cache(api_instance)

    print("\nValidating valid json")
    errors = validator.validate_json_schema(artifact_id, valid_object)
    print("Errors from validator for %s" % valid_object)
    print(errors)

    print("\nValidating invalid json")
    errors = validator.validate_json_schema(artifact_id, invalid_object)
    print("Errors from validator for %s" % invalid_object)
    print(errors)
