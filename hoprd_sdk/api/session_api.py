# coding: utf-8

"""
    hoprd-api

    This Rest API enables developers to interact with a hoprd node programatically through HTTP.  # noqa: E501

    OpenAPI spec version: 3.10.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hoprd_sdk.api_client import ApiClient


class SessionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def close_client(self, protocol, ip, port, **kwargs):  # noqa: E501
        """Closes an existing Session listener.  # noqa: E501

        The listener must've been previously created and bound for the given IP protocol. Once a listener is closed, no more socket connections can be made to it. If the passed port number is 0, listeners on all ports of the given listening IP and protocol will be closed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.close_client(protocol, ip, port, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IpProtocol protocol: (required)
        :param str ip: (required)
        :param int port: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.close_client_with_http_info(protocol, ip, port, **kwargs)  # noqa: E501
        else:
            (data) = self.close_client_with_http_info(protocol, ip, port, **kwargs)  # noqa: E501
            return data

    def close_client_with_http_info(self, protocol, ip, port, **kwargs):  # noqa: E501
        """Closes an existing Session listener.  # noqa: E501

        The listener must've been previously created and bound for the given IP protocol. Once a listener is closed, no more socket connections can be made to it. If the passed port number is 0, listeners on all ports of the given listening IP and protocol will be closed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.close_client_with_http_info(protocol, ip, port, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IpProtocol protocol: (required)
        :param str ip: (required)
        :param int port: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['protocol', 'ip', 'port']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method close_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'protocol' is set
        if ('protocol' not in params or
                params['protocol'] is None):
            raise ValueError("Missing the required parameter `protocol` when calling `close_client`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if ('ip' not in params or
                params['ip'] is None):
            raise ValueError("Missing the required parameter `ip` when calling `close_client`")  # noqa: E501
        # verify the required parameter 'port' is set
        if ('port' not in params or
                params['port'] is None):
            raise ValueError("Missing the required parameter `port` when calling `close_client`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'protocol' in params:
            path_params['protocol'] = params['protocol']  # noqa: E501
        if 'ip' in params:
            path_params['ip'] = params['ip']  # noqa: E501
        if 'port' in params:
            path_params['port'] = params['port']  # noqa: E501

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
            '/api/v3/session/{protocol}/{ip}/{port}', 'DELETE',
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

    def create_client(self, body, protocol, **kwargs):  # noqa: E501
        """Creates a new client session returning the given session listening host and port over TCP or UDP.  # noqa: E501

        If no listening port is given in the request, the socket will be bound to a random free port and returned in the response. Different capabilities can be configured for the session, such as data segmentation or retransmission.  Once the host and port are bound, it is possible to use the socket for bidirectional read/write communication over the selected IP protocol and HOPR network routing with the given destination. The destination HOPR node forwards all the data to the given target over the selected IP protocol.  Various services require different types of socket communications: - services running over UDP usually do not require data retransmission, as it is already expected that UDP does not provide these and is therefore handled at the application layer. - On the contrary, services running over TCP *almost always* expect data segmentation and retransmission capabilities, so these should be configured while creating a session that passes TCP data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client(body, protocol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SessionClientRequest body: Creates a new client HOPR session that will start listening on a dedicated port. Once the port is bound, it is possible to use the socket for bidirectional read and write communication. (required)
        :param str protocol: IP transport protocol (required)
        :return: SessionClientResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_client_with_http_info(body, protocol, **kwargs)  # noqa: E501
        else:
            (data) = self.create_client_with_http_info(body, protocol, **kwargs)  # noqa: E501
            return data

    def create_client_with_http_info(self, body, protocol, **kwargs):  # noqa: E501
        """Creates a new client session returning the given session listening host and port over TCP or UDP.  # noqa: E501

        If no listening port is given in the request, the socket will be bound to a random free port and returned in the response. Different capabilities can be configured for the session, such as data segmentation or retransmission.  Once the host and port are bound, it is possible to use the socket for bidirectional read/write communication over the selected IP protocol and HOPR network routing with the given destination. The destination HOPR node forwards all the data to the given target over the selected IP protocol.  Various services require different types of socket communications: - services running over UDP usually do not require data retransmission, as it is already expected that UDP does not provide these and is therefore handled at the application layer. - On the contrary, services running over TCP *almost always* expect data segmentation and retransmission capabilities, so these should be configured while creating a session that passes TCP data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client_with_http_info(body, protocol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SessionClientRequest body: Creates a new client HOPR session that will start listening on a dedicated port. Once the port is bound, it is possible to use the socket for bidirectional read and write communication. (required)
        :param str protocol: IP transport protocol (required)
        :return: SessionClientResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'protocol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_client`")  # noqa: E501
        # verify the required parameter 'protocol' is set
        if ('protocol' not in params or
                params['protocol'] is None):
            raise ValueError("Missing the required parameter `protocol` when calling `create_client`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'protocol' in params:
            path_params['protocol'] = params['protocol']  # noqa: E501

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
        auth_settings = ['api_token', 'bearer_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/session/{protocol}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SessionClientResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_clients(self, protocol, **kwargs):  # noqa: E501
        """Lists existing Session listeners for the given IP protocol.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_clients(protocol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protocol: IP transport protocol (required)
        :return: list[SessionClientResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_clients_with_http_info(protocol, **kwargs)  # noqa: E501
        else:
            (data) = self.list_clients_with_http_info(protocol, **kwargs)  # noqa: E501
            return data

    def list_clients_with_http_info(self, protocol, **kwargs):  # noqa: E501
        """Lists existing Session listeners for the given IP protocol.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_clients_with_http_info(protocol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protocol: IP transport protocol (required)
        :return: list[SessionClientResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['protocol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_clients" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'protocol' is set
        if ('protocol' not in params or
                params['protocol'] is None):
            raise ValueError("Missing the required parameter `protocol` when calling `list_clients`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'protocol' in params:
            path_params['protocol'] = params['protocol']  # noqa: E501

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
            '/api/v3/session/{protocol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SessionClientResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
