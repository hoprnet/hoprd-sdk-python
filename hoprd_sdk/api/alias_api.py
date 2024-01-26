# coding: utf-8

"""
    hoprd-api

    API server using the hopr-lib created HOPR node and exposing it using a HTTP REST API  # noqa: E501

    OpenAPI spec version: 0.2.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hoprd_sdk.api_client import ApiClient


class AliasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aliases(self, **kwargs):  # noqa: E501
        """Get each previously set alias and its corresponding PeerId  # noqa: E501

        Get each previously set alias and its corresponding PeerId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aliases_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.aliases_with_http_info(**kwargs)  # noqa: E501
            return data

    def aliases_with_http_info(self, **kwargs):  # noqa: E501
        """Get each previously set alias and its corresponding PeerId  # noqa: E501

        Get each previously set alias and its corresponding PeerId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aliases" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/aliases', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, str)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_alias(self, alias, **kwargs):  # noqa: E501
        """Delete an alias.  # noqa: E501

        Delete an alias.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_alias(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias to be shown (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_alias_with_http_info(alias, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_alias_with_http_info(alias, **kwargs)  # noqa: E501
            return data

    def delete_alias_with_http_info(self, alias, **kwargs):  # noqa: E501
        """Delete an alias.  # noqa: E501

        Delete an alias.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_alias_with_http_info(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias to be shown (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alias']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alias' is set
        if ('alias' not in params or
                params['alias'] is None):
            raise ValueError("Missing the required parameter `alias` when calling `delete_alias`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alias' in params:
            path_params['alias'] = params['alias']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/aliases/{alias}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_alias(self, alias, **kwargs):  # noqa: E501
        """Get alias for the PeerId (Hopr address) that have this alias assigned to it.  # noqa: E501

        Get alias for the PeerId (Hopr address) that have this alias assigned to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alias(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias to be shown (required)
        :return: PeerIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alias_with_http_info(alias, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alias_with_http_info(alias, **kwargs)  # noqa: E501
            return data

    def get_alias_with_http_info(self, alias, **kwargs):  # noqa: E501
        """Get alias for the PeerId (Hopr address) that have this alias assigned to it.  # noqa: E501

        Get alias for the PeerId (Hopr address) that have this alias assigned to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alias_with_http_info(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias to be shown (required)
        :return: PeerIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alias']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alias' is set
        if ('alias' not in params or
                params['alias'] is None):
            raise ValueError("Missing the required parameter `alias` when calling `get_alias`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alias' in params:
            path_params['alias'] = params['alias']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/aliases/{alias}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PeerIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_alias(self, body, **kwargs):  # noqa: E501
        """Set alias for a peer with a specific PeerId.  # noqa: E501

        Set alias for a peer with a specific PeerId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_alias(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AliasPeerIdBodyRequest body: Alias name along with the PeerId to be aliased (required)
        :return: PeerIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_alias_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.set_alias_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def set_alias_with_http_info(self, body, **kwargs):  # noqa: E501
        """Set alias for a peer with a specific PeerId.  # noqa: E501

        Set alias for a peer with a specific PeerId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_alias_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AliasPeerIdBodyRequest body: Alias name along with the PeerId to be aliased (required)
        :return: PeerIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_alias`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/aliases', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PeerIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
