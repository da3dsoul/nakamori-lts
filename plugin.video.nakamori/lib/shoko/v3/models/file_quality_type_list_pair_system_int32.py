# coding: utf-8

"""
    Shoko API 3

    Shoko Server API.  # noqa: E501

    The version of the OpenAPI document: 3
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

from lib.shoko.v3 import schemas  # noqa: F401


class FileQualityTypeListPairSystemInt32(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def Operator() -> typing.Type['EnumsFileQualityFilterOperationType']:
                return EnumsFileQualityFilterOperationType
            Value = schemas.Int32Schema
            __annotations__ = {
                "Operator": Operator,
                "Value": Value,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Operator"]) -> 'EnumsFileQualityFilterOperationType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Value"]) -> MetaOapg.properties.Value: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Operator"], typing_extensions.Literal["Value"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Operator"]) -> typing.Union['EnumsFileQualityFilterOperationType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Value"]) -> typing.Union[MetaOapg.properties.Value, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Operator"], typing_extensions.Literal["Value"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Operator: typing.Union['EnumsFileQualityFilterOperationType', schemas.Unset] = schemas.unset,
        Value: typing.Union[MetaOapg.properties.Value, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FileQualityTypeListPairSystemInt32':
        return super().__new__(
            cls,
            *_args,
            Operator=Operator,
            Value=Value,
            _configuration=_configuration,
        )

from lib.shoko.v3.lib.shoko.v3.models.enums_file_quality_filter_operation_type import EnumsFileQualityFilterOperationType
