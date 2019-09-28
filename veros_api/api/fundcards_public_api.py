# coding: utf-8

"""
    Veros API

    Routes of Veros project  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from veros_api.api_client import ApiClient
from veros_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class FundcardsPublicApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fundcards_public_go(self, id, data, **kwargs):  # noqa: E501
        """fundcards_public_go  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fundcards_public_go(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param CardGo data: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CardGo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.fundcards_public_go_with_http_info(id, data, **kwargs)  # noqa: E501

    def fundcards_public_go_with_http_info(self, id, data, **kwargs):  # noqa: E501
        """fundcards_public_go  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fundcards_public_go_with_http_info(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param CardGo data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CardGo, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fundcards_public_go" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `fundcards_public_go`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in local_var_params or
                local_var_params['data'] is None):
            raise ApiValueError("Missing the required parameter `data` when calling `fundcards_public_go`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/fundcards-public/{id}/go/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CardGo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fundcards_public_list(self, **kwargs):  # noqa: E501
        """fundcards_public_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fundcards_public_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str directions: Multiple values may be separated by commas.
        :param str fundraising_type: Multiple values may be separated by commas.
        :param str payment_types: Multiple values may be separated by commas.
        :param str ids: Multiple values may be separated by commas.
        :param str search: A search term.
        :param str ordering: Which field to use when ordering the results.
        :param str country_id: Country ID
        :param str country_name: Country name
        :param str city_id: City ID
        :param str city_name: City name
        :param str organizer_type: Organizer Type
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.fundcards_public_list_with_http_info(**kwargs)  # noqa: E501

    def fundcards_public_list_with_http_info(self, **kwargs):  # noqa: E501
        """fundcards_public_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fundcards_public_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str directions: Multiple values may be separated by commas.
        :param str fundraising_type: Multiple values may be separated by commas.
        :param str payment_types: Multiple values may be separated by commas.
        :param str ids: Multiple values may be separated by commas.
        :param str search: A search term.
        :param str ordering: Which field to use when ordering the results.
        :param str country_id: Country ID
        :param str country_name: Country name
        :param str city_id: City ID
        :param str city_name: City name
        :param str organizer_type: Organizer Type
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2003, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['directions', 'fundraising_type', 'payment_types', 'ids', 'search', 'ordering', 'country_id', 'country_name', 'city_id', 'city_name', 'organizer_type', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fundcards_public_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'directions' in local_var_params:
            query_params.append(('directions', local_var_params['directions']))  # noqa: E501
        if 'fundraising_type' in local_var_params:
            query_params.append(('fundraising_type', local_var_params['fundraising_type']))  # noqa: E501
        if 'payment_types' in local_var_params:
            query_params.append(('payment_types', local_var_params['payment_types']))  # noqa: E501
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))  # noqa: E501
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))  # noqa: E501
        if 'ordering' in local_var_params:
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
        if 'country_id' in local_var_params:
            query_params.append(('country_id', local_var_params['country_id']))  # noqa: E501
        if 'country_name' in local_var_params:
            query_params.append(('country_name', local_var_params['country_name']))  # noqa: E501
        if 'city_id' in local_var_params:
            query_params.append(('city_id', local_var_params['city_id']))  # noqa: E501
        if 'city_name' in local_var_params:
            query_params.append(('city_name', local_var_params['city_name']))  # noqa: E501
        if 'organizer_type' in local_var_params:
            query_params.append(('organizer_type', local_var_params['organizer_type']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/fundcards-public/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fundcards_public_read(self, id, **kwargs):  # noqa: E501
        """fundcards_public_read  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fundcards_public_read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FundCardPublicRetrieve
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.fundcards_public_read_with_http_info(id, **kwargs)  # noqa: E501

    def fundcards_public_read_with_http_info(self, id, **kwargs):  # noqa: E501
        """fundcards_public_read  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fundcards_public_read_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FundCardPublicRetrieve, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fundcards_public_read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `fundcards_public_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/fundcards-public/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FundCardPublicRetrieve',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
