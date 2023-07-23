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


class TagFilterFilter(
    schemas.EnumBase,
    schemas.Int64Schema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def POSITIVE_0(cls):
        return cls(0)
    
    @schemas.classproperty
    def POSITIVE_1(cls):
        return cls(1)
    
    @schemas.classproperty
    def POSITIVE_2(cls):
        return cls(2)
    
    @schemas.classproperty
    def POSITIVE_4(cls):
        return cls(4)
    
    @schemas.classproperty
    def POSITIVE_8(cls):
        return cls(8)
    
    @schemas.classproperty
    def POSITIVE_16(cls):
        return cls(16)
    
    @schemas.classproperty
    def POSITIVE_32(cls):
        return cls(32)
    
    @schemas.classproperty
    def POSITIVE_64(cls):
        return cls(64)
    
    @schemas.classproperty
    def POSITIVE_128(cls):
        return cls(128)
    
    @schemas.classproperty
    def POSITIVE_1073741824(cls):
        return cls(1073741824)
    
    @schemas.classproperty
    def POSITIVE_2147483648(cls):
        return cls(2147483648)
