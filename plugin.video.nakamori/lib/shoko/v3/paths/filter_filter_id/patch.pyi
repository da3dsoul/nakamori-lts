# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from lib.shoko.v3 import api_client, exceptions
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

from lib.shoko.v3.lib.shoko.v3.models.operations_operation import OperationsOperation
from lib.shoko.v3.lib.shoko.v3.models.shoko_filter import ShokoFilter

# Path params
FilterIDSchema = schemas.Int32Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'filterID': typing.Union[FilterIDSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_filter_id = api_client.PathParameter(
    name="filterID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FilterIDSchema,
    required=True,
)
# body param


class SchemaForRequestBodyApplicationJsonPatchjson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OperationsOperation']:
            return OperationsOperation

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['OperationsOperation'], typing.List['OperationsOperation']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaForRequestBodyApplicationJsonPatchjson':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OperationsOperation':
        return super().__getitem__(i)


class SchemaForRequestBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OperationsOperation']:
            return OperationsOperation

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['OperationsOperation'], typing.List['OperationsOperation']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OperationsOperation':
        return super().__getitem__(i)


class SchemaForRequestBodyTextJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OperationsOperation']:
            return OperationsOperation

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['OperationsOperation'], typing.List['OperationsOperation']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaForRequestBodyTextJson':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OperationsOperation':
        return super().__getitem__(i)


class SchemaForRequestBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OperationsOperation']:
            return OperationsOperation

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['OperationsOperation'], typing.List['OperationsOperation']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OperationsOperation':
        return super().__getitem__(i)


request_body_operations_operation = api_client.RequestBody(
    content={
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/*+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyTextPlain = ShokoFilter
SchemaFor200ResponseBodyApplicationJson = ShokoFilter
SchemaFor200ResponseBodyTextJson = ShokoFilter


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyTextPlain,
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyTextJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlain),
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
    },
)
_all_accept_content_types = (
    'text/plain',
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _filter_filter_id_patch_oapg(
        self,
        content_type: typing_extensions.Literal["application/json-patch+json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _filter_filter_id_patch_oapg(
        self,
        content_type: typing_extensions.Literal["application/json"],
        body: typing.Union[SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _filter_filter_id_patch_oapg(
        self,
        content_type: typing_extensions.Literal["text/json"],
        body: typing.Union[SchemaForRequestBodyTextJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _filter_filter_id_patch_oapg(
        self,
        content_type: typing_extensions.Literal["application/*+json"],
        body: typing.Union[SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _filter_filter_id_patch_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def _filter_filter_id_patch_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _filter_filter_id_patch_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _filter_filter_id_patch_oapg(
        self,
        content_type: str = 'application/json-patch+json',
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Edit an existing filter using a JSON patch document to do a partial  update. Requires admin.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_filter_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_operations_operation.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='patch'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class FilterFilterIdPatch(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def filter_filter_id_patch(
        self,
        content_type: typing_extensions.Literal["application/json-patch+json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def filter_filter_id_patch(
        self,
        content_type: typing_extensions.Literal["application/json"],
        body: typing.Union[SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def filter_filter_id_patch(
        self,
        content_type: typing_extensions.Literal["text/json"],
        body: typing.Union[SchemaForRequestBodyTextJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def filter_filter_id_patch(
        self,
        content_type: typing_extensions.Literal["application/*+json"],
        body: typing.Union[SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def filter_filter_id_patch(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def filter_filter_id_patch(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def filter_filter_id_patch(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def filter_filter_id_patch(
        self,
        content_type: str = 'application/json-patch+json',
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._filter_filter_id_patch_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def patch(
        self,
        content_type: typing_extensions.Literal["application/json-patch+json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def patch(
        self,
        content_type: typing_extensions.Literal["application/json"],
        body: typing.Union[SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def patch(
        self,
        content_type: typing_extensions.Literal["text/json"],
        body: typing.Union[SchemaForRequestBodyTextJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def patch(
        self,
        content_type: typing_extensions.Literal["application/*+json"],
        body: typing.Union[SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def patch(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def patch(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def patch(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def patch(
        self,
        content_type: str = 'application/json-patch+json',
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, SchemaForRequestBodyTextJson, list, tuple, SchemaForRequestBodyApplicationJson, list, tuple, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._filter_filter_id_patch_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


