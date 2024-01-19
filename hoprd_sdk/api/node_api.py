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


class NodeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def entry_nodes(self, **kwargs):  # noqa: E501
        """List all known entry nodes with multiaddrs and eligibility.  # noqa: E501

        List all known entry nodes with multiaddrs and eligibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entry_nodes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, EntryNode)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.entry_nodes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.entry_nodes_with_http_info(**kwargs)  # noqa: E501
            return data

    def entry_nodes_with_http_info(self, **kwargs):  # noqa: E501
        """List all known entry nodes with multiaddrs and eligibility.  # noqa: E501

        List all known entry nodes with multiaddrs and eligibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entry_nodes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, EntryNode)
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
                    " to method entry_nodes" % key
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
            '/api/v3/node/entryNodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, EntryNode)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def info(self, **kwargs):  # noqa: E501
        """Get information about this HOPR Node.  # noqa: E501

        Get information about this HOPR Node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeInfoRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.info_with_http_info(**kwargs)  # noqa: E501
            return data

    def info_with_http_info(self, **kwargs):  # noqa: E501
        """Get information about this HOPR Node.  # noqa: E501

        Get information about this HOPR Node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeInfoRes
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
                    " to method info" % key
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
            '/api/v3/node/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeInfoRes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def metrics(self, **kwargs):  # noqa: E501
        """Retrieve Prometheus metrics from the running node.  # noqa: E501

        Retrieve Prometheus metrics from the running node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.metrics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.metrics_with_http_info(**kwargs)  # noqa: E501
            return data

    def metrics_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve Prometheus metrics from the running node.  # noqa: E501

        Retrieve Prometheus metrics from the running node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
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
                    " to method metrics" % key
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
            ['text/plain', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/node/metrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def peers(self, **kwargs):  # noqa: E501
        """Lists information for `connected peers` and `announced peers`.  # noqa: E501

        Lists information for `connected peers` and `announced peers`.  Connected peers are nodes which are connected to the node while announced peers are nodes which have announced to the network.  Optionally pass `quality` parameter to get only peers with higher or equal quality to the specified value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float quality:
        :return: NodePeersRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.peers_with_http_info(**kwargs)  # noqa: E501
            return data

    def peers_with_http_info(self, **kwargs):  # noqa: E501
        """Lists information for `connected peers` and `announced peers`.  # noqa: E501

        Lists information for `connected peers` and `announced peers`.  Connected peers are nodes which are connected to the node while announced peers are nodes which have announced to the network.  Optionally pass `quality` parameter to get only peers with higher or equal quality to the specified value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float quality:
        :return: NodePeersRes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quality']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method peers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'quality' in params:
            query_params.append(('quality', params['quality']))  # noqa: E501

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
            '/api/v3/node/peers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodePeersRes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def version(self, **kwargs):  # noqa: E501
        """Get release version of the running node.  # noqa: E501

        Get release version of the running node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.version(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.version_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.version_with_http_info(**kwargs)  # noqa: E501
            return data

    def version_with_http_info(self, **kwargs):  # noqa: E501
        """Get release version of the running node.  # noqa: E501

        Get release version of the running node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeVersion
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
                    " to method version" % key
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
            '/api/v3/node/version', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
