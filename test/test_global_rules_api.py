"""
    Apicurio Registry API [v2]

    Apicurio Registry is a datastore for standard event schemas and API designs. Apicurio Registry enables developers to manage and share the structure of their data using a REST interface. For example, client applications can dynamically push or pull the latest updates to or from the registry without needing to redeploy. Apicurio Registry also enables developers to create rules that govern how registry content can evolve over time. For example, this includes rules for content validation and version compatibility.  The Apicurio Registry REST API enables client applications to manage the artifacts in the registry. This API provides create, read, update, and delete operations for schema and API artifacts, rules, versions, and metadata.   The supported artifact types include: - Apache Avro schema - AsyncAPI specification - Google protocol buffers - GraphQL schema - JSON Schema - Kafka Connect schema - OpenAPI specification - Web Services Description Language - XML Schema Definition   **Important**: The Apicurio Registry REST API is available from `https://MY-REGISTRY-URL/apis/registry/v2` by default. Therefore you must prefix all API operation paths with `../apis/registry/v2` in this case. For example: `../apis/registry/v2/ids/globalIds/{globalId}`.   # noqa: E501

    The version of the OpenAPI document: 2.2.0.Final
    Contact: apicurio@lists.jboss.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import registryclient
from registryclient.api.global_rules_api import GlobalRulesApi  # noqa: E501


class TestGlobalRulesApi(unittest.TestCase):
    """GlobalRulesApi unit test stubs"""

    def setUp(self):
        self.api = GlobalRulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_global_rule(self):
        """Test case for create_global_rule

        Create global rule  # noqa: E501
        """
        pass

    def test_delete_all_global_rules(self):
        """Test case for delete_all_global_rules

        Delete all global rules  # noqa: E501
        """
        pass

    def test_delete_global_rule(self):
        """Test case for delete_global_rule

        Delete global rule  # noqa: E501
        """
        pass

    def test_get_global_rule_config(self):
        """Test case for get_global_rule_config

        Get global rule configuration  # noqa: E501
        """
        pass

    def test_list_global_rules(self):
        """Test case for list_global_rules

        List global rules  # noqa: E501
        """
        pass

    def test_update_global_rule_config(self):
        """Test case for update_global_rule_config

        Update global rule configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()