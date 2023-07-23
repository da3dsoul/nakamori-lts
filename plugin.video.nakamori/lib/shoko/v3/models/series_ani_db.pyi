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


class SeriesAniDB(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Basic anidb data across all anidb types.
    """


    class MetaOapg:
        required = {
            "Type",
            "Poster",
            "Title",
            "ID",
            "Titles",
        }
        
        class properties:
            ID = schemas.Int32Schema
            Type = schemas.StrSchema
            
            
            class Title(
                schemas.StrSchema
            ):
                pass
            
            
            class Titles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CommonTitle']:
                        return CommonTitle
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CommonTitle'], typing.List['CommonTitle']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Titles':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CommonTitle':
                    return super().__getitem__(i)
        
            @staticmethod
            def Poster() -> typing.Type['CommonImage']:
                return CommonImage
            
            
            class ShokoID(
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
                ) -> 'ShokoID':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            Restricted = schemas.BoolSchema
            
            
            class EpisodeCount(
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
                ) -> 'EpisodeCount':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Rating() -> typing.Type['CommonRating']:
                return CommonRating
        
            @staticmethod
            def UserApproval() -> typing.Type['CommonRating']:
                return CommonRating
        
            @staticmethod
            def Relation() -> typing.Type['DataModelsRelationType']:
                return DataModelsRelationType
            __annotations__ = {
                "ID": ID,
                "Type": Type,
                "Title": Title,
                "Titles": Titles,
                "Poster": Poster,
                "ShokoID": ShokoID,
                "Description": Description,
                "Restricted": Restricted,
                "EpisodeCount": EpisodeCount,
                "Rating": Rating,
                "UserApproval": UserApproval,
                "Relation": Relation,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    Type: MetaOapg.properties.Type
    Poster: 'CommonImage'
    Title: MetaOapg.properties.Title
    ID: MetaOapg.properties.ID
    Titles: MetaOapg.properties.Titles
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Poster"]) -> 'CommonImage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Title"]) -> MetaOapg.properties.Title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Titles"]) -> MetaOapg.properties.Titles: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ShokoID"]) -> MetaOapg.properties.ShokoID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Restricted"]) -> MetaOapg.properties.Restricted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EpisodeCount"]) -> MetaOapg.properties.EpisodeCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rating"]) -> 'CommonRating': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UserApproval"]) -> 'CommonRating': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Relation"]) -> 'DataModelsRelationType': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Poster"], typing_extensions.Literal["Title"], typing_extensions.Literal["ID"], typing_extensions.Literal["Titles"], typing_extensions.Literal["ShokoID"], typing_extensions.Literal["Description"], typing_extensions.Literal["Restricted"], typing_extensions.Literal["EpisodeCount"], typing_extensions.Literal["Rating"], typing_extensions.Literal["UserApproval"], typing_extensions.Literal["Relation"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Poster"]) -> 'CommonImage': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Title"]) -> MetaOapg.properties.Title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Titles"]) -> MetaOapg.properties.Titles: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ShokoID"]) -> typing.Union[MetaOapg.properties.ShokoID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union[MetaOapg.properties.Description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Restricted"]) -> typing.Union[MetaOapg.properties.Restricted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EpisodeCount"]) -> typing.Union[MetaOapg.properties.EpisodeCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Rating"]) -> typing.Union['CommonRating', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UserApproval"]) -> typing.Union['CommonRating', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Relation"]) -> typing.Union['DataModelsRelationType', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Poster"], typing_extensions.Literal["Title"], typing_extensions.Literal["ID"], typing_extensions.Literal["Titles"], typing_extensions.Literal["ShokoID"], typing_extensions.Literal["Description"], typing_extensions.Literal["Restricted"], typing_extensions.Literal["EpisodeCount"], typing_extensions.Literal["Rating"], typing_extensions.Literal["UserApproval"], typing_extensions.Literal["Relation"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        Poster: 'CommonImage',
        Title: typing.Union[MetaOapg.properties.Title, str, ],
        ID: typing.Union[MetaOapg.properties.ID, decimal.Decimal, int, ],
        Titles: typing.Union[MetaOapg.properties.Titles, list, tuple, ],
        ShokoID: typing.Union[MetaOapg.properties.ShokoID, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Description: typing.Union[MetaOapg.properties.Description, None, str, schemas.Unset] = schemas.unset,
        Restricted: typing.Union[MetaOapg.properties.Restricted, bool, schemas.Unset] = schemas.unset,
        EpisodeCount: typing.Union[MetaOapg.properties.EpisodeCount, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Rating: typing.Union['CommonRating', schemas.Unset] = schemas.unset,
        UserApproval: typing.Union['CommonRating', schemas.Unset] = schemas.unset,
        Relation: typing.Union['DataModelsRelationType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SeriesAniDB':
        return super().__new__(
            cls,
            *_args,
            Type=Type,
            Poster=Poster,
            Title=Title,
            ID=ID,
            Titles=Titles,
            ShokoID=ShokoID,
            Description=Description,
            Restricted=Restricted,
            EpisodeCount=EpisodeCount,
            Rating=Rating,
            UserApproval=UserApproval,
            Relation=Relation,
            _configuration=_configuration,
        )

from lib.shoko.v3.lib.shoko.v3.models.common_image import CommonImage
from lib.shoko.v3.lib.shoko.v3.models.common_rating import CommonRating
from lib.shoko.v3.lib.shoko.v3.models.common_title import CommonTitle
from lib.shoko.v3.lib.shoko.v3.models.data_models_relation_type import DataModelsRelationType
