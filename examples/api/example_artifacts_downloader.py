#!/usr/bin/env python
import os
import pprint
import sys

import apicurioregistryclient
from apicurioregistryclient.api import artifacts_api
from utils import save_api_file

from dotenv import load_dotenv

load_dotenv()

configuration = apicurioregistryclient.Configuration(
    host=os.environ['SERVICE_REGISTRY_URL'],
    username=os.environ['SERVICE_ACCOUNT_CLIENT_ID'],
    password=os.environ['SERVICE_ACCOUNT_CLIENT_SECRET'],
)

# Enable debug mode that prints the request and response
# configuration.debug = True

## Change if your registry instance using different group
## We recommend to use the same group for your artifact types
group_id = "default"

if sys.argv[0]:
    group_id = sys.argv[0]

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifacts_api.ArtifactsApi(api_client)

    try:
        result = api_instance.list_artifacts_in_group(group_id, async_req=False)
        print(f'Successfully downloaded artifact metadata for group {group_id}')
        if result["artifacts"] is not None:
            for artifact in result["artifacts"]:
                print(f'Fetching Artifact {artifact["id"]}')
                response = api_instance.get_latest_artifact(group_id, artifact["id"], async_req=False)
                schemaFile = response.read()
                schemaFileName = artifact["id"] + "." + artifact["type"].value.lower()
                print(f"Saving artifact as {schemaFileName}")
                save_api_file(schemaFileName, schemaFile)
        else:
            pprint.pprint("No artifacts found in group ", group_id)

    except apicurioregistryclient.ApiException as e:
        pprint.pprint("Exception when fetching artifact: %s\n" % e)
