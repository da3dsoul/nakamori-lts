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


class ImageImageSeriesInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            ID = schemas.Int32Schema
            
            
            class Name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "ID": ID,
                "Name": Name,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ID"], typing_extensions.Literal["Name"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> typing.Union[MetaOapg.properties.ID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ID"], typing_extensions.Literal["Name"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ID: typing.Union[MetaOapg.properties.ID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ImageImageSeriesInfo':
        return super().__new__(
            cls,
            *_args,
            ID=ID,
            Name=Name,
            _configuration=_configuration,
        )
