
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.admin_api import AdminApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from registryclient.api.admin_api import AdminApi
from registryclient.api.artifact_rules_api import ArtifactRulesApi
from registryclient.api.artifacts_api import ArtifactsApi
from registryclient.api.global_rules_api import GlobalRulesApi
from registryclient.api.metadata_api import MetadataApi
from registryclient.api.search_api import SearchApi
from registryclient.api.system_api import SystemApi
from registryclient.api.users_api import UsersApi
from registryclient.api.versions_api import VersionsApi
