# veros_api.FundraisingTypesApi

All URIs are relative to *https://api.vedh.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fundraising_types_list**](FundraisingTypesApi.md#fundraising_types_list) | **GET** /fundraising-types/ | 
[**fundraising_types_read**](FundraisingTypesApi.md#fundraising_types_read) | **GET** /fundraising-types/{id}/ | 


# **fundraising_types_list**
> list[FundraisingType] fundraising_types_list()



### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import veros_api
from veros_api.rest import ApiException
from pprint import pprint
configuration = veros_api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = veros_api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.vedh.io/api/v1
configuration.host = "https://api.vedh.io/api/v1"
# Create an instance of the API class
api_instance = veros_api.FundraisingTypesApi(veros_api.ApiClient(configuration))

try:
    api_response = api_instance.fundraising_types_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundraisingTypesApi->fundraising_types_list: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import veros_api
from veros_api.rest import ApiException
from pprint import pprint
configuration = veros_api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = veros_api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.vedh.io/api/v1
configuration.host = "https://api.vedh.io/api/v1"
# Create an instance of the API class
api_instance = veros_api.FundraisingTypesApi(veros_api.ApiClient(configuration))

try:
    api_response = api_instance.fundraising_types_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundraisingTypesApi->fundraising_types_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FundraisingType]**](FundraisingType.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fundraising_types_read**
> FundraisingType fundraising_types_read(id)



### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import veros_api
from veros_api.rest import ApiException
from pprint import pprint
configuration = veros_api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = veros_api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.vedh.io/api/v1
configuration.host = "https://api.vedh.io/api/v1"
# Create an instance of the API class
api_instance = veros_api.FundraisingTypesApi(veros_api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fundraising type.

try:
    api_response = api_instance.fundraising_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundraisingTypesApi->fundraising_types_read: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import veros_api
from veros_api.rest import ApiException
from pprint import pprint
configuration = veros_api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = veros_api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.vedh.io/api/v1
configuration.host = "https://api.vedh.io/api/v1"
# Create an instance of the API class
api_instance = veros_api.FundraisingTypesApi(veros_api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fundraising type.

try:
    api_response = api_instance.fundraising_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundraisingTypesApi->fundraising_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this fundraising type. | 

### Return type

[**FundraisingType**](FundraisingType.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

