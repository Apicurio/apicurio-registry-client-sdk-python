

import json
import pprint
import apicurioregistryclient
from jsonschema import validate

from apicurioregistryclient.api.artifacts_api import ArtifactsApi

class RegistryArtifactValidator:
    """ Apicurio Registry Artifact validator
    Downloads the latest schemas from group and caches them locally.
    Uses jsonschema lib to validate json against the schema.

    Usage: 
        validator = RegistryArtifactValidator("default")
        ## Initiallize the cache from API
        validator.build_artifacts_cache(api_instance)
        errors = validator.validate_json_schema("artifact_id", "...your json schema..")
        print(errors)
    
    """

    artifactCache = {}

    def __init__(self, group_id):
        self.artifact_cache = {}
        self.group = group_id

    def build_artifacts_cache(self, api_instance: ArtifactsApi):
        """ Builds a cache of all artifacts in the registry """
        try:
            result = api_instance.list_artifacts_in_group(self.group, async_req=False)
            if result.get("artifacts") is not None:
                for artifact in result["artifacts"]:
                    response = api_instance.get_latest_artifact(
                        self.group, artifact["id"], async_req=False)
                    schemaContent = response.read()
                    schemaKey = artifact["id"]
                    self.artifact_cache[schemaKey] = schemaContent
            else:
                pprint.pprint("No artifacts found in group ", self.group)

        except apicurioregistryclient.ApiException as e:
            pprint.pprint("Exception when fetching artifact: %s" % e)

    def validate_json_schema(self, artifactId: str, jsonObject: dict):
        if self.artifact_cache.get(artifactId, None) is not None:
            schema = self.artifact_cache[artifactId]
            try:
                return validate(instance=jsonObject, schema=json.loads(schema))
            except Exception as e:
                return e
        else:
            raise Exception("Artifact not found in cache. Are you using the right artifactId: " + artifactId)
    