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


class InputCreateOrUpdateGroupBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class ParentID(
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
                ) -> 'ParentID':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class DefaultSeriesID(
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
                ) -> 'DefaultSeriesID':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class SeriesIDs(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.Int32Schema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SeriesIDs':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class ChildIDs(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.Int32Schema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ChildIDs':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
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
            
            
            class SortName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SortName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class HasCustomName(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'HasCustomName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class HasCustomDescription(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'HasCustomDescription':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "ParentID": ParentID,
                "DefaultSeriesID": DefaultSeriesID,
                "SeriesIDs": SeriesIDs,
                "ChildIDs": ChildIDs,
                "Name": Name,
                "SortName": SortName,
                "Description": Description,
                "HasCustomName": HasCustomName,
                "HasCustomDescription": HasCustomDescription,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParentID"]) -> MetaOapg.properties.ParentID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DefaultSeriesID"]) -> MetaOapg.properties.DefaultSeriesID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SeriesIDs"]) -> MetaOapg.properties.SeriesIDs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ChildIDs"]) -> MetaOapg.properties.ChildIDs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SortName"]) -> MetaOapg.properties.SortName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HasCustomName"]) -> MetaOapg.properties.HasCustomName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HasCustomDescription"]) -> MetaOapg.properties.HasCustomDescription: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ParentID"], typing_extensions.Literal["DefaultSeriesID"], typing_extensions.Literal["SeriesIDs"], typing_extensions.Literal["ChildIDs"], typing_extensions.Literal["Name"], typing_extensions.Literal["SortName"], typing_extensions.Literal["Description"], typing_extensions.Literal["HasCustomName"], typing_extensions.Literal["HasCustomDescription"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParentID"]) -> typing.Union[MetaOapg.properties.ParentID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DefaultSeriesID"]) -> typing.Union[MetaOapg.properties.DefaultSeriesID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SeriesIDs"]) -> typing.Union[MetaOapg.properties.SeriesIDs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ChildIDs"]) -> typing.Union[MetaOapg.properties.ChildIDs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SortName"]) -> typing.Union[MetaOapg.properties.SortName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union[MetaOapg.properties.Description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HasCustomName"]) -> typing.Union[MetaOapg.properties.HasCustomName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HasCustomDescription"]) -> typing.Union[MetaOapg.properties.HasCustomDescription, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ParentID"], typing_extensions.Literal["DefaultSeriesID"], typing_extensions.Literal["SeriesIDs"], typing_extensions.Literal["ChildIDs"], typing_extensions.Literal["Name"], typing_extensions.Literal["SortName"], typing_extensions.Literal["Description"], typing_extensions.Literal["HasCustomName"], typing_extensions.Literal["HasCustomDescription"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ParentID: typing.Union[MetaOapg.properties.ParentID, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        DefaultSeriesID: typing.Union[MetaOapg.properties.DefaultSeriesID, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        SeriesIDs: typing.Union[MetaOapg.properties.SeriesIDs, list, tuple, None, schemas.Unset] = schemas.unset,
        ChildIDs: typing.Union[MetaOapg.properties.ChildIDs, list, tuple, None, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, None, str, schemas.Unset] = schemas.unset,
        SortName: typing.Union[MetaOapg.properties.SortName, None, str, schemas.Unset] = schemas.unset,
        Description: typing.Union[MetaOapg.properties.Description, None, str, schemas.Unset] = schemas.unset,
        HasCustomName: typing.Union[MetaOapg.properties.HasCustomName, None, bool, schemas.Unset] = schemas.unset,
        HasCustomDescription: typing.Union[MetaOapg.properties.HasCustomDescription, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InputCreateOrUpdateGroupBody':
        return super().__new__(
            cls,
            *_args,
            ParentID=ParentID,
            DefaultSeriesID=DefaultSeriesID,
            SeriesIDs=SeriesIDs,
            ChildIDs=ChildIDs,
            Name=Name,
            SortName=SortName,
            Description=Description,
            HasCustomName=HasCustomName,
            HasCustomDescription=HasCustomDescription,
            _configuration=_configuration,
        )
