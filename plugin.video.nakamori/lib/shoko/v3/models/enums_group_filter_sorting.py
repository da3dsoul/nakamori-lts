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


class EnumsGroupFilterSorting(
    schemas.EnumBase,
    schemas.Int32Schema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        format = 'int32'
        enum_value_to_name = {
            1: "POSITIVE_1",
            2: "POSITIVE_2",
            3: "POSITIVE_3",
            4: "POSITIVE_4",
            5: "POSITIVE_5",
            6: "POSITIVE_6",
            7: "POSITIVE_7",
            8: "POSITIVE_8",
            9: "POSITIVE_9",
            10: "POSITIVE_10",
            11: "POSITIVE_11",
            12: "POSITIVE_12",
            13: "POSITIVE_13",
        }
    
    @schemas.classproperty
    def POSITIVE_1(cls):
        return cls(1)
    
    @schemas.classproperty
    def POSITIVE_2(cls):
        return cls(2)
    
    @schemas.classproperty
    def POSITIVE_3(cls):
        return cls(3)
    
    @schemas.classproperty
    def POSITIVE_4(cls):
        return cls(4)
    
    @schemas.classproperty
    def POSITIVE_5(cls):
        return cls(5)
    
    @schemas.classproperty
    def POSITIVE_6(cls):
        return cls(6)
    
    @schemas.classproperty
    def POSITIVE_7(cls):
        return cls(7)
    
    @schemas.classproperty
    def POSITIVE_8(cls):
        return cls(8)
    
    @schemas.classproperty
    def POSITIVE_9(cls):
        return cls(9)
    
    @schemas.classproperty
    def POSITIVE_10(cls):
        return cls(10)
    
    @schemas.classproperty
    def POSITIVE_11(cls):
        return cls(11)
    
    @schemas.classproperty
    def POSITIVE_12(cls):
        return cls(12)
    
    @schemas.classproperty
    def POSITIVE_13(cls):
        return cls(13)
