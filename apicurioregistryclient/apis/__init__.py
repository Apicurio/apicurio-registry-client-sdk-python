
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
from apicurioregistryclient.api.admin_api import AdminApi
from apicurioregistryclient.api.artifact_rules_api import ArtifactRulesApi
from apicurioregistryclient.api.artifacts_api import ArtifactsApi
from apicurioregistryclient.api.metadata_api import MetadataApi
from apicurioregistryclient.api.system_api import SystemApi
from apicurioregistryclient.api.users_api import UsersApi
from apicurioregistryclient.api.versions_api import VersionsApi
