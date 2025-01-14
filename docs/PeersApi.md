# hoprd_sdk.PeersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_peer**](PeersApi.md#ping_peer) | **POST** /api/v3/peers/{destination}/ping | Directly pings the given peer.
[**show_peer_info**](PeersApi.md#show_peer_info) | **GET** /api/v3/peers/{destination} | Returns transport-related information about the given peer.

# **ping_peer**
> PingResponse ping_peer(destination)

Directly pings the given peer.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.PeersApi(hoprd_sdk.ApiClient(configuration))
destination = 'destination_example' # str | PeerID or address of the requested peer

try:
    # Directly pings the given peer.
    api_response = api_instance.ping_peer(destination)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->ping_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination** | **str**| PeerID or address of the requested peer | 

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_peer_info**
> NodePeerInfoResponse show_peer_info(destination)

Returns transport-related information about the given peer.

This includes the peer ids that the given peer has `announced` on-chain and peer ids that are actually `observed` by the transport layer.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.PeersApi(hoprd_sdk.ApiClient(configuration))
destination = 'destination_example' # str | PeerID or address of the requested peer

try:
    # Returns transport-related information about the given peer.
    api_response = api_instance.show_peer_info(destination)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->show_peer_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination** | **str**| PeerID or address of the requested peer | 

### Return type

[**NodePeerInfoResponse**](NodePeerInfoResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

