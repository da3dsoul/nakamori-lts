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


class InputCreateOrUpdateFilterBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Used for creating new filters, updating existing filters, and/or
updating the live filter.
    """


    class MetaOapg:
        
        class properties:
            
            
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
            IsDirectory = schemas.BoolSchema
            IsInverted = schemas.BoolSchema
            IsHidden = schemas.BoolSchema
            ApplyAtSeriesLevel = schemas.BoolSchema
            
            
            class Conditions(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FilterFilterCondition']:
                        return FilterFilterCondition
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Conditions':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Sorting(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FilterSortingCriteria']:
                        return FilterSortingCriteria
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Sorting':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "Name": Name,
                "ParentID": ParentID,
                "IsDirectory": IsDirectory,
                "IsInverted": IsInverted,
                "IsHidden": IsHidden,
                "ApplyAtSeriesLevel": ApplyAtSeriesLevel,
                "Conditions": Conditions,
                "Sorting": Sorting,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParentID"]) -> MetaOapg.properties.ParentID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsDirectory"]) -> MetaOapg.properties.IsDirectory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsInverted"]) -> MetaOapg.properties.IsInverted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsHidden"]) -> MetaOapg.properties.IsHidden: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApplyAtSeriesLevel"]) -> MetaOapg.properties.ApplyAtSeriesLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Conditions"]) -> MetaOapg.properties.Conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Sorting"]) -> MetaOapg.properties.Sorting: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Name"], typing_extensions.Literal["ParentID"], typing_extensions.Literal["IsDirectory"], typing_extensions.Literal["IsInverted"], typing_extensions.Literal["IsHidden"], typing_extensions.Literal["ApplyAtSeriesLevel"], typing_extensions.Literal["Conditions"], typing_extensions.Literal["Sorting"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParentID"]) -> typing.Union[MetaOapg.properties.ParentID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsDirectory"]) -> typing.Union[MetaOapg.properties.IsDirectory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsInverted"]) -> typing.Union[MetaOapg.properties.IsInverted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsHidden"]) -> typing.Union[MetaOapg.properties.IsHidden, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApplyAtSeriesLevel"]) -> typing.Union[MetaOapg.properties.ApplyAtSeriesLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Conditions"]) -> typing.Union[MetaOapg.properties.Conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Sorting"]) -> typing.Union[MetaOapg.properties.Sorting, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Name"], typing_extensions.Literal["ParentID"], typing_extensions.Literal["IsDirectory"], typing_extensions.Literal["IsInverted"], typing_extensions.Literal["IsHidden"], typing_extensions.Literal["ApplyAtSeriesLevel"], typing_extensions.Literal["Conditions"], typing_extensions.Literal["Sorting"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Name: typing.Union[MetaOapg.properties.Name, None, str, schemas.Unset] = schemas.unset,
        ParentID: typing.Union[MetaOapg.properties.ParentID, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        IsDirectory: typing.Union[MetaOapg.properties.IsDirectory, bool, schemas.Unset] = schemas.unset,
        IsInverted: typing.Union[MetaOapg.properties.IsInverted, bool, schemas.Unset] = schemas.unset,
        IsHidden: typing.Union[MetaOapg.properties.IsHidden, bool, schemas.Unset] = schemas.unset,
        ApplyAtSeriesLevel: typing.Union[MetaOapg.properties.ApplyAtSeriesLevel, bool, schemas.Unset] = schemas.unset,
        Conditions: typing.Union[MetaOapg.properties.Conditions, list, tuple, None, schemas.Unset] = schemas.unset,
        Sorting: typing.Union[MetaOapg.properties.Sorting, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InputCreateOrUpdateFilterBody':
        return super().__new__(
            cls,
            *_args,
            Name=Name,
            ParentID=ParentID,
            IsDirectory=IsDirectory,
            IsInverted=IsInverted,
            IsHidden=IsHidden,
            ApplyAtSeriesLevel=ApplyAtSeriesLevel,
            Conditions=Conditions,
            Sorting=Sorting,
            _configuration=_configuration,
        )

from lib.shoko.v3.lib.shoko.v3.models.filter_filter_condition import FilterFilterCondition
from lib.shoko.v3.lib.shoko.v3.models.filter_sorting_criteria import FilterSortingCriteria
