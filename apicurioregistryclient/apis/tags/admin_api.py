# coding: utf-8

"""
    Apicurio Registry API [v2]

    Apicurio Registry is a datastore for standard event schemas and API designs. Apicurio Registry enables developers to manage and share the structure of their data using a REST interface. For example, client applications can dynamically push or pull the latest updates to or from the registry without needing to redeploy. Apicurio Registry also enables developers to create rules that govern how registry content can evolve over time. For example, this includes rules for content validation and version compatibility.  The Apicurio Registry REST API enables client applications to manage the artifacts in the registry. This API provides create, read, update, and delete operations for schema and API artifacts, rules, versions, and metadata.   The supported artifact types include: - Apache Avro schema - AsyncAPI specification - Google protocol buffers - GraphQL schema - JSON Schema - Kafka Connect schema - OpenAPI specification - Web Services Description Language - XML Schema Definition   **Important**: The Apicurio Registry REST API is available from `https://MY-REGISTRY-URL/apis/registry/v2` by default. Therefore you must prefix all API operation paths with `../apis/registry/v2` in this case. For example: `../apis/registry/v2/ids/globalIds/{globalId}`.   # noqa: E501

    The version of the OpenAPI document: 2.3.1.Final
    Contact: apicurio@lists.jboss.org
    Generated by: https://openapi-generator.tech
"""

from apicurioregistryclient.paths.admin_rules.post import CreateGlobalRule
from apicurioregistryclient.paths.admin_role_mappings.post import CreateRoleMapping
from apicurioregistryclient.paths.admin_rules.delete import DeleteAllGlobalRules
from apicurioregistryclient.paths.admin_rules_rule.delete import DeleteGlobalRule
from apicurioregistryclient.paths.admin_role_mappings_principal_id.delete import DeleteRoleMapping
from apicurioregistryclient.paths.admin_export.get import ExportData
from apicurioregistryclient.paths.admin_config_properties_property_name.get import GetConfigProperty
from apicurioregistryclient.paths.admin_rules_rule.get import GetGlobalRuleConfig
from apicurioregistryclient.paths.admin_loggers_logger.get import GetLogConfiguration
from apicurioregistryclient.paths.admin_role_mappings_principal_id.get import GetRoleMapping
from apicurioregistryclient.paths.admin_import.post import ImportData
from apicurioregistryclient.paths.admin_config_properties.get import ListConfigProperties
from apicurioregistryclient.paths.admin_rules.get import ListGlobalRules
from apicurioregistryclient.paths.admin_loggers.get import ListLogConfigurations
from apicurioregistryclient.paths.admin_role_mappings.get import ListRoleMappings
from apicurioregistryclient.paths.admin_loggers_logger.delete import RemoveLogConfiguration
from apicurioregistryclient.paths.admin_config_properties_property_name.delete import ResetConfigProperty
from apicurioregistryclient.paths.admin_loggers_logger.put import SetLogConfiguration
from apicurioregistryclient.paths.admin_config_properties_property_name.put import UpdateConfigProperty
from apicurioregistryclient.paths.admin_rules_rule.put import UpdateGlobalRuleConfig
from apicurioregistryclient.paths.admin_role_mappings_principal_id.put import UpdateRoleMapping


class AdminApi(
    CreateGlobalRule,
    CreateRoleMapping,
    DeleteAllGlobalRules,
    DeleteGlobalRule,
    DeleteRoleMapping,
    ExportData,
    GetConfigProperty,
    GetGlobalRuleConfig,
    GetLogConfiguration,
    GetRoleMapping,
    ImportData,
    ListConfigProperties,
    ListGlobalRules,
    ListLogConfigurations,
    ListRoleMappings,
    RemoveLogConfiguration,
    ResetConfigProperty,
    SetLogConfiguration,
    UpdateConfigProperty,
    UpdateGlobalRuleConfig,
    UpdateRoleMapping,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
