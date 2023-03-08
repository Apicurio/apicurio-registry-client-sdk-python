# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from apicurioregistryclient.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    IDS_CONTENT_IDS_CONTENT_ID_ = "/ids/contentIds/{contentId}/"
    IDS_GLOBAL_IDS_GLOBAL_ID = "/ids/globalIds/{globalId}"
    IDS_CONTENT_HASHES_CONTENT_HASH_ = "/ids/contentHashes/{contentHash}/"
    ADMIN_ARTIFACT_TYPES = "/admin/artifactTypes"
    ADMIN_RULES = "/admin/rules"
    ADMIN_RULES_RULE = "/admin/rules/{rule}"
    ADMIN_LOGGERS = "/admin/loggers"
    ADMIN_LOGGERS_LOGGER = "/admin/loggers/{logger}"
    SYSTEM_INFO = "/system/info"
    SEARCH_ARTIFACTS = "/search/artifacts"
    ADMIN_EXPORT = "/admin/export"
    ADMIN_IMPORT = "/admin/import"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_STATE = "/groups/{groupId}/artifacts/{artifactId}/state"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_META = "/groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION = "/groups/{groupId}/artifacts/{artifactId}/versions/{version}"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_STATE = "/groups/{groupId}/artifacts/{artifactId}/versions/{version}/state"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_RULES = "/groups/{groupId}/artifacts/{artifactId}/rules"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_RULES_RULE = "/groups/{groupId}/artifacts/{artifactId}/rules/{rule}"
    ADMIN_ROLE_MAPPINGS_PRINCIPAL_ID = "/admin/roleMappings/{principalId}"
    ADMIN_ROLE_MAPPINGS = "/admin/roleMappings"
    USERS_ME = "/users/me"
    IDS_CONTENT_HASHES_CONTENT_HASH_REFERENCES = "/ids/contentHashes/{contentHash}/references"
    IDS_CONTENT_IDS_CONTENT_ID_REFERENCES = "/ids/contentIds/{contentId}/references"
    IDS_GLOBAL_IDS_GLOBAL_ID_REFERENCES = "/ids/globalIds/{globalId}/references"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_REFERENCES = "/groups/{groupId}/artifacts/{artifactId}/versions/{version}/references"
    ADMIN_CONFIG_PROPERTIES = "/admin/config/properties"
    ADMIN_CONFIG_PROPERTIES_PROPERTY_NAME = "/admin/config/properties/{propertyName}"
    SYSTEM_LIMITS = "/system/limits"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID = "/groups/{groupId}/artifacts/{artifactId}"
    GROUPS_GROUP_ID_ARTIFACTS = "/groups/{groupId}/artifacts"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_TEST = "/groups/{groupId}/artifacts/{artifactId}/test"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS = "/groups/{groupId}/artifacts/{artifactId}/versions"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_META = "/groups/{groupId}/artifacts/{artifactId}/meta"
    GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_OWNER = "/groups/{groupId}/artifacts/{artifactId}/owner"
    GROUPS_GROUP_ID = "/groups/{groupId}"
    GROUPS = "/groups"
