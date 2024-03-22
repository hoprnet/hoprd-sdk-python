# hoprd_sdk.ChecksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthyz**](ChecksApi.md#healthyz) | **GET** /healthyz | Check whether the node is healthy
[**readyz**](ChecksApi.md#readyz) | **GET** /readyz | Check whether the node is ready to accept connections.
[**startedz**](ChecksApi.md#startedz) | **GET** /startedz | Check whether the node is started.

# **healthyz**
> healthyz()

Check whether the node is healthy

Check whether the node is healthy

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hoprd_sdk.ChecksApi()

try:
    # Check whether the node is healthy
    api_instance.healthyz()
except ApiException as e:
    print("Exception when calling ChecksApi->healthyz: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **readyz**
> readyz()

Check whether the node is ready to accept connections.

Check whether the node is ready to accept connections.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hoprd_sdk.ChecksApi()

try:
    # Check whether the node is ready to accept connections.
    api_instance.readyz()
except ApiException as e:
    print("Exception when calling ChecksApi->readyz: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **startedz**
> startedz()

Check whether the node is started.

Check whether the node is started.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hoprd_sdk.ChecksApi()

try:
    # Check whether the node is started.
    api_instance.startedz()
except ApiException as e:
    print("Exception when calling ChecksApi->startedz: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

