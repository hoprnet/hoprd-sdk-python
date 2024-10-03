# coding: utf-8

"""
    hoprd-api

    This Rest API enables developers to interact with a hoprd node programatically through HTTP.  # noqa: E501

    OpenAPI spec version: 3.1.1
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hoprd_sdk.api_client import ApiClient


class PeersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ping_peer(self, peer_id, **kwargs):  # noqa: E501
        """Directly pings the given peer.  # noqa: E501

        Directly pings the given peer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ping_peer(peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peer_id: PeerID of the requested peer (required)
        :return: PingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ping_peer_with_http_info(peer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.ping_peer_with_http_info(peer_id, **kwargs)  # noqa: E501
            return data

    def ping_peer_with_http_info(self, peer_id, **kwargs):  # noqa: E501
        """Directly pings the given peer.  # noqa: E501

        Directly pings the given peer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ping_peer_with_http_info(peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peer_id: PeerID of the requested peer (required)
        :return: PingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['peer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ping_peer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'peer_id' is set
        if ('peer_id' not in params or
                params['peer_id'] is None):
            raise ValueError("Missing the required parameter `peer_id` when calling `ping_peer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'peer_id' in params:
            path_params['peerId'] = params['peer_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'bearer_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/peers/{peerId}/ping', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PingResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def show_peer_info(self, peer_id, **kwargs):  # noqa: E501
        """Returns transport-related information about the given peer.  # noqa: E501

        Returns transport-related information about the given peer.  This includes the peer ids that the given peer has `announced` on-chain and peer ids that are actually `observed` by the transport layer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_peer_info(peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peer_id: PeerID of the requested peer (required)
        :return: NodePeerInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.show_peer_info_with_http_info(peer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.show_peer_info_with_http_info(peer_id, **kwargs)  # noqa: E501
            return data

    def show_peer_info_with_http_info(self, peer_id, **kwargs):  # noqa: E501
        """Returns transport-related information about the given peer.  # noqa: E501

        Returns transport-related information about the given peer.  This includes the peer ids that the given peer has `announced` on-chain and peer ids that are actually `observed` by the transport layer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_peer_info_with_http_info(peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peer_id: PeerID of the requested peer (required)
        :return: NodePeerInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['peer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_peer_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'peer_id' is set
        if ('peer_id' not in params or
                params['peer_id'] is None):
            raise ValueError("Missing the required parameter `peer_id` when calling `show_peer_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'peer_id' in params:
            path_params['peerId'] = params['peer_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'bearer_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/peers/{peerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodePeerInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
