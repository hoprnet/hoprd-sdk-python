# coding: utf-8

"""
    HOPRd Rest API v3

    This Rest API enables developers to interact with a hoprd node programatically.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PeerInfoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def peer_info_get_peer_info(self, peerid, **kwargs):  # noqa: E501
        """peer_info_get_peer_info  # noqa: E501

        Get information about this peer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peer_info_get_peer_info(peerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peerid: (required)
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peer_info_get_peer_info_with_http_info(peerid, **kwargs)  # noqa: E501
        else:
            (data) = self.peer_info_get_peer_info_with_http_info(peerid, **kwargs)  # noqa: E501
            return data

    def peer_info_get_peer_info_with_http_info(self, peerid, **kwargs):  # noqa: E501
        """peer_info_get_peer_info  # noqa: E501

        Get information about this peer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peer_info_get_peer_info_with_http_info(peerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peerid: (required)
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['peerid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method peer_info_get_peer_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'peerid' is set
        if ('peerid' not in params or
                params['peerid'] is None):
            raise ValueError("Missing the required parameter `peerid` when calling `peer_info_get_peer_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'peerid' in params:
            path_params['peerid'] = params['peerid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/peers/{peerid}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
