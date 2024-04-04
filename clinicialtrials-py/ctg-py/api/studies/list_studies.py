from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_studies_format import ListStudiesFormat
from ...models.list_studies_markup_format import ListStudiesMarkupFormat
from ...models.paged_studies import PagedStudies
from ...models.status import Status
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_: Union[Unset, ListStudiesFormat] = ListStudiesFormat.JSON,
    markup_format: Union[Unset, ListStudiesMarkupFormat] = ListStudiesMarkupFormat.MARKDOWN,
    query_cond: Union[Unset, str] = UNSET,
    query_term: Union[Unset, str] = UNSET,
    query_locn: Union[Unset, str] = UNSET,
    query_titles: Union[Unset, str] = UNSET,
    query_intr: Union[Unset, str] = UNSET,
    query_outc: Union[Unset, str] = UNSET,
    query_spons: Union[Unset, str] = UNSET,
    query_lead: Union[Unset, str] = UNSET,
    query_id: Union[Unset, str] = UNSET,
    query_patient: Union[Unset, str] = UNSET,
    filter_overall_status: Union[Unset, List[Status]] = UNSET,
    filter_geo: Union[Unset, str] = UNSET,
    filter_ids: Union[Unset, List[str]] = UNSET,
    filter_advanced: Union[Unset, str] = UNSET,
    filter_synonyms: Union[Unset, List[str]] = UNSET,
    post_filter_overall_status: Union[Unset, List[Status]] = UNSET,
    post_filter_geo: Union[Unset, str] = UNSET,
    post_filter_ids: Union[Unset, List[str]] = UNSET,
    post_filter_advanced: Union[Unset, str] = UNSET,
    post_filter_synonyms: Union[Unset, List[str]] = UNSET,
    agg_filters: Union[Unset, str] = UNSET,
    geo_decay: Union[Unset, str] = "func:exp,scale:300mi,offset:0mi,decay:0.5",
    fields: Union[Unset, List[str]] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    count_total: Union[Unset, bool] = False,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    json_markup_format: Union[Unset, str] = UNSET
    if not isinstance(markup_format, Unset):
        json_markup_format = markup_format.value

    params["markupFormat"] = json_markup_format

    params["query.cond"] = query_cond

    params["query.term"] = query_term

    params["query.locn"] = query_locn

    params["query.titles"] = query_titles

    params["query.intr"] = query_intr

    params["query.outc"] = query_outc

    params["query.spons"] = query_spons

    params["query.lead"] = query_lead

    params["query.id"] = query_id

    params["query.patient"] = query_patient

    json_filter_overall_status: Union[Unset, List[str]] = UNSET
    if not isinstance(filter_overall_status, Unset):
        json_filter_overall_status = []
        for filter_overall_status_item_data in filter_overall_status:
            filter_overall_status_item = filter_overall_status_item_data.value
            json_filter_overall_status.append(filter_overall_status_item)

    params["filter.overallStatus"] = json_filter_overall_status

    params["filter.geo"] = filter_geo

    json_filter_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(filter_ids, Unset):
        json_filter_ids = filter_ids

    params["filter.ids"] = json_filter_ids

    params["filter.advanced"] = filter_advanced

    json_filter_synonyms: Union[Unset, List[str]] = UNSET
    if not isinstance(filter_synonyms, Unset):
        json_filter_synonyms = filter_synonyms

    params["filter.synonyms"] = json_filter_synonyms

    json_post_filter_overall_status: Union[Unset, List[str]] = UNSET
    if not isinstance(post_filter_overall_status, Unset):
        json_post_filter_overall_status = []
        for post_filter_overall_status_item_data in post_filter_overall_status:
            post_filter_overall_status_item = post_filter_overall_status_item_data.value
            json_post_filter_overall_status.append(post_filter_overall_status_item)

    params["postFilter.overallStatus"] = json_post_filter_overall_status

    params["postFilter.geo"] = post_filter_geo

    json_post_filter_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(post_filter_ids, Unset):
        json_post_filter_ids = post_filter_ids

    params["postFilter.ids"] = json_post_filter_ids

    params["postFilter.advanced"] = post_filter_advanced

    json_post_filter_synonyms: Union[Unset, List[str]] = UNSET
    if not isinstance(post_filter_synonyms, Unset):
        json_post_filter_synonyms = post_filter_synonyms

    params["postFilter.synonyms"] = json_post_filter_synonyms

    params["aggFilters"] = agg_filters

    params["geoDecay"] = geo_decay

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    json_sort: Union[Unset, List[str]] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["countTotal"] = count_total

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/studies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PagedStudies, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PagedStudies.from_dict(response.json())

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
) -> Response[Union[PagedStudies, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, ListStudiesFormat] = ListStudiesFormat.JSON,
    markup_format: Union[Unset, ListStudiesMarkupFormat] = ListStudiesMarkupFormat.MARKDOWN,
    query_cond: Union[Unset, str] = UNSET,
    query_term: Union[Unset, str] = UNSET,
    query_locn: Union[Unset, str] = UNSET,
    query_titles: Union[Unset, str] = UNSET,
    query_intr: Union[Unset, str] = UNSET,
    query_outc: Union[Unset, str] = UNSET,
    query_spons: Union[Unset, str] = UNSET,
    query_lead: Union[Unset, str] = UNSET,
    query_id: Union[Unset, str] = UNSET,
    query_patient: Union[Unset, str] = UNSET,
    filter_overall_status: Union[Unset, List[Status]] = UNSET,
    filter_geo: Union[Unset, str] = UNSET,
    filter_ids: Union[Unset, List[str]] = UNSET,
    filter_advanced: Union[Unset, str] = UNSET,
    filter_synonyms: Union[Unset, List[str]] = UNSET,
    post_filter_overall_status: Union[Unset, List[Status]] = UNSET,
    post_filter_geo: Union[Unset, str] = UNSET,
    post_filter_ids: Union[Unset, List[str]] = UNSET,
    post_filter_advanced: Union[Unset, str] = UNSET,
    post_filter_synonyms: Union[Unset, List[str]] = UNSET,
    agg_filters: Union[Unset, str] = UNSET,
    geo_decay: Union[Unset, str] = "func:exp,scale:300mi,offset:0mi,decay:0.5",
    fields: Union[Unset, List[str]] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    count_total: Union[Unset, bool] = False,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Response[Union[PagedStudies, str]]:
    """Studies

     Returns data of studies matching query and filter parameters. The studies are returned page by page.
    If response contains `nextPageToken`, use its value in `pageToken` to get next page.
    The last page will not contain `nextPageToken`. A page may have empty `studies` array.
    Request for each subsequent page **must** have the same parameters as for the first page, except
    `countTotal`, `pageSize`, and `pageToken` parameters.

    If neither queries nor filters are set, all studies will be returned.
    If any query parameter contains only NCT IDs (comma- and/or space-separated), filters are ignored.

    `query.*` parameters are in [Essie expression
    syntax](https://classic.clinicaltrials.gov/api/gui/ref/syntax).
    Those parameters affect ranking of studies, if sorted by relevance. See `sort` parameter for
    details.

    `filter.*` and `postFilter.*` parameters have same effect as there is no aggregation calculation.
    Both are available just to simplify applying parameters from search request.
    Both do not affect ranking of studies.

    Note: When trying JSON format in your browser, do not set too large `pageSize` parameter, if
    `fields` is
    unlimited. That may return too much data for the browser to parse and render.

    Args:
        format_ (Union[Unset, ListStudiesFormat]):  Default: ListStudiesFormat.JSON.
        markup_format (Union[Unset, ListStudiesMarkupFormat]):  Default:
            ListStudiesMarkupFormat.MARKDOWN.
        query_cond (Union[Unset, str]):
        query_term (Union[Unset, str]):
        query_locn (Union[Unset, str]):
        query_titles (Union[Unset, str]):
        query_intr (Union[Unset, str]):
        query_outc (Union[Unset, str]):
        query_spons (Union[Unset, str]):
        query_lead (Union[Unset, str]):
        query_id (Union[Unset, str]):
        query_patient (Union[Unset, str]):
        filter_overall_status (Union[Unset, List[Status]]):
        filter_geo (Union[Unset, str]):
        filter_ids (Union[Unset, List[str]]):
        filter_advanced (Union[Unset, str]):
        filter_synonyms (Union[Unset, List[str]]):
        post_filter_overall_status (Union[Unset, List[Status]]):
        post_filter_geo (Union[Unset, str]):
        post_filter_ids (Union[Unset, List[str]]):
        post_filter_advanced (Union[Unset, str]):
        post_filter_synonyms (Union[Unset, List[str]]):
        agg_filters (Union[Unset, str]):
        geo_decay (Union[Unset, str]):  Default: 'func:exp,scale:300mi,offset:0mi,decay:0.5'.
        fields (Union[Unset, List[str]]):
        sort (Union[Unset, List[str]]):
        count_total (Union[Unset, bool]):  Default: False.
        page_size (Union[Unset, int]):  Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PagedStudies, str]]
    """

    kwargs = _get_kwargs(
        format_=format_,
        markup_format=markup_format,
        query_cond=query_cond,
        query_term=query_term,
        query_locn=query_locn,
        query_titles=query_titles,
        query_intr=query_intr,
        query_outc=query_outc,
        query_spons=query_spons,
        query_lead=query_lead,
        query_id=query_id,
        query_patient=query_patient,
        filter_overall_status=filter_overall_status,
        filter_geo=filter_geo,
        filter_ids=filter_ids,
        filter_advanced=filter_advanced,
        filter_synonyms=filter_synonyms,
        post_filter_overall_status=post_filter_overall_status,
        post_filter_geo=post_filter_geo,
        post_filter_ids=post_filter_ids,
        post_filter_advanced=post_filter_advanced,
        post_filter_synonyms=post_filter_synonyms,
        agg_filters=agg_filters,
        geo_decay=geo_decay,
        fields=fields,
        sort=sort,
        count_total=count_total,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, ListStudiesFormat] = ListStudiesFormat.JSON,
    markup_format: Union[Unset, ListStudiesMarkupFormat] = ListStudiesMarkupFormat.MARKDOWN,
    query_cond: Union[Unset, str] = UNSET,
    query_term: Union[Unset, str] = UNSET,
    query_locn: Union[Unset, str] = UNSET,
    query_titles: Union[Unset, str] = UNSET,
    query_intr: Union[Unset, str] = UNSET,
    query_outc: Union[Unset, str] = UNSET,
    query_spons: Union[Unset, str] = UNSET,
    query_lead: Union[Unset, str] = UNSET,
    query_id: Union[Unset, str] = UNSET,
    query_patient: Union[Unset, str] = UNSET,
    filter_overall_status: Union[Unset, List[Status]] = UNSET,
    filter_geo: Union[Unset, str] = UNSET,
    filter_ids: Union[Unset, List[str]] = UNSET,
    filter_advanced: Union[Unset, str] = UNSET,
    filter_synonyms: Union[Unset, List[str]] = UNSET,
    post_filter_overall_status: Union[Unset, List[Status]] = UNSET,
    post_filter_geo: Union[Unset, str] = UNSET,
    post_filter_ids: Union[Unset, List[str]] = UNSET,
    post_filter_advanced: Union[Unset, str] = UNSET,
    post_filter_synonyms: Union[Unset, List[str]] = UNSET,
    agg_filters: Union[Unset, str] = UNSET,
    geo_decay: Union[Unset, str] = "func:exp,scale:300mi,offset:0mi,decay:0.5",
    fields: Union[Unset, List[str]] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    count_total: Union[Unset, bool] = False,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[Union[PagedStudies, str]]:
    """Studies

     Returns data of studies matching query and filter parameters. The studies are returned page by page.
    If response contains `nextPageToken`, use its value in `pageToken` to get next page.
    The last page will not contain `nextPageToken`. A page may have empty `studies` array.
    Request for each subsequent page **must** have the same parameters as for the first page, except
    `countTotal`, `pageSize`, and `pageToken` parameters.

    If neither queries nor filters are set, all studies will be returned.
    If any query parameter contains only NCT IDs (comma- and/or space-separated), filters are ignored.

    `query.*` parameters are in [Essie expression
    syntax](https://classic.clinicaltrials.gov/api/gui/ref/syntax).
    Those parameters affect ranking of studies, if sorted by relevance. See `sort` parameter for
    details.

    `filter.*` and `postFilter.*` parameters have same effect as there is no aggregation calculation.
    Both are available just to simplify applying parameters from search request.
    Both do not affect ranking of studies.

    Note: When trying JSON format in your browser, do not set too large `pageSize` parameter, if
    `fields` is
    unlimited. That may return too much data for the browser to parse and render.

    Args:
        format_ (Union[Unset, ListStudiesFormat]):  Default: ListStudiesFormat.JSON.
        markup_format (Union[Unset, ListStudiesMarkupFormat]):  Default:
            ListStudiesMarkupFormat.MARKDOWN.
        query_cond (Union[Unset, str]):
        query_term (Union[Unset, str]):
        query_locn (Union[Unset, str]):
        query_titles (Union[Unset, str]):
        query_intr (Union[Unset, str]):
        query_outc (Union[Unset, str]):
        query_spons (Union[Unset, str]):
        query_lead (Union[Unset, str]):
        query_id (Union[Unset, str]):
        query_patient (Union[Unset, str]):
        filter_overall_status (Union[Unset, List[Status]]):
        filter_geo (Union[Unset, str]):
        filter_ids (Union[Unset, List[str]]):
        filter_advanced (Union[Unset, str]):
        filter_synonyms (Union[Unset, List[str]]):
        post_filter_overall_status (Union[Unset, List[Status]]):
        post_filter_geo (Union[Unset, str]):
        post_filter_ids (Union[Unset, List[str]]):
        post_filter_advanced (Union[Unset, str]):
        post_filter_synonyms (Union[Unset, List[str]]):
        agg_filters (Union[Unset, str]):
        geo_decay (Union[Unset, str]):  Default: 'func:exp,scale:300mi,offset:0mi,decay:0.5'.
        fields (Union[Unset, List[str]]):
        sort (Union[Unset, List[str]]):
        count_total (Union[Unset, bool]):  Default: False.
        page_size (Union[Unset, int]):  Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PagedStudies, str]
    """

    return sync_detailed(
        client=client,
        format_=format_,
        markup_format=markup_format,
        query_cond=query_cond,
        query_term=query_term,
        query_locn=query_locn,
        query_titles=query_titles,
        query_intr=query_intr,
        query_outc=query_outc,
        query_spons=query_spons,
        query_lead=query_lead,
        query_id=query_id,
        query_patient=query_patient,
        filter_overall_status=filter_overall_status,
        filter_geo=filter_geo,
        filter_ids=filter_ids,
        filter_advanced=filter_advanced,
        filter_synonyms=filter_synonyms,
        post_filter_overall_status=post_filter_overall_status,
        post_filter_geo=post_filter_geo,
        post_filter_ids=post_filter_ids,
        post_filter_advanced=post_filter_advanced,
        post_filter_synonyms=post_filter_synonyms,
        agg_filters=agg_filters,
        geo_decay=geo_decay,
        fields=fields,
        sort=sort,
        count_total=count_total,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, ListStudiesFormat] = ListStudiesFormat.JSON,
    markup_format: Union[Unset, ListStudiesMarkupFormat] = ListStudiesMarkupFormat.MARKDOWN,
    query_cond: Union[Unset, str] = UNSET,
    query_term: Union[Unset, str] = UNSET,
    query_locn: Union[Unset, str] = UNSET,
    query_titles: Union[Unset, str] = UNSET,
    query_intr: Union[Unset, str] = UNSET,
    query_outc: Union[Unset, str] = UNSET,
    query_spons: Union[Unset, str] = UNSET,
    query_lead: Union[Unset, str] = UNSET,
    query_id: Union[Unset, str] = UNSET,
    query_patient: Union[Unset, str] = UNSET,
    filter_overall_status: Union[Unset, List[Status]] = UNSET,
    filter_geo: Union[Unset, str] = UNSET,
    filter_ids: Union[Unset, List[str]] = UNSET,
    filter_advanced: Union[Unset, str] = UNSET,
    filter_synonyms: Union[Unset, List[str]] = UNSET,
    post_filter_overall_status: Union[Unset, List[Status]] = UNSET,
    post_filter_geo: Union[Unset, str] = UNSET,
    post_filter_ids: Union[Unset, List[str]] = UNSET,
    post_filter_advanced: Union[Unset, str] = UNSET,
    post_filter_synonyms: Union[Unset, List[str]] = UNSET,
    agg_filters: Union[Unset, str] = UNSET,
    geo_decay: Union[Unset, str] = "func:exp,scale:300mi,offset:0mi,decay:0.5",
    fields: Union[Unset, List[str]] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    count_total: Union[Unset, bool] = False,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Response[Union[PagedStudies, str]]:
    """Studies

     Returns data of studies matching query and filter parameters. The studies are returned page by page.
    If response contains `nextPageToken`, use its value in `pageToken` to get next page.
    The last page will not contain `nextPageToken`. A page may have empty `studies` array.
    Request for each subsequent page **must** have the same parameters as for the first page, except
    `countTotal`, `pageSize`, and `pageToken` parameters.

    If neither queries nor filters are set, all studies will be returned.
    If any query parameter contains only NCT IDs (comma- and/or space-separated), filters are ignored.

    `query.*` parameters are in [Essie expression
    syntax](https://classic.clinicaltrials.gov/api/gui/ref/syntax).
    Those parameters affect ranking of studies, if sorted by relevance. See `sort` parameter for
    details.

    `filter.*` and `postFilter.*` parameters have same effect as there is no aggregation calculation.
    Both are available just to simplify applying parameters from search request.
    Both do not affect ranking of studies.

    Note: When trying JSON format in your browser, do not set too large `pageSize` parameter, if
    `fields` is
    unlimited. That may return too much data for the browser to parse and render.

    Args:
        format_ (Union[Unset, ListStudiesFormat]):  Default: ListStudiesFormat.JSON.
        markup_format (Union[Unset, ListStudiesMarkupFormat]):  Default:
            ListStudiesMarkupFormat.MARKDOWN.
        query_cond (Union[Unset, str]):
        query_term (Union[Unset, str]):
        query_locn (Union[Unset, str]):
        query_titles (Union[Unset, str]):
        query_intr (Union[Unset, str]):
        query_outc (Union[Unset, str]):
        query_spons (Union[Unset, str]):
        query_lead (Union[Unset, str]):
        query_id (Union[Unset, str]):
        query_patient (Union[Unset, str]):
        filter_overall_status (Union[Unset, List[Status]]):
        filter_geo (Union[Unset, str]):
        filter_ids (Union[Unset, List[str]]):
        filter_advanced (Union[Unset, str]):
        filter_synonyms (Union[Unset, List[str]]):
        post_filter_overall_status (Union[Unset, List[Status]]):
        post_filter_geo (Union[Unset, str]):
        post_filter_ids (Union[Unset, List[str]]):
        post_filter_advanced (Union[Unset, str]):
        post_filter_synonyms (Union[Unset, List[str]]):
        agg_filters (Union[Unset, str]):
        geo_decay (Union[Unset, str]):  Default: 'func:exp,scale:300mi,offset:0mi,decay:0.5'.
        fields (Union[Unset, List[str]]):
        sort (Union[Unset, List[str]]):
        count_total (Union[Unset, bool]):  Default: False.
        page_size (Union[Unset, int]):  Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PagedStudies, str]]
    """

    kwargs = _get_kwargs(
        format_=format_,
        markup_format=markup_format,
        query_cond=query_cond,
        query_term=query_term,
        query_locn=query_locn,
        query_titles=query_titles,
        query_intr=query_intr,
        query_outc=query_outc,
        query_spons=query_spons,
        query_lead=query_lead,
        query_id=query_id,
        query_patient=query_patient,
        filter_overall_status=filter_overall_status,
        filter_geo=filter_geo,
        filter_ids=filter_ids,
        filter_advanced=filter_advanced,
        filter_synonyms=filter_synonyms,
        post_filter_overall_status=post_filter_overall_status,
        post_filter_geo=post_filter_geo,
        post_filter_ids=post_filter_ids,
        post_filter_advanced=post_filter_advanced,
        post_filter_synonyms=post_filter_synonyms,
        agg_filters=agg_filters,
        geo_decay=geo_decay,
        fields=fields,
        sort=sort,
        count_total=count_total,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, ListStudiesFormat] = ListStudiesFormat.JSON,
    markup_format: Union[Unset, ListStudiesMarkupFormat] = ListStudiesMarkupFormat.MARKDOWN,
    query_cond: Union[Unset, str] = UNSET,
    query_term: Union[Unset, str] = UNSET,
    query_locn: Union[Unset, str] = UNSET,
    query_titles: Union[Unset, str] = UNSET,
    query_intr: Union[Unset, str] = UNSET,
    query_outc: Union[Unset, str] = UNSET,
    query_spons: Union[Unset, str] = UNSET,
    query_lead: Union[Unset, str] = UNSET,
    query_id: Union[Unset, str] = UNSET,
    query_patient: Union[Unset, str] = UNSET,
    filter_overall_status: Union[Unset, List[Status]] = UNSET,
    filter_geo: Union[Unset, str] = UNSET,
    filter_ids: Union[Unset, List[str]] = UNSET,
    filter_advanced: Union[Unset, str] = UNSET,
    filter_synonyms: Union[Unset, List[str]] = UNSET,
    post_filter_overall_status: Union[Unset, List[Status]] = UNSET,
    post_filter_geo: Union[Unset, str] = UNSET,
    post_filter_ids: Union[Unset, List[str]] = UNSET,
    post_filter_advanced: Union[Unset, str] = UNSET,
    post_filter_synonyms: Union[Unset, List[str]] = UNSET,
    agg_filters: Union[Unset, str] = UNSET,
    geo_decay: Union[Unset, str] = "func:exp,scale:300mi,offset:0mi,decay:0.5",
    fields: Union[Unset, List[str]] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    count_total: Union[Unset, bool] = False,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[Union[PagedStudies, str]]:
    """Studies

     Returns data of studies matching query and filter parameters. The studies are returned page by page.
    If response contains `nextPageToken`, use its value in `pageToken` to get next page.
    The last page will not contain `nextPageToken`. A page may have empty `studies` array.
    Request for each subsequent page **must** have the same parameters as for the first page, except
    `countTotal`, `pageSize`, and `pageToken` parameters.

    If neither queries nor filters are set, all studies will be returned.
    If any query parameter contains only NCT IDs (comma- and/or space-separated), filters are ignored.

    `query.*` parameters are in [Essie expression
    syntax](https://classic.clinicaltrials.gov/api/gui/ref/syntax).
    Those parameters affect ranking of studies, if sorted by relevance. See `sort` parameter for
    details.

    `filter.*` and `postFilter.*` parameters have same effect as there is no aggregation calculation.
    Both are available just to simplify applying parameters from search request.
    Both do not affect ranking of studies.

    Note: When trying JSON format in your browser, do not set too large `pageSize` parameter, if
    `fields` is
    unlimited. That may return too much data for the browser to parse and render.

    Args:
        format_ (Union[Unset, ListStudiesFormat]):  Default: ListStudiesFormat.JSON.
        markup_format (Union[Unset, ListStudiesMarkupFormat]):  Default:
            ListStudiesMarkupFormat.MARKDOWN.
        query_cond (Union[Unset, str]):
        query_term (Union[Unset, str]):
        query_locn (Union[Unset, str]):
        query_titles (Union[Unset, str]):
        query_intr (Union[Unset, str]):
        query_outc (Union[Unset, str]):
        query_spons (Union[Unset, str]):
        query_lead (Union[Unset, str]):
        query_id (Union[Unset, str]):
        query_patient (Union[Unset, str]):
        filter_overall_status (Union[Unset, List[Status]]):
        filter_geo (Union[Unset, str]):
        filter_ids (Union[Unset, List[str]]):
        filter_advanced (Union[Unset, str]):
        filter_synonyms (Union[Unset, List[str]]):
        post_filter_overall_status (Union[Unset, List[Status]]):
        post_filter_geo (Union[Unset, str]):
        post_filter_ids (Union[Unset, List[str]]):
        post_filter_advanced (Union[Unset, str]):
        post_filter_synonyms (Union[Unset, List[str]]):
        agg_filters (Union[Unset, str]):
        geo_decay (Union[Unset, str]):  Default: 'func:exp,scale:300mi,offset:0mi,decay:0.5'.
        fields (Union[Unset, List[str]]):
        sort (Union[Unset, List[str]]):
        count_total (Union[Unset, bool]):  Default: False.
        page_size (Union[Unset, int]):  Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PagedStudies, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
            markup_format=markup_format,
            query_cond=query_cond,
            query_term=query_term,
            query_locn=query_locn,
            query_titles=query_titles,
            query_intr=query_intr,
            query_outc=query_outc,
            query_spons=query_spons,
            query_lead=query_lead,
            query_id=query_id,
            query_patient=query_patient,
            filter_overall_status=filter_overall_status,
            filter_geo=filter_geo,
            filter_ids=filter_ids,
            filter_advanced=filter_advanced,
            filter_synonyms=filter_synonyms,
            post_filter_overall_status=post_filter_overall_status,
            post_filter_geo=post_filter_geo,
            post_filter_ids=post_filter_ids,
            post_filter_advanced=post_filter_advanced,
            post_filter_synonyms=post_filter_synonyms,
            agg_filters=agg_filters,
            geo_decay=geo_decay,
            fields=fields,
            sort=sort,
            count_total=count_total,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
