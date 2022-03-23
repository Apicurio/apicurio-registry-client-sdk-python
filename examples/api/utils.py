

# Helper method to save api files in temporary folder
import io

from apicurioregistryclient import api
from apicurioregistryclient.api.artifacts_api import ArtifactsApi
from apicurioregistryclient.model.artifact_type import ArtifactType


def save_api_file(name, content):
    with open("./temp/" + name, "w+b") as file:
        try:
            print(file.name)
            file.write(content)
        except Exception as e:
            print("Error writing file: " + str(e))

# Helper method to seed registry with example artifact
# 1. read message.jsonschema file
# 2. create schema object using api_instance.create_artifact


def seed_schema_from_file(api_instance: ArtifactsApi, group: str, artifact_id: str):
    with open("./message.jsonschema", "r") as file:
        try:
            schema = io.StringIO(file.read())
            result = api_instance.create_artifact(group, schema,
                                                  async_req=False,
                                                  x_registry_artifact_type="JSON",
                                                  x_registry_artifact_id=artifact_id)
            print("Schema created: " + result["id"])
        except Exception as e:
            print("Error creating schema: " + str(e))
