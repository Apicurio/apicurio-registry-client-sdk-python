# coding: utf-8

"""
    Apicurio Registry API [v2]

    Apicurio Registry is a datastore for standard event schemas and API designs. Apicurio Registry enables developers to manage and share the structure of their data using a REST interface. For example, client applications can dynamically push or pull the latest updates to or from the registry without needing to redeploy. Apicurio Registry also enables developers to create rules that govern how registry content can evolve over time. For example, this includes rules for content validation and version compatibility.  The Apicurio Registry REST API enables client applications to manage the artifacts in the registry. This API provides create, read, update, and delete operations for schema and API artifacts, rules, versions, and metadata.   The supported artifact types include: - Apache Avro schema - AsyncAPI specification - Google protocol buffers - GraphQL schema - JSON Schema - Kafka Connect schema - OpenAPI specification - Web Services Description Language - XML Schema Definition   **Important**: The Apicurio Registry REST API is available from `https://MY-REGISTRY-URL/apis/registry/v2` by default. Therefore you must prefix all API operation paths with `../apis/registry/v2` in this case. For example: `../apis/registry/v2/ids/globalIds/{globalId}`.   # noqa: E501

    The version of the OpenAPI document: 2.4.x
    Contact: apicurio@lists.jboss.org
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from apicurioregistryclient import schemas  # noqa: F401


class Limits(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    List of limitations on used resources, that are applied on the current instance of Registry.
Keys represent the resource type and are suffixed by the corresponding unit.
Values are integers. Only non-negative values are allowed, with the exception of -1, which means that the limit is not applied.
    """


    class MetaOapg:
        
        class properties:
            maxTotalSchemasCount = schemas.Int64Schema
            maxSchemaSizeBytes = schemas.Int64Schema
            maxArtifactsCount = schemas.Int64Schema
            maxVersionsPerArtifactCount = schemas.Int64Schema
            maxArtifactPropertiesCount = schemas.Int64Schema
            maxPropertyKeySizeBytes = schemas.Int64Schema
            maxPropertyValueSizeBytes = schemas.Int64Schema
            maxArtifactLabelsCount = schemas.Int64Schema
            maxLabelSizeBytes = schemas.Int64Schema
            maxArtifactNameLengthChars = schemas.Int64Schema
            maxArtifactDescriptionLengthChars = schemas.Int64Schema
            maxRequestsPerSecondCount = schemas.Int64Schema
            __annotations__ = {
                "maxTotalSchemasCount": maxTotalSchemasCount,
                "maxSchemaSizeBytes": maxSchemaSizeBytes,
                "maxArtifactsCount": maxArtifactsCount,
                "maxVersionsPerArtifactCount": maxVersionsPerArtifactCount,
                "maxArtifactPropertiesCount": maxArtifactPropertiesCount,
                "maxPropertyKeySizeBytes": maxPropertyKeySizeBytes,
                "maxPropertyValueSizeBytes": maxPropertyValueSizeBytes,
                "maxArtifactLabelsCount": maxArtifactLabelsCount,
                "maxLabelSizeBytes": maxLabelSizeBytes,
                "maxArtifactNameLengthChars": maxArtifactNameLengthChars,
                "maxArtifactDescriptionLengthChars": maxArtifactDescriptionLengthChars,
                "maxRequestsPerSecondCount": maxRequestsPerSecondCount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxTotalSchemasCount"]) -> MetaOapg.properties.maxTotalSchemasCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxSchemaSizeBytes"]) -> MetaOapg.properties.maxSchemaSizeBytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxArtifactsCount"]) -> MetaOapg.properties.maxArtifactsCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxVersionsPerArtifactCount"]) -> MetaOapg.properties.maxVersionsPerArtifactCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxArtifactPropertiesCount"]) -> MetaOapg.properties.maxArtifactPropertiesCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPropertyKeySizeBytes"]) -> MetaOapg.properties.maxPropertyKeySizeBytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPropertyValueSizeBytes"]) -> MetaOapg.properties.maxPropertyValueSizeBytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxArtifactLabelsCount"]) -> MetaOapg.properties.maxArtifactLabelsCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxLabelSizeBytes"]) -> MetaOapg.properties.maxLabelSizeBytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxArtifactNameLengthChars"]) -> MetaOapg.properties.maxArtifactNameLengthChars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxArtifactDescriptionLengthChars"]) -> MetaOapg.properties.maxArtifactDescriptionLengthChars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxRequestsPerSecondCount"]) -> MetaOapg.properties.maxRequestsPerSecondCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxTotalSchemasCount", "maxSchemaSizeBytes", "maxArtifactsCount", "maxVersionsPerArtifactCount", "maxArtifactPropertiesCount", "maxPropertyKeySizeBytes", "maxPropertyValueSizeBytes", "maxArtifactLabelsCount", "maxLabelSizeBytes", "maxArtifactNameLengthChars", "maxArtifactDescriptionLengthChars", "maxRequestsPerSecondCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxTotalSchemasCount"]) -> typing.Union[MetaOapg.properties.maxTotalSchemasCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxSchemaSizeBytes"]) -> typing.Union[MetaOapg.properties.maxSchemaSizeBytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxArtifactsCount"]) -> typing.Union[MetaOapg.properties.maxArtifactsCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxVersionsPerArtifactCount"]) -> typing.Union[MetaOapg.properties.maxVersionsPerArtifactCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxArtifactPropertiesCount"]) -> typing.Union[MetaOapg.properties.maxArtifactPropertiesCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPropertyKeySizeBytes"]) -> typing.Union[MetaOapg.properties.maxPropertyKeySizeBytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPropertyValueSizeBytes"]) -> typing.Union[MetaOapg.properties.maxPropertyValueSizeBytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxArtifactLabelsCount"]) -> typing.Union[MetaOapg.properties.maxArtifactLabelsCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxLabelSizeBytes"]) -> typing.Union[MetaOapg.properties.maxLabelSizeBytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxArtifactNameLengthChars"]) -> typing.Union[MetaOapg.properties.maxArtifactNameLengthChars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxArtifactDescriptionLengthChars"]) -> typing.Union[MetaOapg.properties.maxArtifactDescriptionLengthChars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxRequestsPerSecondCount"]) -> typing.Union[MetaOapg.properties.maxRequestsPerSecondCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxTotalSchemasCount", "maxSchemaSizeBytes", "maxArtifactsCount", "maxVersionsPerArtifactCount", "maxArtifactPropertiesCount", "maxPropertyKeySizeBytes", "maxPropertyValueSizeBytes", "maxArtifactLabelsCount", "maxLabelSizeBytes", "maxArtifactNameLengthChars", "maxArtifactDescriptionLengthChars", "maxRequestsPerSecondCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        maxTotalSchemasCount: typing.Union[MetaOapg.properties.maxTotalSchemasCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxSchemaSizeBytes: typing.Union[MetaOapg.properties.maxSchemaSizeBytes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxArtifactsCount: typing.Union[MetaOapg.properties.maxArtifactsCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxVersionsPerArtifactCount: typing.Union[MetaOapg.properties.maxVersionsPerArtifactCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxArtifactPropertiesCount: typing.Union[MetaOapg.properties.maxArtifactPropertiesCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxPropertyKeySizeBytes: typing.Union[MetaOapg.properties.maxPropertyKeySizeBytes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxPropertyValueSizeBytes: typing.Union[MetaOapg.properties.maxPropertyValueSizeBytes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxArtifactLabelsCount: typing.Union[MetaOapg.properties.maxArtifactLabelsCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxLabelSizeBytes: typing.Union[MetaOapg.properties.maxLabelSizeBytes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxArtifactNameLengthChars: typing.Union[MetaOapg.properties.maxArtifactNameLengthChars, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxArtifactDescriptionLengthChars: typing.Union[MetaOapg.properties.maxArtifactDescriptionLengthChars, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxRequestsPerSecondCount: typing.Union[MetaOapg.properties.maxRequestsPerSecondCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Limits':
        return super().__new__(
            cls,
            *_args,
            maxTotalSchemasCount=maxTotalSchemasCount,
            maxSchemaSizeBytes=maxSchemaSizeBytes,
            maxArtifactsCount=maxArtifactsCount,
            maxVersionsPerArtifactCount=maxVersionsPerArtifactCount,
            maxArtifactPropertiesCount=maxArtifactPropertiesCount,
            maxPropertyKeySizeBytes=maxPropertyKeySizeBytes,
            maxPropertyValueSizeBytes=maxPropertyValueSizeBytes,
            maxArtifactLabelsCount=maxArtifactLabelsCount,
            maxLabelSizeBytes=maxLabelSizeBytes,
            maxArtifactNameLengthChars=maxArtifactNameLengthChars,
            maxArtifactDescriptionLengthChars=maxArtifactDescriptionLengthChars,
            maxRequestsPerSecondCount=maxRequestsPerSecondCount,
            _configuration=_configuration,
            **kwargs,
        )
