# hoprd_sdk.NodeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_graph**](NodeApi.md#channel_graph) | **GET** /api/v3/node/graph | Retrieve node&#x27;s channel graph in DOT or JSON format.
[**entry_nodes**](NodeApi.md#entry_nodes) | **GET** /api/v3/node/entryNodes | List all known entry nodes with multiaddrs and eligibility.
[**info**](NodeApi.md#info) | **GET** /api/v3/node/info | Get information about this HOPR Node.
[**metrics**](NodeApi.md#metrics) | **GET** /api/v3/node/metrics | Retrieve Prometheus metrics from the running node.
[**peers**](NodeApi.md#peers) | **GET** /api/v3/node/peers | Lists information for &#x60;connected peers&#x60; and &#x60;announced peers&#x60;.
[**version**](NodeApi.md#version) | **GET** /api/v3/node/version | Get the release version of the running node.

# **channel_graph**
> str channel_graph(ignore_disconnected_components=ignore_disconnected_components, ignore_non_opened_channels=ignore_non_opened_channels, raw_graph=raw_graph)

Retrieve node's channel graph in DOT or JSON format.

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
api_instance = hoprd_sdk.NodeApi(hoprd_sdk.ApiClient(configuration))
ignore_disconnected_components = true # bool | If set, nodes that are not connected to this node (via open channels) will not be exported. This setting automatically implies `ignore_non_opened_channels`. (optional)
ignore_non_opened_channels = true # bool | Do not export channels that are not in the `Open` state. (optional)
raw_graph = true # bool | Export the entire graph in raw JSON format, that can be later used to load the graph into e.g. a unit test.  Note that `ignore_disconnected_components` and `ignore_non_opened_channels` are ignored. (optional)

try:
    # Retrieve node's channel graph in DOT or JSON format.
    api_response = api_instance.channel_graph(ignore_disconnected_components=ignore_disconnected_components, ignore_non_opened_channels=ignore_non_opened_channels, raw_graph=raw_graph)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->channel_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ignore_disconnected_components** | **bool**| If set, nodes that are not connected to this node (via open channels) will not be exported. This setting automatically implies &#x60;ignore_non_opened_channels&#x60;. | [optional] 
 **ignore_non_opened_channels** | **bool**| Do not export channels that are not in the &#x60;Open&#x60; state. | [optional] 
 **raw_graph** | **bool**| Export the entire graph in raw JSON format, that can be later used to load the graph into e.g. a unit test.  Note that &#x60;ignore_disconnected_components&#x60; and &#x60;ignore_non_opened_channels&#x60; are ignored. | [optional] 

### Return type

**str**

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entry_nodes**
> dict(str, EntryNode) entry_nodes()

List all known entry nodes with multiaddrs and eligibility.

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
api_instance = hoprd_sdk.NodeApi(hoprd_sdk.ApiClient(configuration))

try:
    # List all known entry nodes with multiaddrs and eligibility.
    api_response = api_instance.entry_nodes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->entry_nodes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, EntryNode)**](EntryNode.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> NodeInfoResponse info()

Get information about this HOPR Node.

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
api_instance = hoprd_sdk.NodeApi(hoprd_sdk.ApiClient(configuration))

try:
    # Get information about this HOPR Node.
    api_response = api_instance.info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeInfoResponse**](NodeInfoResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics**
> str metrics()

Retrieve Prometheus metrics from the running node.

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
api_instance = hoprd_sdk.NodeApi(hoprd_sdk.ApiClient(configuration))

try:
    # Retrieve Prometheus metrics from the running node.
    api_response = api_instance.metrics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peers**
> NodePeersResponse peers(quality=quality)

Lists information for `connected peers` and `announced peers`.

Connected peers are nodes which are connected to the node while announced peers are nodes which have announced to the network.  Optionally pass `quality` parameter to get only peers with higher or equal quality to the specified value.

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
api_instance = hoprd_sdk.NodeApi(hoprd_sdk.ApiClient(configuration))
quality = 1.2 # float |  (optional)

try:
    # Lists information for `connected peers` and `announced peers`.
    api_response = api_instance.peers(quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quality** | **float**|  | [optional] 

### Return type

[**NodePeersResponse**](NodePeersResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version**
> NodeVersionResponse version()

Get the release version of the running node.

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
api_instance = hoprd_sdk.NodeApi(hoprd_sdk.ApiClient(configuration))

try:
    # Get the release version of the running node.
    api_response = api_instance.version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeVersionResponse**](NodeVersionResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

