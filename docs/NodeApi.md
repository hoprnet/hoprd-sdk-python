# hoprd_sdk.NodeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entry_nodes**](NodeApi.md#entry_nodes) | **GET** /api/v3/node/entryNodes | List all known entry nodes with multiaddrs and eligibility.
[**info**](NodeApi.md#info) | **GET** /api/v3/node/info | Get information about this HOPR Node.
[**metrics**](NodeApi.md#metrics) | **GET** /api/v3/node/metrics | Retrieve Prometheus metrics from the running node.
[**peers**](NodeApi.md#peers) | **GET** /api/v3/node/peers | Lists information for &#x60;connected peers&#x60; and &#x60;announced peers&#x60;.
[**version**](NodeApi.md#version) | **GET** /api/v3/node/version | Get release version of the running node.

# **entry_nodes**
> dict(str, EntryNode) entry_nodes()

List all known entry nodes with multiaddrs and eligibility.

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

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> NodeInfoRes info()

Get information about this HOPR Node.

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

[**NodeInfoRes**](NodeInfoRes.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics**
> str metrics()

Retrieve Prometheus metrics from the running node.

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

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peers**
> NodePeersRes peers(quality=quality)

Lists information for `connected peers` and `announced peers`.

Lists information for `connected peers` and `announced peers`.  Connected peers are nodes which are connected to the node while announced peers are nodes which have announced to the network.  Optionally pass `quality` parameter to get only peers with higher or equal quality to the specified value.

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

[**NodePeersRes**](NodePeersRes.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version**
> NodeVersion version()

Get release version of the running node.

Get release version of the running node.

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
    # Get release version of the running node.
    api_response = api_instance.version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeVersion**](NodeVersion.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

