from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.version import Version
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/version",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Version, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Version.from_dict(response.json())

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
) -> Response[Union[Version, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Version, str]]:
    """Version

     API and data versions.

    API version follows [Semantic Versioning 2.0.0 Schema](https://semver.org/spec/v2.0.0.html).
    Data version is UTC timestamp in `yyyy-MM-dd'T'HH:mm:ss` format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Version, str]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Version, str]]:
    """Version

     API and data versions.

    API version follows [Semantic Versioning 2.0.0 Schema](https://semver.org/spec/v2.0.0.html).
    Data version is UTC timestamp in `yyyy-MM-dd'T'HH:mm:ss` format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Version, str]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Version, str]]:
    """Version

     API and data versions.

    API version follows [Semantic Versioning 2.0.0 Schema](https://semver.org/spec/v2.0.0.html).
    Data version is UTC timestamp in `yyyy-MM-dd'T'HH:mm:ss` format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Version, str]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Version, str]]:
    """Version

     API and data versions.

    API version follows [Semantic Versioning 2.0.0 Schema](https://semver.org/spec/v2.0.0.html).
    Data version is UTC timestamp in `yyyy-MM-dd'T'HH:mm:ss` format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Version, str]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
