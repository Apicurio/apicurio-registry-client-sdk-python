#!/usr/bin/env python
import json
import os
import pprint
from time import time
import apicurioregistryclient
from apicurioregistryclient.api import artifacts_api
from artifact_validator import RegistryArtifactValidator
from utils import saveApiFile

from dotenv import load_dotenv

load_dotenv()

configuration = apicurioregistryclient.Configuration(
    host = os.environ['SERVICE_REGISTRY_URL'],
    username=os.environ['SERVICE_ACCOUNT_CLIENT_ID'],
    password=os.environ['SERVICE_ACCOUNT_CLIENT_SECRET'],
)

# Enable debug mode that prints the request and response
# configuration.debug = True

## Change if your registry instance using different group
## We recommend to use the same group for your artifact types
group_id = "default"

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
    validator = RegistryArtifactValidator("default")
    ## Initiallize the cache from API
    validator.build_artifacts_cache(api_instance)
    
    print("\nValidating valid json")
    errors = validator.validate_json_schema("message", valid_object)
    print("Errors from validator for %s" % valid_object)
    print(errors)

    print("\nValidating invalid json")
    errors = validator.validate_json_schema("message", invalid_object)
    print("Errors from validator for %s" % invalid_object)
    print(errors)

              