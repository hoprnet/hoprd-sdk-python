# swagger_client.SettingsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_get_settings**](SettingsApi.md#settings_get_settings) | **GET** /settings/ | 
[**settings_set_setting**](SettingsApi.md#settings_set_setting) | **PUT** /settings/{setting} | 

# **settings_get_settings**
> Settings settings_get_settings()



Get all of the node's settings.

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.settings_get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Settings**](Settings.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_set_setting**
> settings_set_setting(setting, body=body)



Change this node's setting value. Check Settings schema to learn more about each setting and the type of value it expects.

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
setting = 'setting_example' # str | 
body = swagger_client.SettingsSettingBody() # SettingsSettingBody |  (optional)

try:
    api_instance.settings_set_setting(setting, body=body)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_set_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | **str**|  | 
 **body** | [**SettingsSettingBody**](SettingsSettingBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

