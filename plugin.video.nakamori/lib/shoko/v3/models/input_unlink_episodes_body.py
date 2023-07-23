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


class InputUnlinkEpisodesBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Unlink the spesified episodes from a file.
    """


    class MetaOapg:
        required = {
            "EpisodeIDs",
        }
        
        class properties:
            
            
            class EpisodeIDs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int32Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EpisodeIDs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "EpisodeIDs": EpisodeIDs,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    EpisodeIDs: MetaOapg.properties.EpisodeIDs
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EpisodeIDs"]) -> MetaOapg.properties.EpisodeIDs: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["EpisodeIDs"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EpisodeIDs"]) -> MetaOapg.properties.EpisodeIDs: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["EpisodeIDs"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        EpisodeIDs: typing.Union[MetaOapg.properties.EpisodeIDs, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InputUnlinkEpisodesBody':
        return super().__new__(
            cls,
            *_args,
            EpisodeIDs=EpisodeIDs,
            _configuration=_configuration,
        )
