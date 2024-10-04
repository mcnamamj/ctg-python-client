from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enum_info import EnumInfo
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/studies/enums",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[List["EnumInfo"], str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_enum_info_list_item_data in _response_200:
            componentsschemas_enum_info_list_item = EnumInfo.from_dict(componentsschemas_enum_info_list_item_data)

            response_200.append(componentsschemas_enum_info_list_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = response.text
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[List["EnumInfo"], str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[List["EnumInfo"], str]]:
    """Enums

     Returns enumeration types and their values.

    Every item of the returning array represents enum type and contains the following properties:
    * `type` - enum type name
    * `pieces` - array of names of all data pieces having the enum type
    * `values` - all available values of the enum; every item contains the following properties:
      * `value` - data value
      * `legacyValue` - data value in legacy API
      * `exceptions` - map from data piece name to legacy value when different from `legacyValue`
        (some data pieces had special enum values in legacy API)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['EnumInfo'], str]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[List["EnumInfo"], str]]:
    """Enums

     Returns enumeration types and their values.

    Every item of the returning array represents enum type and contains the following properties:
    * `type` - enum type name
    * `pieces` - array of names of all data pieces having the enum type
    * `values` - all available values of the enum; every item contains the following properties:
      * `value` - data value
      * `legacyValue` - data value in legacy API
      * `exceptions` - map from data piece name to legacy value when different from `legacyValue`
        (some data pieces had special enum values in legacy API)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['EnumInfo'], str]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[List["EnumInfo"], str]]:
    """Enums

     Returns enumeration types and their values.

    Every item of the returning array represents enum type and contains the following properties:
    * `type` - enum type name
    * `pieces` - array of names of all data pieces having the enum type
    * `values` - all available values of the enum; every item contains the following properties:
      * `value` - data value
      * `legacyValue` - data value in legacy API
      * `exceptions` - map from data piece name to legacy value when different from `legacyValue`
        (some data pieces had special enum values in legacy API)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['EnumInfo'], str]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[List["EnumInfo"], str]]:
    """Enums

     Returns enumeration types and their values.

    Every item of the returning array represents enum type and contains the following properties:
    * `type` - enum type name
    * `pieces` - array of names of all data pieces having the enum type
    * `values` - all available values of the enum; every item contains the following properties:
      * `value` - data value
      * `legacyValue` - data value in legacy API
      * `exceptions` - map from data piece name to legacy value when different from `legacyValue`
        (some data pieces had special enum values in legacy API)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['EnumInfo'], str]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
