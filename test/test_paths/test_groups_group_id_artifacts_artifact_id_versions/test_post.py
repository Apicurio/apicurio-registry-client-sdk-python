# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import apicurioregistryclient
from apicurioregistryclient.paths.groups_group_id_artifacts_artifact_id_versions import post  # noqa: E501
from apicurioregistryclient import configuration, schemas, api_client

from .. import ApiTestMixin


class TestGroupsGroupIdArtifactsArtifactIdVersions(ApiTestMixin, unittest.TestCase):
    """
    GroupsGroupIdArtifactsArtifactIdVersions unit test stubs
        Create artifact version  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200










if __name__ == '__main__':
    unittest.main()
