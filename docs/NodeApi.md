# swagger_client.NodeApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**node_get_entry_nodes**](NodeApi.md#node_get_entry_nodes) | **GET** /node/entryNodes | 
[**node_get_info**](NodeApi.md#node_get_info) | **GET** /node/info | 
[**node_get_metrics**](NodeApi.md#node_get_metrics) | **GET** /node/metrics | 
[**node_get_peers**](NodeApi.md#node_get_peers) | **GET** /node/peers | 
[**node_get_version**](NodeApi.md#node_get_version) | **GET** /node/version | 

# **node_get_entry_nodes**
> dict(str, InlineResponseMap200) node_get_entry_nodes()



List all known entry nodes and their multiaddrs and their eligibility state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.node_get_entry_nodes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->node_get_entry_nodes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, InlineResponseMap200)**](InlineResponseMap200.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_get_info**
> InlineResponse2002 node_get_info()



Information about the HOPR Node, including any options it started with. See the schema of the response to get more information on each field.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.node_get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->node_get_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_get_metrics**
> str node_get_metrics()



Retrieve Prometheus metrics from the running node.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.node_get_metrics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->node_get_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; version=0.0.4, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_get_peers**
> InlineResponse2001 node_get_peers(quality=quality)



Lists information for `connected peers` and `announced peers`. Connected peers are nodes which are connected to the node while announced peers are nodes which have announced to the network. Optionally, you can pass `quality` parameter which would filter out peers with lower quality to the one specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))
quality = 1.2 # float | When quality is passed, the response will only include peers with higher or equal quality to the one specified. (optional)

try:
    api_response = api_instance.node_get_peers(quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->node_get_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quality** | **float**| When quality is passed, the response will only include peers with higher or equal quality to the one specified. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_get_version**
> str node_get_version()



Get release version of the running node.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.node_get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->node_get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

