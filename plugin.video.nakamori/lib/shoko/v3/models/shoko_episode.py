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


class ShokoEpisode(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "Size",
            "Name",
        }
        
        class properties:
            
            
            class Name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            Size = schemas.Int32Schema
        
            @staticmethod
            def IDs() -> typing.Type['EpisodeEpisodeIDs']:
                return EpisodeEpisodeIDs
            Duration = schemas.StrSchema
            
            
            class ResumePosition(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-span'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ResumePosition':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Watched(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Watched':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            WatchCount = schemas.Int32Schema
            IsHidden = schemas.BoolSchema
        
            @staticmethod
            def AniDB() -> typing.Type['EpisodeAniDB']:
                return EpisodeAniDB
            
            
            class TvDB(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EpisodeTvDB']:
                        return EpisodeTvDB
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TvDB':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "Name": Name,
                "Size": Size,
                "IDs": IDs,
                "Duration": Duration,
                "ResumePosition": ResumePosition,
                "Watched": Watched,
                "WatchCount": WatchCount,
                "IsHidden": IsHidden,
                "AniDB": AniDB,
                "TvDB": TvDB,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    Size: MetaOapg.properties.Size
    Name: MetaOapg.properties.Name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Size"]) -> MetaOapg.properties.Size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IDs"]) -> 'EpisodeEpisodeIDs': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Duration"]) -> MetaOapg.properties.Duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ResumePosition"]) -> MetaOapg.properties.ResumePosition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Watched"]) -> MetaOapg.properties.Watched: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WatchCount"]) -> MetaOapg.properties.WatchCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsHidden"]) -> MetaOapg.properties.IsHidden: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AniDB"]) -> 'EpisodeAniDB': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TvDB"]) -> MetaOapg.properties.TvDB: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Size"], typing_extensions.Literal["Name"], typing_extensions.Literal["IDs"], typing_extensions.Literal["Duration"], typing_extensions.Literal["ResumePosition"], typing_extensions.Literal["Watched"], typing_extensions.Literal["WatchCount"], typing_extensions.Literal["IsHidden"], typing_extensions.Literal["AniDB"], typing_extensions.Literal["TvDB"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Size"]) -> MetaOapg.properties.Size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IDs"]) -> typing.Union['EpisodeEpisodeIDs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Duration"]) -> typing.Union[MetaOapg.properties.Duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ResumePosition"]) -> typing.Union[MetaOapg.properties.ResumePosition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Watched"]) -> typing.Union[MetaOapg.properties.Watched, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WatchCount"]) -> typing.Union[MetaOapg.properties.WatchCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsHidden"]) -> typing.Union[MetaOapg.properties.IsHidden, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AniDB"]) -> typing.Union['EpisodeAniDB', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TvDB"]) -> typing.Union[MetaOapg.properties.TvDB, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Size"], typing_extensions.Literal["Name"], typing_extensions.Literal["IDs"], typing_extensions.Literal["Duration"], typing_extensions.Literal["ResumePosition"], typing_extensions.Literal["Watched"], typing_extensions.Literal["WatchCount"], typing_extensions.Literal["IsHidden"], typing_extensions.Literal["AniDB"], typing_extensions.Literal["TvDB"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Size: typing.Union[MetaOapg.properties.Size, decimal.Decimal, int, ],
        Name: typing.Union[MetaOapg.properties.Name, str, ],
        IDs: typing.Union['EpisodeEpisodeIDs', schemas.Unset] = schemas.unset,
        Duration: typing.Union[MetaOapg.properties.Duration, str, schemas.Unset] = schemas.unset,
        ResumePosition: typing.Union[MetaOapg.properties.ResumePosition, None, str, schemas.Unset] = schemas.unset,
        Watched: typing.Union[MetaOapg.properties.Watched, None, str, datetime, schemas.Unset] = schemas.unset,
        WatchCount: typing.Union[MetaOapg.properties.WatchCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        IsHidden: typing.Union[MetaOapg.properties.IsHidden, bool, schemas.Unset] = schemas.unset,
        AniDB: typing.Union['EpisodeAniDB', schemas.Unset] = schemas.unset,
        TvDB: typing.Union[MetaOapg.properties.TvDB, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ShokoEpisode':
        return super().__new__(
            cls,
            *_args,
            Size=Size,
            Name=Name,
            IDs=IDs,
            Duration=Duration,
            ResumePosition=ResumePosition,
            Watched=Watched,
            WatchCount=WatchCount,
            IsHidden=IsHidden,
            AniDB=AniDB,
            TvDB=TvDB,
            _configuration=_configuration,
        )

from lib.shoko.v3.lib.shoko.v3.models.episode_ani_db import EpisodeAniDB
from lib.shoko.v3.lib.shoko.v3.models.episode_episode_ids import EpisodeEpisodeIDs
from lib.shoko.v3.lib.shoko.v3.models.episode_tv_db import EpisodeTvDB
