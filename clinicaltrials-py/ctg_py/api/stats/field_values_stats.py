from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.boolean_stats import BooleanStats
from ...models.date_stats import DateStats
from ...models.enum_stats import EnumStats
from ...models.field_stats_type import FieldStatsType
from ...models.integer_stats import IntegerStats
from ...models.number_stats import NumberStats
from ...models.string_stats import StringStats
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    types: Union[Unset, List[FieldStatsType]] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_types: Union[Unset, List[str]] = UNSET
    if not isinstance(types, Unset):
        json_types = []
        for types_item_data in types:
            types_item = types_item_data.value
            json_types.append(types_item)

    params["types"] = json_types

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/stats/field/values",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[List[Union["BooleanStats", "DateStats", "EnumStats", "IntegerStats", "NumberStats", "StringStats"]], str]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_field_values_stats_list_item_data in _response_200:

            def _parse_componentsschemas_field_values_stats_list_item(
                data: object,
            ) -> Union["BooleanStats", "DateStats", "EnumStats", "IntegerStats", "NumberStats", "StringStats"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_field_values_stats_type_0 = EnumStats.from_dict(data)

                    return componentsschemas_field_values_stats_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_field_values_stats_type_1 = StringStats.from_dict(data)

                    return componentsschemas_field_values_stats_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_field_values_stats_type_2 = DateStats.from_dict(data)

                    return componentsschemas_field_values_stats_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_field_values_stats_type_3 = IntegerStats.from_dict(data)

                    return componentsschemas_field_values_stats_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_field_values_stats_type_4 = NumberStats.from_dict(data)

                    return componentsschemas_field_values_stats_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_field_values_stats_type_5 = BooleanStats.from_dict(data)

                return componentsschemas_field_values_stats_type_5

            componentsschemas_field_values_stats_list_item = _parse_componentsschemas_field_values_stats_list_item(
                componentsschemas_field_values_stats_list_item_data
            )

            response_200.append(componentsschemas_field_values_stats_list_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = response.text
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = response.text
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[List[Union["BooleanStats", "DateStats", "EnumStats", "IntegerStats", "NumberStats", "StringStats"]], str]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[FieldStatsType]] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Response[
    Union[List[Union["BooleanStats", "DateStats", "EnumStats", "IntegerStats", "NumberStats", "StringStats"]], str]
]:
    """Field Values

     Value statistics of the study leaf fields.

    Args:
        types (Union[Unset, List[FieldStatsType]]):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List[Union['BooleanStats', 'DateStats', 'EnumStats', 'IntegerStats', 'NumberStats', 'StringStats']], str]]
    """

    kwargs = _get_kwargs(
        types=types,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[FieldStatsType]] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Optional[
    Union[List[Union["BooleanStats", "DateStats", "EnumStats", "IntegerStats", "NumberStats", "StringStats"]], str]
]:
    """Field Values

     Value statistics of the study leaf fields.

    Args:
        types (Union[Unset, List[FieldStatsType]]):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List[Union['BooleanStats', 'DateStats', 'EnumStats', 'IntegerStats', 'NumberStats', 'StringStats']], str]
    """

    return sync_detailed(
        client=client,
        types=types,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[FieldStatsType]] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Response[
    Union[List[Union["BooleanStats", "DateStats", "EnumStats", "IntegerStats", "NumberStats", "StringStats"]], str]
]:
    """Field Values

     Value statistics of the study leaf fields.

    Args:
        types (Union[Unset, List[FieldStatsType]]):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List[Union['BooleanStats', 'DateStats', 'EnumStats', 'IntegerStats', 'NumberStats', 'StringStats']], str]]
    """

    kwargs = _get_kwargs(
        types=types,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[FieldStatsType]] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Optional[
    Union[List[Union["BooleanStats", "DateStats", "EnumStats", "IntegerStats", "NumberStats", "StringStats"]], str]
]:
    """Field Values

     Value statistics of the study leaf fields.

    Args:
        types (Union[Unset, List[FieldStatsType]]):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List[Union['BooleanStats', 'DateStats', 'EnumStats', 'IntegerStats', 'NumberStats', 'StringStats']], str]
    """

    return (
        await asyncio_detailed(
            client=client,
            types=types,
            fields=fields,
        )
    ).parsed
