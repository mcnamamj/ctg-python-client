from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_sizes import ListSizes
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/stats/field/sizes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[List["ListSizes"], str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_list_sizes_list_item_data in _response_200:
            componentsschemas_list_sizes_list_item = ListSizes.from_dict(componentsschemas_list_sizes_list_item_data)

            response_200.append(componentsschemas_list_sizes_list_item)

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
) -> Response[Union[List["ListSizes"], str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, List[str]] = UNSET,
) -> Response[Union[List["ListSizes"], str]]:
    r"""List Field Sizes

     Sizes of list/array fields.

    To search studies by a list field size, use `AREA[FieldName:size]` search operator.
    For example, [AREA\[Phase:size\] 2](https://clinicaltrials.gov/search?term=AREA%5BPhase:size%5D%202)
    query finds studies with 2 phases.

    Args:
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['ListSizes'], str]]
    """

    kwargs = _get_kwargs(
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[List["ListSizes"], str]]:
    r"""List Field Sizes

     Sizes of list/array fields.

    To search studies by a list field size, use `AREA[FieldName:size]` search operator.
    For example, [AREA\[Phase:size\] 2](https://clinicaltrials.gov/search?term=AREA%5BPhase:size%5D%202)
    query finds studies with 2 phases.

    Args:
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['ListSizes'], str]
    """

    return sync_detailed(
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, List[str]] = UNSET,
) -> Response[Union[List["ListSizes"], str]]:
    r"""List Field Sizes

     Sizes of list/array fields.

    To search studies by a list field size, use `AREA[FieldName:size]` search operator.
    For example, [AREA\[Phase:size\] 2](https://clinicaltrials.gov/search?term=AREA%5BPhase:size%5D%202)
    query finds studies with 2 phases.

    Args:
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['ListSizes'], str]]
    """

    kwargs = _get_kwargs(
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[List["ListSizes"], str]]:
    r"""List Field Sizes

     Sizes of list/array fields.

    To search studies by a list field size, use `AREA[FieldName:size]` search operator.
    For example, [AREA\[Phase:size\] 2](https://clinicaltrials.gov/search?term=AREA%5BPhase:size%5D%202)
    query finds studies with 2 phases.

    Args:
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['ListSizes'], str]
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
        )
    ).parsed
