# veros_api.DirectionsApi

All URIs are relative to *https://api.vedh.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directions_list**](DirectionsApi.md#directions_list) | **GET** /directions/ | 
[**directions_read**](DirectionsApi.md#directions_read) | **GET** /directions/{id}/ | 


# **directions_list**
> list[Direction] directions_list()



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
api_instance = veros_api.DirectionsApi(veros_api.ApiClient(configuration))

try:
    api_response = api_instance.directions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectionsApi->directions_list: %s\n" % e)
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
api_instance = veros_api.DirectionsApi(veros_api.ApiClient(configuration))

try:
    api_response = api_instance.directions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectionsApi->directions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Direction]**](Direction.md)

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

# **directions_read**
> Direction directions_read(id)



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
api_instance = veros_api.DirectionsApi(veros_api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this direction.

try:
    api_response = api_instance.directions_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectionsApi->directions_read: %s\n" % e)
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
api_instance = veros_api.DirectionsApi(veros_api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this direction.

try:
    api_response = api_instance.directions_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectionsApi->directions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this direction. | 

### Return type

[**Direction**](Direction.md)

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

