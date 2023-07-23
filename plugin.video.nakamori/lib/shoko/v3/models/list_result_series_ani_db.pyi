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


class ListResultSeriesAniDB(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A list with the total count of <typeparamref name="T" /> entries that
match the filter and a sliced or the full list of <typeparamref name="T" />
entries.
    """


    class MetaOapg:
        
        class properties:
            Total = schemas.Int32Schema
            
            
            class _list(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SeriesAniDB']:
                        return SeriesAniDB
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> '_list':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "Total": Total,
                "List": _list,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Total"]) -> MetaOapg.properties.Total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["List"]) -> MetaOapg.properties._list: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Total"], typing_extensions.Literal["List"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Total"]) -> typing.Union[MetaOapg.properties.Total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["List"]) -> typing.Union[MetaOapg.properties._list, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Total"], typing_extensions.Literal["List"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Total: typing.Union[MetaOapg.properties.Total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ListResultSeriesAniDB':
        return super().__new__(
            cls,
            *_args,
            Total=Total,
            _configuration=_configuration,
        )

from lib.shoko.v3.lib.shoko.v3.models.series_ani_db import SeriesAniDB
