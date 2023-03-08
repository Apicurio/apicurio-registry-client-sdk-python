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


class ArtifactSearchResults(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Describes the response received when searching for artifacts.
    """


    class MetaOapg:
        required = {
            "count",
            "artifacts",
        }
        
        class properties:
            
            
            class artifacts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SearchedArtifact']:
                        return SearchedArtifact
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SearchedArtifact'], typing.List['SearchedArtifact']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'artifacts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SearchedArtifact':
                    return super().__getitem__(i)
            count = schemas.IntSchema
            __annotations__ = {
                "artifacts": artifacts,
                "count": count,
            }
    
    count: MetaOapg.properties.count
    artifacts: MetaOapg.properties.artifacts
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["artifacts"]) -> MetaOapg.properties.artifacts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["artifacts", "count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["artifacts"]) -> MetaOapg.properties.artifacts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["artifacts", "count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, ],
        artifacts: typing.Union[MetaOapg.properties.artifacts, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArtifactSearchResults':
        return super().__new__(
            cls,
            *_args,
            count=count,
            artifacts=artifacts,
            _configuration=_configuration,
            **kwargs,
        )

from apicurioregistryclient.model.searched_artifact import SearchedArtifact
