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


class SeriesAutoMatchSettings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Auto-matching settings for the series.
    """


    class MetaOapg:
        required = {
            "TMDB",
            "TvDB",
            "Trakt",
        }
        
        class properties:
            TvDB = schemas.BoolSchema
            TMDB = schemas.BoolSchema
            Trakt = schemas.BoolSchema
            __annotations__ = {
                "TvDB": TvDB,
                "TMDB": TMDB,
                "Trakt": Trakt,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    TMDB: MetaOapg.properties.TMDB
    TvDB: MetaOapg.properties.TvDB
    Trakt: MetaOapg.properties.Trakt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TMDB"]) -> MetaOapg.properties.TMDB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TvDB"]) -> MetaOapg.properties.TvDB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Trakt"]) -> MetaOapg.properties.Trakt: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TMDB"], typing_extensions.Literal["TvDB"], typing_extensions.Literal["Trakt"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TMDB"]) -> MetaOapg.properties.TMDB: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TvDB"]) -> MetaOapg.properties.TvDB: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Trakt"]) -> MetaOapg.properties.Trakt: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TMDB"], typing_extensions.Literal["TvDB"], typing_extensions.Literal["Trakt"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        TMDB: typing.Union[MetaOapg.properties.TMDB, bool, ],
        TvDB: typing.Union[MetaOapg.properties.TvDB, bool, ],
        Trakt: typing.Union[MetaOapg.properties.Trakt, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SeriesAutoMatchSettings':
        return super().__new__(
            cls,
            *_args,
            TMDB=TMDB,
            TvDB=TvDB,
            Trakt=Trakt,
            _configuration=_configuration,
        )
