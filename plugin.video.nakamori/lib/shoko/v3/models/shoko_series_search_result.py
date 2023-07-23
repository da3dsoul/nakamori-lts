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


class ShokoSeriesSearchResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An Extended Series Model with Values for Search Results
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
            ExactMatch = schemas.BoolSchema
            Index = schemas.Int32Schema
            Distance = schemas.Float64Schema
            LengthDifference = schemas.Int32Schema
            
            
            class Match(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Match':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def IDs() -> typing.Type['ShokoSeriesIDs']:
                return ShokoSeriesIDs
        
            @staticmethod
            def Images() -> typing.Type['CommonImages']:
                return CommonImages
        
            @staticmethod
            def UserRating() -> typing.Type['CommonRating']:
                return CommonRating
            
            
            class AirsOn(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SystemDayOfWeek']:
                        return SystemDayOfWeek
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AirsOn':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Links(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SeriesResource']:
                        return SeriesResource
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Links':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Sizes() -> typing.Type['ShokoSeriesSizes']:
                return ShokoSeriesSizes
            Created = schemas.DateTimeSchema
            Updated = schemas.DateTimeSchema
        
            @staticmethod
            def AniDB() -> typing.Type['SeriesAniDBWithDate']:
                return SeriesAniDBWithDate
            
            
            class TvDB(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SeriesTvDB']:
                        return SeriesTvDB
            
            
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
                "ExactMatch": ExactMatch,
                "Index": Index,
                "Distance": Distance,
                "LengthDifference": LengthDifference,
                "Match": Match,
                "IDs": IDs,
                "Images": Images,
                "UserRating": UserRating,
                "AirsOn": AirsOn,
                "Links": Links,
                "Sizes": Sizes,
                "Created": Created,
                "Updated": Updated,
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
    def __getitem__(self, name: typing_extensions.Literal["ExactMatch"]) -> MetaOapg.properties.ExactMatch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Index"]) -> MetaOapg.properties.Index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Distance"]) -> MetaOapg.properties.Distance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LengthDifference"]) -> MetaOapg.properties.LengthDifference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Match"]) -> MetaOapg.properties.Match: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IDs"]) -> 'ShokoSeriesIDs': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Images"]) -> 'CommonImages': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UserRating"]) -> 'CommonRating': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AirsOn"]) -> MetaOapg.properties.AirsOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Links"]) -> MetaOapg.properties.Links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Sizes"]) -> 'ShokoSeriesSizes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Created"]) -> MetaOapg.properties.Created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Updated"]) -> MetaOapg.properties.Updated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AniDB"]) -> 'SeriesAniDBWithDate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TvDB"]) -> MetaOapg.properties.TvDB: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Size"], typing_extensions.Literal["Name"], typing_extensions.Literal["ExactMatch"], typing_extensions.Literal["Index"], typing_extensions.Literal["Distance"], typing_extensions.Literal["LengthDifference"], typing_extensions.Literal["Match"], typing_extensions.Literal["IDs"], typing_extensions.Literal["Images"], typing_extensions.Literal["UserRating"], typing_extensions.Literal["AirsOn"], typing_extensions.Literal["Links"], typing_extensions.Literal["Sizes"], typing_extensions.Literal["Created"], typing_extensions.Literal["Updated"], typing_extensions.Literal["AniDB"], typing_extensions.Literal["TvDB"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Size"]) -> MetaOapg.properties.Size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExactMatch"]) -> typing.Union[MetaOapg.properties.ExactMatch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Index"]) -> typing.Union[MetaOapg.properties.Index, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Distance"]) -> typing.Union[MetaOapg.properties.Distance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LengthDifference"]) -> typing.Union[MetaOapg.properties.LengthDifference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Match"]) -> typing.Union[MetaOapg.properties.Match, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IDs"]) -> typing.Union['ShokoSeriesIDs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Images"]) -> typing.Union['CommonImages', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UserRating"]) -> typing.Union['CommonRating', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AirsOn"]) -> typing.Union[MetaOapg.properties.AirsOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Links"]) -> typing.Union[MetaOapg.properties.Links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Sizes"]) -> typing.Union['ShokoSeriesSizes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Created"]) -> typing.Union[MetaOapg.properties.Created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Updated"]) -> typing.Union[MetaOapg.properties.Updated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AniDB"]) -> typing.Union['SeriesAniDBWithDate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TvDB"]) -> typing.Union[MetaOapg.properties.TvDB, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Size"], typing_extensions.Literal["Name"], typing_extensions.Literal["ExactMatch"], typing_extensions.Literal["Index"], typing_extensions.Literal["Distance"], typing_extensions.Literal["LengthDifference"], typing_extensions.Literal["Match"], typing_extensions.Literal["IDs"], typing_extensions.Literal["Images"], typing_extensions.Literal["UserRating"], typing_extensions.Literal["AirsOn"], typing_extensions.Literal["Links"], typing_extensions.Literal["Sizes"], typing_extensions.Literal["Created"], typing_extensions.Literal["Updated"], typing_extensions.Literal["AniDB"], typing_extensions.Literal["TvDB"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Size: typing.Union[MetaOapg.properties.Size, decimal.Decimal, int, ],
        Name: typing.Union[MetaOapg.properties.Name, str, ],
        ExactMatch: typing.Union[MetaOapg.properties.ExactMatch, bool, schemas.Unset] = schemas.unset,
        Index: typing.Union[MetaOapg.properties.Index, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Distance: typing.Union[MetaOapg.properties.Distance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        LengthDifference: typing.Union[MetaOapg.properties.LengthDifference, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Match: typing.Union[MetaOapg.properties.Match, None, str, schemas.Unset] = schemas.unset,
        IDs: typing.Union['ShokoSeriesIDs', schemas.Unset] = schemas.unset,
        Images: typing.Union['CommonImages', schemas.Unset] = schemas.unset,
        UserRating: typing.Union['CommonRating', schemas.Unset] = schemas.unset,
        AirsOn: typing.Union[MetaOapg.properties.AirsOn, list, tuple, None, schemas.Unset] = schemas.unset,
        Links: typing.Union[MetaOapg.properties.Links, list, tuple, None, schemas.Unset] = schemas.unset,
        Sizes: typing.Union['ShokoSeriesSizes', schemas.Unset] = schemas.unset,
        Created: typing.Union[MetaOapg.properties.Created, str, datetime, schemas.Unset] = schemas.unset,
        Updated: typing.Union[MetaOapg.properties.Updated, str, datetime, schemas.Unset] = schemas.unset,
        AniDB: typing.Union['SeriesAniDBWithDate', schemas.Unset] = schemas.unset,
        TvDB: typing.Union[MetaOapg.properties.TvDB, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ShokoSeriesSearchResult':
        return super().__new__(
            cls,
            *_args,
            Size=Size,
            Name=Name,
            ExactMatch=ExactMatch,
            Index=Index,
            Distance=Distance,
            LengthDifference=LengthDifference,
            Match=Match,
            IDs=IDs,
            Images=Images,
            UserRating=UserRating,
            AirsOn=AirsOn,
            Links=Links,
            Sizes=Sizes,
            Created=Created,
            Updated=Updated,
            AniDB=AniDB,
            TvDB=TvDB,
            _configuration=_configuration,
        )

from lib.shoko.v3.lib.shoko.v3.models.common_images import CommonImages
from lib.shoko.v3.lib.shoko.v3.models.common_rating import CommonRating
from lib.shoko.v3.lib.shoko.v3.models.series_ani_db_with_date import SeriesAniDBWithDate
from lib.shoko.v3.lib.shoko.v3.models.series_resource import SeriesResource
from lib.shoko.v3.lib.shoko.v3.models.series_tv_db import SeriesTvDB
from lib.shoko.v3.lib.shoko.v3.models.shoko_series_ids import ShokoSeriesIDs
from lib.shoko.v3.lib.shoko.v3.models.shoko_series_sizes import ShokoSeriesSizes
from lib.shoko.v3.lib.shoko.v3.models.system_day_of_week import SystemDayOfWeek
