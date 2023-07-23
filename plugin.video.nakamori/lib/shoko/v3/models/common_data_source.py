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


class CommonDataSource(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Available data sources to chose from.
    """


    class MetaOapg:
        enum_value_to_name = {
            "None": "NONE",
            "AniDB": "ANI_DB",
            "TvDB": "TV_DB",
            "TMDB": "TMDB",
            "Trakt": "TRAKT",
            "MAL": "MAL",
            "AniList": "ANI_LIST",
            "Animeshon": "ANIMESHON",
            "Kitsu": "KITSU",
            "Shoko": "SHOKO",
        }
    
    @schemas.classproperty
    def NONE(cls):
        return cls("None")
    
    @schemas.classproperty
    def ANI_DB(cls):
        return cls("AniDB")
    
    @schemas.classproperty
    def TV_DB(cls):
        return cls("TvDB")
    
    @schemas.classproperty
    def TMDB(cls):
        return cls("TMDB")
    
    @schemas.classproperty
    def TRAKT(cls):
        return cls("Trakt")
    
    @schemas.classproperty
    def MAL(cls):
        return cls("MAL")
    
    @schemas.classproperty
    def ANI_LIST(cls):
        return cls("AniList")
    
    @schemas.classproperty
    def ANIMESHON(cls):
        return cls("Animeshon")
    
    @schemas.classproperty
    def KITSU(cls):
        return cls("Kitsu")
    
    @schemas.classproperty
    def SHOKO(cls):
        return cls("Shoko")
