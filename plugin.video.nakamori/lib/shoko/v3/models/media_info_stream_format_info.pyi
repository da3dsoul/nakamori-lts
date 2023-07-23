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


class MediaInfoStreamFormatInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
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
            
            
            class Profile(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Profile':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Level(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Level':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Settings(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Settings':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class AdditionalFeatures(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AdditionalFeatures':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Endianness(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Endianness':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Tier(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Tier':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Commercial(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Commercial':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class HDR(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'HDR':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class HDRCompatibility(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'HDRCompatibility':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class CABAC(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'CABAC':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class BVOP(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'BVOP':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class QPel(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'QPel':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class GMC(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'GMC':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class ReferenceFrames(
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
                ) -> 'ReferenceFrames':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "Name": Name,
                "Profile": Profile,
                "Level": Level,
                "Settings": Settings,
                "AdditionalFeatures": AdditionalFeatures,
                "Endianness": Endianness,
                "Tier": Tier,
                "Commercial": Commercial,
                "HDR": HDR,
                "HDRCompatibility": HDRCompatibility,
                "CABAC": CABAC,
                "BVOP": BVOP,
                "QPel": QPel,
                "GMC": GMC,
                "ReferenceFrames": ReferenceFrames,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Profile"]) -> MetaOapg.properties.Profile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Level"]) -> MetaOapg.properties.Level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Settings"]) -> MetaOapg.properties.Settings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AdditionalFeatures"]) -> MetaOapg.properties.AdditionalFeatures: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Endianness"]) -> MetaOapg.properties.Endianness: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Tier"]) -> MetaOapg.properties.Tier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Commercial"]) -> MetaOapg.properties.Commercial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HDR"]) -> MetaOapg.properties.HDR: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HDRCompatibility"]) -> MetaOapg.properties.HDRCompatibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CABAC"]) -> MetaOapg.properties.CABAC: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BVOP"]) -> MetaOapg.properties.BVOP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QPel"]) -> MetaOapg.properties.QPel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["GMC"]) -> MetaOapg.properties.GMC: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ReferenceFrames"]) -> MetaOapg.properties.ReferenceFrames: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Name"], typing_extensions.Literal["Profile"], typing_extensions.Literal["Level"], typing_extensions.Literal["Settings"], typing_extensions.Literal["AdditionalFeatures"], typing_extensions.Literal["Endianness"], typing_extensions.Literal["Tier"], typing_extensions.Literal["Commercial"], typing_extensions.Literal["HDR"], typing_extensions.Literal["HDRCompatibility"], typing_extensions.Literal["CABAC"], typing_extensions.Literal["BVOP"], typing_extensions.Literal["QPel"], typing_extensions.Literal["GMC"], typing_extensions.Literal["ReferenceFrames"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Profile"]) -> typing.Union[MetaOapg.properties.Profile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Level"]) -> typing.Union[MetaOapg.properties.Level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Settings"]) -> typing.Union[MetaOapg.properties.Settings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AdditionalFeatures"]) -> typing.Union[MetaOapg.properties.AdditionalFeatures, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Endianness"]) -> typing.Union[MetaOapg.properties.Endianness, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Tier"]) -> typing.Union[MetaOapg.properties.Tier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Commercial"]) -> typing.Union[MetaOapg.properties.Commercial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HDR"]) -> typing.Union[MetaOapg.properties.HDR, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HDRCompatibility"]) -> typing.Union[MetaOapg.properties.HDRCompatibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CABAC"]) -> typing.Union[MetaOapg.properties.CABAC, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BVOP"]) -> typing.Union[MetaOapg.properties.BVOP, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QPel"]) -> typing.Union[MetaOapg.properties.QPel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["GMC"]) -> typing.Union[MetaOapg.properties.GMC, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ReferenceFrames"]) -> typing.Union[MetaOapg.properties.ReferenceFrames, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Name"], typing_extensions.Literal["Profile"], typing_extensions.Literal["Level"], typing_extensions.Literal["Settings"], typing_extensions.Literal["AdditionalFeatures"], typing_extensions.Literal["Endianness"], typing_extensions.Literal["Tier"], typing_extensions.Literal["Commercial"], typing_extensions.Literal["HDR"], typing_extensions.Literal["HDRCompatibility"], typing_extensions.Literal["CABAC"], typing_extensions.Literal["BVOP"], typing_extensions.Literal["QPel"], typing_extensions.Literal["GMC"], typing_extensions.Literal["ReferenceFrames"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Name: typing.Union[MetaOapg.properties.Name, None, str, schemas.Unset] = schemas.unset,
        Profile: typing.Union[MetaOapg.properties.Profile, None, str, schemas.Unset] = schemas.unset,
        Level: typing.Union[MetaOapg.properties.Level, None, str, schemas.Unset] = schemas.unset,
        Settings: typing.Union[MetaOapg.properties.Settings, None, str, schemas.Unset] = schemas.unset,
        AdditionalFeatures: typing.Union[MetaOapg.properties.AdditionalFeatures, None, str, schemas.Unset] = schemas.unset,
        Endianness: typing.Union[MetaOapg.properties.Endianness, None, str, schemas.Unset] = schemas.unset,
        Tier: typing.Union[MetaOapg.properties.Tier, None, str, schemas.Unset] = schemas.unset,
        Commercial: typing.Union[MetaOapg.properties.Commercial, None, str, schemas.Unset] = schemas.unset,
        HDR: typing.Union[MetaOapg.properties.HDR, None, str, schemas.Unset] = schemas.unset,
        HDRCompatibility: typing.Union[MetaOapg.properties.HDRCompatibility, None, str, schemas.Unset] = schemas.unset,
        CABAC: typing.Union[MetaOapg.properties.CABAC, None, bool, schemas.Unset] = schemas.unset,
        BVOP: typing.Union[MetaOapg.properties.BVOP, None, bool, schemas.Unset] = schemas.unset,
        QPel: typing.Union[MetaOapg.properties.QPel, None, bool, schemas.Unset] = schemas.unset,
        GMC: typing.Union[MetaOapg.properties.GMC, None, str, schemas.Unset] = schemas.unset,
        ReferenceFrames: typing.Union[MetaOapg.properties.ReferenceFrames, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MediaInfoStreamFormatInfo':
        return super().__new__(
            cls,
            *_args,
            Name=Name,
            Profile=Profile,
            Level=Level,
            Settings=Settings,
            AdditionalFeatures=AdditionalFeatures,
            Endianness=Endianness,
            Tier=Tier,
            Commercial=Commercial,
            HDR=HDR,
            HDRCompatibility=HDRCompatibility,
            CABAC=CABAC,
            BVOP=BVOP,
            QPel=QPel,
            GMC=GMC,
            ReferenceFrames=ReferenceFrames,
            _configuration=_configuration,
        )
