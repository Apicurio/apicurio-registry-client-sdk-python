import typing_extensions

from apicurioregistryclient.apis.tags import TagValues
from apicurioregistryclient.apis.tags.artifacts_api import ArtifactsApi
from apicurioregistryclient.apis.tags.metadata_api import MetadataApi
from apicurioregistryclient.apis.tags.versions_api import VersionsApi
from apicurioregistryclient.apis.tags.artifact_rules_api import ArtifactRulesApi
from apicurioregistryclient.apis.tags.global_rules_api import GlobalRulesApi
from apicurioregistryclient.apis.tags.search_api import SearchApi
from apicurioregistryclient.apis.tags.admin_api import AdminApi
from apicurioregistryclient.apis.tags.system_api import SystemApi
from apicurioregistryclient.apis.tags.users_api import UsersApi
from apicurioregistryclient.apis.tags.groups_api import GroupsApi
from apicurioregistryclient.apis.tags.artifact_type_api import ArtifactTypeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ARTIFACTS: ArtifactsApi,
        TagValues.METADATA: MetadataApi,
        TagValues.VERSIONS: VersionsApi,
        TagValues.ARTIFACT_RULES: ArtifactRulesApi,
        TagValues.GLOBAL_RULES: GlobalRulesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.ADMIN: AdminApi,
        TagValues.SYSTEM: SystemApi,
        TagValues.USERS: UsersApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.ARTIFACT_TYPE: ArtifactTypeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ARTIFACTS: ArtifactsApi,
        TagValues.METADATA: MetadataApi,
        TagValues.VERSIONS: VersionsApi,
        TagValues.ARTIFACT_RULES: ArtifactRulesApi,
        TagValues.GLOBAL_RULES: GlobalRulesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.ADMIN: AdminApi,
        TagValues.SYSTEM: SystemApi,
        TagValues.USERS: UsersApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.ARTIFACT_TYPE: ArtifactTypeApi,
    }
)
