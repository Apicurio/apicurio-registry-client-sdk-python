#!/usr/bin/env python
import os
import apicurioregistryclient
from apicurioregistryclient.api import artifacts_api
from dotenv import load_dotenv

load_dotenv()

configuration = apicurioregistryclient.Configuration(
    host = os.environ['RHOAS_SERVICE_REGISTRY_URL'],
    username=os.environ['RHOAS_SERVICE_ACCOUNT_CLIENT_ID'],
    password=os.environ['RHOAS_SERVICE_ACCOUNT_CLIENT_SECRET'],
)

artifact_id = "8f9231ac-9d2b-4619-81e0-86b5088dadd3"
group_id = "default"

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifacts_api.ArtifactsApi(api_client)

    try:
        ## Fetch artifact
        response = api_instance.get_latest_artifact(group_id, artifact_id, async_req=False)
        print(response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when fetching artifact: %s\n" % e)           