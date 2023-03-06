# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from apicurioregistryclient.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ARTIFACTS = "Artifacts"
    METADATA = "Metadata"
    VERSIONS = "Versions"
    ARTIFACT_RULES = "Artifact rules"
    GLOBAL_RULES = "Global rules"
    SEARCH = "Search"
    ADMIN = "Admin"
    SYSTEM = "System"
    USERS = "Users"
    GROUPS = "Groups"
    ARTIFACT_TYPE = "Artifact Type"
