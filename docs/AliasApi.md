# hoprd_sdk.AliasApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aliases**](AliasApi.md#aliases) | **GET** /api/v3/aliases | Get each previously set alias and its corresponding PeerId
[**delete_alias**](AliasApi.md#delete_alias) | **DELETE** /api/v3/aliases/{alias} | Delete an alias.
[**get_alias**](AliasApi.md#get_alias) | **GET** /api/v3/aliases/{alias} | Get alias for the PeerId (Hopr address) that have this alias assigned to it.
[**set_alias**](AliasApi.md#set_alias) | **POST** /api/v3/aliases | Set alias for a peer with a specific PeerId.

# **aliases**
> dict(str, str) aliases()

Get each previously set alias and its corresponding PeerId

Get each previously set alias and its corresponding PeerId

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
api_instance = hoprd_sdk.AliasApi(hoprd_sdk.ApiClient(configuration))

try:
    # Get each previously set alias and its corresponding PeerId
    api_response = api_instance.aliases()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApi->aliases: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, str)**

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alias**
> delete_alias(alias)

Delete an alias.

Delete an alias.

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
api_instance = hoprd_sdk.AliasApi(hoprd_sdk.ApiClient(configuration))
alias = 'alias_example' # str | Alias to be shown

try:
    # Delete an alias.
    api_instance.delete_alias(alias)
except ApiException as e:
    print("Exception when calling AliasApi->delete_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias to be shown | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alias**
> PeerIdResponse get_alias(alias)

Get alias for the PeerId (Hopr address) that have this alias assigned to it.

Get alias for the PeerId (Hopr address) that have this alias assigned to it.

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
api_instance = hoprd_sdk.AliasApi(hoprd_sdk.ApiClient(configuration))
alias = 'alias_example' # str | Alias to be shown

try:
    # Get alias for the PeerId (Hopr address) that have this alias assigned to it.
    api_response = api_instance.get_alias(alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApi->get_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias to be shown | 

### Return type

[**PeerIdResponse**](PeerIdResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_alias**
> PeerIdResponse set_alias(body)

Set alias for a peer with a specific PeerId.

Set alias for a peer with a specific PeerId.

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
api_instance = hoprd_sdk.AliasApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.AliasPeerIdBodyRequest() # AliasPeerIdBodyRequest | Alias name along with the PeerId to be aliased

try:
    # Set alias for a peer with a specific PeerId.
    api_response = api_instance.set_alias(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApi->set_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AliasPeerIdBodyRequest**](AliasPeerIdBodyRequest.md)| Alias name along with the PeerId to be aliased | 

### Return type

[**PeerIdResponse**](PeerIdResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

