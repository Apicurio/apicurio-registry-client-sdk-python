#!/usr/bin/env python
import os
import apicurioregistryclient
from apicurioregistryclient.api import artifacts_api
from dotenv import load_dotenv

load_dotenv()

configuration = apicurioregistryclient.Configuration(
    host = os.environ['SERVICE_REGISTRY_URL'],
    username=os.environ['SERVICE_ACCOUNT_CLIENT_ID'],
    password=os.environ['SERVICE_ACCOUNT_CLIENT_SECRET'],
)

# configuration.debug = True

group_id = "default"

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifacts_api.ArtifactsApi(api_client)

    try:
        result = api_instance.list_artifacts_in_group(group_id, async_req=False)
        print(result["artifacts"])
        if result["artifacts"] is not None:
            for artifact in result["artifacts"]:
                print("Fetching Artifact " + artifact["id"])
                response = api_instance.get_latest_artifact(group_id, artifact["id"], async_req=False)

    except apicurioregistryclient.ApiException as e:
        print("Exception when fetching artifact: %s\n" % e)           