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


class GroupGroupIDs(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "ID",
        }
        
        class properties:
            ID = schemas.Int32Schema
            
            
            class DefaultSeries(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'DefaultSeries':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            MainSeries = schemas.Int32Schema
            
            
            class ParentGroup(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ParentGroup':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            TopLevelGroup = schemas.Int32Schema
            __annotations__ = {
                "ID": ID,
                "DefaultSeries": DefaultSeries,
                "MainSeries": MainSeries,
                "ParentGroup": ParentGroup,
                "TopLevelGroup": TopLevelGroup,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    ID: MetaOapg.properties.ID
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DefaultSeries"]) -> MetaOapg.properties.DefaultSeries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MainSeries"]) -> MetaOapg.properties.MainSeries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParentGroup"]) -> MetaOapg.properties.ParentGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TopLevelGroup"]) -> MetaOapg.properties.TopLevelGroup: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ID"], typing_extensions.Literal["DefaultSeries"], typing_extensions.Literal["MainSeries"], typing_extensions.Literal["ParentGroup"], typing_extensions.Literal["TopLevelGroup"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DefaultSeries"]) -> typing.Union[MetaOapg.properties.DefaultSeries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MainSeries"]) -> typing.Union[MetaOapg.properties.MainSeries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParentGroup"]) -> typing.Union[MetaOapg.properties.ParentGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TopLevelGroup"]) -> typing.Union[MetaOapg.properties.TopLevelGroup, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ID"], typing_extensions.Literal["DefaultSeries"], typing_extensions.Literal["MainSeries"], typing_extensions.Literal["ParentGroup"], typing_extensions.Literal["TopLevelGroup"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ID: typing.Union[MetaOapg.properties.ID, decimal.Decimal, int, ],
        DefaultSeries: typing.Union[MetaOapg.properties.DefaultSeries, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        MainSeries: typing.Union[MetaOapg.properties.MainSeries, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ParentGroup: typing.Union[MetaOapg.properties.ParentGroup, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TopLevelGroup: typing.Union[MetaOapg.properties.TopLevelGroup, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'GroupGroupIDs':
        return super().__new__(
            cls,
            *_args,
            ID=ID,
            DefaultSeries=DefaultSeries,
            MainSeries=MainSeries,
            ParentGroup=ParentGroup,
            TopLevelGroup=TopLevelGroup,
            _configuration=_configuration,
        )
