
import io
import json
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


def seed_schema_from_file(api_instance: ArtifactsApi, group: str, 
    artifact_id: str, location: str, artifact_type = "JSON"):
    """ Helper method to seed registry with example artifact """
    with open(location, "r") as file:
        try:
            result = api_instance.create_artifact(group, file ,
                                                  x_registry_artifact_type=artifact_type,
                                                  x_registry_artifact_id=artifact_id,
                                                  _content_type="application/binary"
                                                  )
            print("Schema created: " + result["id"])
        except Exception as e:
            print("Error creating schema: " + str(e))
