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


class EpisodeEpisodeIDs(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "ID",
            "AniDB",
        }
        
        class properties:
            AniDB = schemas.Int32Schema
            ID = schemas.Int32Schema
            ParentSeries = schemas.Int32Schema
            
            
            class TvDB(
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
                ) -> 'TvDB':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "AniDB": AniDB,
                "ID": ID,
                "ParentSeries": ParentSeries,
                "TvDB": TvDB,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    ID: MetaOapg.properties.ID
    AniDB: MetaOapg.properties.AniDB
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AniDB"]) -> MetaOapg.properties.AniDB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParentSeries"]) -> MetaOapg.properties.ParentSeries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TvDB"]) -> MetaOapg.properties.TvDB: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ID"], typing_extensions.Literal["AniDB"], typing_extensions.Literal["ParentSeries"], typing_extensions.Literal["TvDB"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AniDB"]) -> MetaOapg.properties.AniDB: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParentSeries"]) -> typing.Union[MetaOapg.properties.ParentSeries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TvDB"]) -> typing.Union[MetaOapg.properties.TvDB, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ID"], typing_extensions.Literal["AniDB"], typing_extensions.Literal["ParentSeries"], typing_extensions.Literal["TvDB"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ID: typing.Union[MetaOapg.properties.ID, decimal.Decimal, int, ],
        AniDB: typing.Union[MetaOapg.properties.AniDB, decimal.Decimal, int, ],
        ParentSeries: typing.Union[MetaOapg.properties.ParentSeries, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TvDB: typing.Union[MetaOapg.properties.TvDB, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EpisodeEpisodeIDs':
        return super().__new__(
            cls,
            *_args,
            ID=ID,
            AniDB=AniDB,
            ParentSeries=ParentSeries,
            TvDB=TvDB,
            _configuration=_configuration,
        )
