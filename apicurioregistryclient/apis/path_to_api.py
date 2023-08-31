import typing_extensions

from apicurioregistryclient.paths import PathValues
from apicurioregistryclient.apis.paths.ids_global_ids_global_id import IdsGlobalIdsGlobalId
from apicurioregistryclient.apis.paths.admin_artifact_types import AdminArtifactTypes
from apicurioregistryclient.apis.paths.admin_rules import AdminRules
from apicurioregistryclient.apis.paths.admin_rules_rule import AdminRulesRule
from apicurioregistryclient.apis.paths.admin_loggers import AdminLoggers
from apicurioregistryclient.apis.paths.admin_loggers_logger import AdminLoggersLogger
from apicurioregistryclient.apis.paths.system_info import SystemInfo
from apicurioregistryclient.apis.paths.search_artifacts import SearchArtifacts
from apicurioregistryclient.apis.paths.admin_export import AdminExport
from apicurioregistryclient.apis.paths.admin_import import AdminImport
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_state import GroupsGroupIdArtifactsArtifactIdState
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_versions_version_meta import GroupsGroupIdArtifactsArtifactIdVersionsVersionMeta
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_versions_version import GroupsGroupIdArtifactsArtifactIdVersionsVersion
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_versions_version_state import GroupsGroupIdArtifactsArtifactIdVersionsVersionState
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_rules import GroupsGroupIdArtifactsArtifactIdRules
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_rules_rule import GroupsGroupIdArtifactsArtifactIdRulesRule
from apicurioregistryclient.apis.paths.admin_role_mappings_principal_id import AdminRoleMappingsPrincipalId
from apicurioregistryclient.apis.paths.admin_role_mappings import AdminRoleMappings
from apicurioregistryclient.apis.paths.users_me import UsersMe
from apicurioregistryclient.apis.paths.ids_content_hashes_content_hash_references import IdsContentHashesContentHashReferences
from apicurioregistryclient.apis.paths.ids_content_ids_content_id_references import IdsContentIdsContentIdReferences
from apicurioregistryclient.apis.paths.ids_global_ids_global_id_references import IdsGlobalIdsGlobalIdReferences
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_versions_version_references import GroupsGroupIdArtifactsArtifactIdVersionsVersionReferences
from apicurioregistryclient.apis.paths.admin_config_properties import AdminConfigProperties
from apicurioregistryclient.apis.paths.admin_config_properties_property_name import AdminConfigPropertiesPropertyName
from apicurioregistryclient.apis.paths.system_limits import SystemLimits
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id import GroupsGroupIdArtifactsArtifactId
from apicurioregistryclient.apis.paths.groups_group_id_artifacts import GroupsGroupIdArtifacts
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_test import GroupsGroupIdArtifactsArtifactIdTest
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_versions import GroupsGroupIdArtifactsArtifactIdVersions
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_owner import GroupsGroupIdArtifactsArtifactIdOwner
from apicurioregistryclient.apis.paths.groups_group_id import GroupsGroupId
from apicurioregistryclient.apis.paths.groups import Groups
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_meta import GroupsGroupIdArtifactsArtifactIdMeta
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_versions_version_comments import GroupsGroupIdArtifactsArtifactIdVersionsVersionComments
from apicurioregistryclient.apis.paths.groups_group_id_artifacts_artifact_id_versions_version_comments_comment_id import GroupsGroupIdArtifactsArtifactIdVersionsVersionCommentsCommentId
from apicurioregistryclient.apis.paths.ids_content_ids_content_id_ import IdsContentIdsContentId
from apicurioregistryclient.apis.paths.ids_content_hashes_content_hash_ import IdsContentHashesContentHash

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.IDS_GLOBAL_IDS_GLOBAL_ID: IdsGlobalIdsGlobalId,
        PathValues.ADMIN_ARTIFACT_TYPES: AdminArtifactTypes,
        PathValues.ADMIN_RULES: AdminRules,
        PathValues.ADMIN_RULES_RULE: AdminRulesRule,
        PathValues.ADMIN_LOGGERS: AdminLoggers,
        PathValues.ADMIN_LOGGERS_LOGGER: AdminLoggersLogger,
        PathValues.SYSTEM_INFO: SystemInfo,
        PathValues.SEARCH_ARTIFACTS: SearchArtifacts,
        PathValues.ADMIN_EXPORT: AdminExport,
        PathValues.ADMIN_IMPORT: AdminImport,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_STATE: GroupsGroupIdArtifactsArtifactIdState,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_META: GroupsGroupIdArtifactsArtifactIdVersionsVersionMeta,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION: GroupsGroupIdArtifactsArtifactIdVersionsVersion,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_STATE: GroupsGroupIdArtifactsArtifactIdVersionsVersionState,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_RULES: GroupsGroupIdArtifactsArtifactIdRules,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_RULES_RULE: GroupsGroupIdArtifactsArtifactIdRulesRule,
        PathValues.ADMIN_ROLE_MAPPINGS_PRINCIPAL_ID: AdminRoleMappingsPrincipalId,
        PathValues.ADMIN_ROLE_MAPPINGS: AdminRoleMappings,
        PathValues.USERS_ME: UsersMe,
        PathValues.IDS_CONTENT_HASHES_CONTENT_HASH_REFERENCES: IdsContentHashesContentHashReferences,
        PathValues.IDS_CONTENT_IDS_CONTENT_ID_REFERENCES: IdsContentIdsContentIdReferences,
        PathValues.IDS_GLOBAL_IDS_GLOBAL_ID_REFERENCES: IdsGlobalIdsGlobalIdReferences,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_REFERENCES: GroupsGroupIdArtifactsArtifactIdVersionsVersionReferences,
        PathValues.ADMIN_CONFIG_PROPERTIES: AdminConfigProperties,
        PathValues.ADMIN_CONFIG_PROPERTIES_PROPERTY_NAME: AdminConfigPropertiesPropertyName,
        PathValues.SYSTEM_LIMITS: SystemLimits,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID: GroupsGroupIdArtifactsArtifactId,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS: GroupsGroupIdArtifacts,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_TEST: GroupsGroupIdArtifactsArtifactIdTest,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS: GroupsGroupIdArtifactsArtifactIdVersions,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_OWNER: GroupsGroupIdArtifactsArtifactIdOwner,
        PathValues.GROUPS_GROUP_ID: GroupsGroupId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_META: GroupsGroupIdArtifactsArtifactIdMeta,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_COMMENTS: GroupsGroupIdArtifactsArtifactIdVersionsVersionComments,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_COMMENTS_COMMENT_ID: GroupsGroupIdArtifactsArtifactIdVersionsVersionCommentsCommentId,
        PathValues.IDS_CONTENT_IDS_CONTENT_ID_: IdsContentIdsContentId,
        PathValues.IDS_CONTENT_HASHES_CONTENT_HASH_: IdsContentHashesContentHash,
    }
)

