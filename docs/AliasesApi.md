# swagger_client.AliasesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aliases_get_alias**](AliasesApi.md#aliases_get_alias) | **GET** /aliases/{alias} | 
[**aliases_get_aliases**](AliasesApi.md#aliases_get_aliases) | **GET** /aliases/ | 
[**aliases_remove_alias**](AliasesApi.md#aliases_remove_alias) | **DELETE** /aliases/{alias} | 
[**aliases_set_alias**](AliasesApi.md#aliases_set_alias) | **POST** /aliases/ | 

# **aliases_get_alias**
> InlineResponse20012 aliases_get_alias(alias)



Get the PeerId (Hopr address) that have this alias assigned to it.

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
api_instance = swagger_client.AliasesApi(swagger_client.ApiClient(configuration))
alias = 'alias_example' # str | Alias that we previously assigned to some PeerId.

try:
    api_response = api_instance.aliases_get_alias(alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasesApi->aliases_get_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias that we previously assigned to some PeerId. | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aliases_get_aliases**
> InlineResponse2006 aliases_get_aliases()



Get all aliases you set previously and thier corresponding peer IDs.

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
api_instance = swagger_client.AliasesApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.aliases_get_aliases()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasesApi->aliases_get_aliases: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aliases_remove_alias**
> aliases_remove_alias(alias)



Unassign an alias from a PeerId. You can always assign back alias to that PeerId using /aliases endpoint.

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
api_instance = swagger_client.AliasesApi(swagger_client.ApiClient(configuration))
alias = 'alias_example' # str | Alias that we want to remove.

try:
    api_instance.aliases_remove_alias(alias)
except ApiException as e:
    print("Exception when calling AliasesApi->aliases_remove_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias that we want to remove. | 

### Return type

void (empty response body)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aliases_set_alias**
> aliases_set_alias(body=body)



Instead of using HOPR address, we can assign HOPR address to a specific name called alias. Give an address a more memorable alias and use it instead of Hopr address. Aliases are kept locally and are not saved or shared on the network.

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
api_instance = swagger_client.AliasesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AliasesBody() # AliasesBody |  (optional)

try:
    api_instance.aliases_set_alias(body=body)
except ApiException as e:
    print("Exception when calling AliasesApi->aliases_set_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AliasesBody**](AliasesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

