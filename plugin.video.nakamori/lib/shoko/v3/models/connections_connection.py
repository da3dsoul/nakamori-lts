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


class ConnectionsConnection(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class Protocol(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Protocol':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Address(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Address':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Port(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Port':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Uri(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Uri':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Local(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Local':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "Protocol": Protocol,
                "Address": Address,
                "Port": Port,
                "Uri": Uri,
                "Local": Local,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Protocol"]) -> MetaOapg.properties.Protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address"]) -> MetaOapg.properties.Address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Port"]) -> MetaOapg.properties.Port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Uri"]) -> MetaOapg.properties.Uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Local"]) -> MetaOapg.properties.Local: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Protocol"], typing_extensions.Literal["Address"], typing_extensions.Literal["Port"], typing_extensions.Literal["Uri"], typing_extensions.Literal["Local"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Protocol"]) -> typing.Union[MetaOapg.properties.Protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address"]) -> typing.Union[MetaOapg.properties.Address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Port"]) -> typing.Union[MetaOapg.properties.Port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Uri"]) -> typing.Union[MetaOapg.properties.Uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Local"]) -> typing.Union[MetaOapg.properties.Local, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Protocol"], typing_extensions.Literal["Address"], typing_extensions.Literal["Port"], typing_extensions.Literal["Uri"], typing_extensions.Literal["Local"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Protocol: typing.Union[MetaOapg.properties.Protocol, None, str, schemas.Unset] = schemas.unset,
        Address: typing.Union[MetaOapg.properties.Address, None, str, schemas.Unset] = schemas.unset,
        Port: typing.Union[MetaOapg.properties.Port, None, str, schemas.Unset] = schemas.unset,
        Uri: typing.Union[MetaOapg.properties.Uri, None, str, schemas.Unset] = schemas.unset,
        Local: typing.Union[MetaOapg.properties.Local, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ConnectionsConnection':
        return super().__new__(
            cls,
            *_args,
            Protocol=Protocol,
            Address=Address,
            Port=Port,
            Uri=Uri,
            Local=Local,
            _configuration=_configuration,
        )
