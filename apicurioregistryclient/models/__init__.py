# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from apicurioregistryclient.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from apicurioregistryclient.model.artifact_meta_data import ArtifactMetaData
from apicurioregistryclient.model.artifact_reference import ArtifactReference
from apicurioregistryclient.model.artifact_search_results import ArtifactSearchResults
from apicurioregistryclient.model.artifact_state import ArtifactState
from apicurioregistryclient.model.artifact_type import ArtifactType
from apicurioregistryclient.model.configuration_property import ConfigurationProperty
from apicurioregistryclient.model.content_create_request import ContentCreateRequest
from apicurioregistryclient.model.download_ref import DownloadRef
from apicurioregistryclient.model.editable_meta_data import EditableMetaData
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.if_exists import IfExists
from apicurioregistryclient.model.limits import Limits
from apicurioregistryclient.model.log_configuration import LogConfiguration
from apicurioregistryclient.model.log_level import LogLevel
from apicurioregistryclient.model.named_log_configuration import NamedLogConfiguration
from apicurioregistryclient.model.named_log_configuration_all_of import NamedLogConfigurationAllOf
from apicurioregistryclient.model.properties import Properties
from apicurioregistryclient.model.role_mapping import RoleMapping
from apicurioregistryclient.model.role_type import RoleType
from apicurioregistryclient.model.rule import Rule
from apicurioregistryclient.model.rule_type import RuleType
from apicurioregistryclient.model.rule_violation_cause import RuleViolationCause
from apicurioregistryclient.model.rule_violation_error import RuleViolationError
from apicurioregistryclient.model.rule_violation_error_all_of import RuleViolationErrorAllOf
from apicurioregistryclient.model.searched_artifact import SearchedArtifact
from apicurioregistryclient.model.searched_version import SearchedVersion
from apicurioregistryclient.model.sort_by import SortBy
from apicurioregistryclient.model.sort_order import SortOrder
from apicurioregistryclient.model.system_info import SystemInfo
from apicurioregistryclient.model.update_configuration_property import UpdateConfigurationProperty
from apicurioregistryclient.model.update_role import UpdateRole
from apicurioregistryclient.model.update_state import UpdateState
from apicurioregistryclient.model.user_info import UserInfo
from apicurioregistryclient.model.version_meta_data import VersionMetaData
from apicurioregistryclient.model.version_search_results import VersionSearchResults
