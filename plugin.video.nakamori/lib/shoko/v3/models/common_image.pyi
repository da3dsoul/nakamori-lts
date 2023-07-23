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


class CommonImage(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Image container
    """


    class MetaOapg:
        required = {
            "Type",
            "ID",
            "Source",
        }
        
        class properties:
        
            @staticmethod
            def Source() -> typing.Type['ImageImageSource']:
                return ImageImageSource
        
            @staticmethod
            def Type() -> typing.Type['ImageImageType']:
                return ImageImageType
            
            
            class ID(
                schemas.StrSchema
            ):
                pass
            
            
            class RelativeFilepath(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'RelativeFilepath':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            Preferred = schemas.BoolSchema
            
            
            class Width(
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
                ) -> 'Width':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Height(
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
                ) -> 'Height':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            Disabled = schemas.BoolSchema
        
            @staticmethod
            def Series() -> typing.Type['ImageImageSeriesInfo']:
                return ImageImageSeriesInfo
            __annotations__ = {
                "Source": Source,
                "Type": Type,
                "ID": ID,
                "RelativeFilepath": RelativeFilepath,
                "Preferred": Preferred,
                "Width": Width,
                "Height": Height,
                "Disabled": Disabled,
                "Series": Series,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    Type: 'ImageImageType'
    ID: MetaOapg.properties.ID
    Source: 'ImageImageSource'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> 'ImageImageType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Source"]) -> 'ImageImageSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RelativeFilepath"]) -> MetaOapg.properties.RelativeFilepath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Preferred"]) -> MetaOapg.properties.Preferred: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Width"]) -> MetaOapg.properties.Width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Height"]) -> MetaOapg.properties.Height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Disabled"]) -> MetaOapg.properties.Disabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Series"]) -> 'ImageImageSeriesInfo': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["ID"], typing_extensions.Literal["Source"], typing_extensions.Literal["RelativeFilepath"], typing_extensions.Literal["Preferred"], typing_extensions.Literal["Width"], typing_extensions.Literal["Height"], typing_extensions.Literal["Disabled"], typing_extensions.Literal["Series"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> 'ImageImageType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Source"]) -> 'ImageImageSource': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RelativeFilepath"]) -> typing.Union[MetaOapg.properties.RelativeFilepath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Preferred"]) -> typing.Union[MetaOapg.properties.Preferred, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Width"]) -> typing.Union[MetaOapg.properties.Width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Height"]) -> typing.Union[MetaOapg.properties.Height, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Disabled"]) -> typing.Union[MetaOapg.properties.Disabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Series"]) -> typing.Union['ImageImageSeriesInfo', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["ID"], typing_extensions.Literal["Source"], typing_extensions.Literal["RelativeFilepath"], typing_extensions.Literal["Preferred"], typing_extensions.Literal["Width"], typing_extensions.Literal["Height"], typing_extensions.Literal["Disabled"], typing_extensions.Literal["Series"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Type: 'ImageImageType',
        ID: typing.Union[MetaOapg.properties.ID, str, ],
        Source: 'ImageImageSource',
        RelativeFilepath: typing.Union[MetaOapg.properties.RelativeFilepath, None, str, schemas.Unset] = schemas.unset,
        Preferred: typing.Union[MetaOapg.properties.Preferred, bool, schemas.Unset] = schemas.unset,
        Width: typing.Union[MetaOapg.properties.Width, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Height: typing.Union[MetaOapg.properties.Height, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Disabled: typing.Union[MetaOapg.properties.Disabled, bool, schemas.Unset] = schemas.unset,
        Series: typing.Union['ImageImageSeriesInfo', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CommonImage':
        return super().__new__(
            cls,
            *_args,
            Type=Type,
            ID=ID,
            Source=Source,
            RelativeFilepath=RelativeFilepath,
            Preferred=Preferred,
            Width=Width,
            Height=Height,
            Disabled=Disabled,
            Series=Series,
            _configuration=_configuration,
        )

from lib.shoko.v3.lib.shoko.v3.models.image_image_series_info import ImageImageSeriesInfo
from lib.shoko.v3.lib.shoko.v3.models.image_image_source import ImageImageSource
from lib.shoko.v3.lib.shoko.v3.models.image_image_type import ImageImageType