path_to_api = PathToApi(
    {
        PathValues.IDS_GLOBAL_IDS_GLOBAL_ID: IdsGlobalIdsGlobalId,
        PathValues.ADMIN_ARTIFACT_TYPES: AdminArtifactTypes,
        PathValues.ADMIN_RULES: AdminRules,
        PathValues.ADMIN_RULES_RULE: AdminRulesRule,
        PathValues.ADMIN_LOGGERS: AdminLoggers,
        PathValues.ADMIN_LOGGERS_LOGGER: AdminLoggersLogger,
        PathValues.SYSTEM_INFO: SystemInfo,
        PathValues.SEARCH_ARTIFACTS: SearchArtifacts,
        PathValues.ADMIN_EXPORT: AdminExport,
        PathValues.ADMIN_IMPORT: AdminImport,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_STATE: GroupsGroupIdArtifactsArtifactIdState,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_META: GroupsGroupIdArtifactsArtifactIdVersionsVersionMeta,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION: GroupsGroupIdArtifactsArtifactIdVersionsVersion,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_STATE: GroupsGroupIdArtifactsArtifactIdVersionsVersionState,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_RULES: GroupsGroupIdArtifactsArtifactIdRules,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_RULES_RULE: GroupsGroupIdArtifactsArtifactIdRulesRule,
        PathValues.ADMIN_ROLE_MAPPINGS_PRINCIPAL_ID: AdminRoleMappingsPrincipalId,
        PathValues.ADMIN_ROLE_MAPPINGS: AdminRoleMappings,
        PathValues.USERS_ME: UsersMe,
        PathValues.IDS_CONTENT_HASHES_CONTENT_HASH_REFERENCES: IdsContentHashesContentHashReferences,
        PathValues.IDS_CONTENT_IDS_CONTENT_ID_REFERENCES: IdsContentIdsContentIdReferences,
        PathValues.IDS_GLOBAL_IDS_GLOBAL_ID_REFERENCES: IdsGlobalIdsGlobalIdReferences,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_REFERENCES: GroupsGroupIdArtifactsArtifactIdVersionsVersionReferences,
        PathValues.ADMIN_CONFIG_PROPERTIES: AdminConfigProperties,
        PathValues.ADMIN_CONFIG_PROPERTIES_PROPERTY_NAME: AdminConfigPropertiesPropertyName,
        PathValues.SYSTEM_LIMITS: SystemLimits,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID: GroupsGroupIdArtifactsArtifactId,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS: GroupsGroupIdArtifacts,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_TEST: GroupsGroupIdArtifactsArtifactIdTest,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS: GroupsGroupIdArtifactsArtifactIdVersions,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_OWNER: GroupsGroupIdArtifactsArtifactIdOwner,
        PathValues.GROUPS_GROUP_ID: GroupsGroupId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_META: GroupsGroupIdArtifactsArtifactIdMeta,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_COMMENTS: GroupsGroupIdArtifactsArtifactIdVersionsVersionComments,
        PathValues.GROUPS_GROUP_ID_ARTIFACTS_ARTIFACT_ID_VERSIONS_VERSION_COMMENTS_COMMENT_ID: GroupsGroupIdArtifactsArtifactIdVersionsVersionCommentsCommentId,
        PathValues.IDS_CONTENT_IDS_CONTENT_ID_: IdsContentIdsContentId,
        PathValues.IDS_CONTENT_HASHES_CONTENT_HASH_: IdsContentHashesContentHash,
    }
)
