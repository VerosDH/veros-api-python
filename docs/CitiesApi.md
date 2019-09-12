# api.CitiesApi

All URIs are relative to *https://api.vedh.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cities_list**](CitiesApi.md#cities_list) | **GET** /cities/ | 
[**cities_read**](CitiesApi.md#cities_read) | **GET** /cities/{id}/ | 


# **cities_list**
> InlineResponse200 cities_list(search=search, ordering=ordering, country__name=country__name, country__id=country__id, page=page)



### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import api
from api.rest import ApiException
from pprint import pprint
configuration = api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.vedh.io/api/v1
configuration.host = "https://api.vedh.io/api/v1"
# Create an instance of the API class
api_instance = api.CitiesApi(api.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
country__name = 'country__name_example' # str |  (optional)
country__id = 3.4 # float |  (optional)
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.cities_list(search=search, ordering=ordering, country__name=country__name, country__id=country__id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CitiesApi->cities_list: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import api
from api.rest import ApiException
from pprint import pprint
configuration = api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.vedh.io/api/v1
configuration.host = "https://api.vedh.io/api/v1"
# Create an instance of the API class
api_instance = api.CitiesApi(api.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
country__name = 'country__name_example' # str |  (optional)
country__id = 3.4 # float |  (optional)
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.cities_list(search=search, ordering=ordering, country__name=country__name, country__id=country__id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CitiesApi->cities_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **country__name** | **str**|  | [optional] 
 **country__id** | **float**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **cities_read**
> City cities_read(id)



### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import api
from api.rest import ApiException
from pprint import pprint
configuration = api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.vedh.io/api/v1
configuration.host = "https://api.vedh.io/api/v1"
# Create an instance of the API class
api_instance = api.CitiesApi(api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this city.

try:
    api_response = api_instance.cities_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CitiesApi->cities_read: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import api
from api.rest import ApiException
from pprint import pprint
configuration = api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.vedh.io/api/v1
configuration.host = "https://api.vedh.io/api/v1"
# Create an instance of the API class
api_instance = api.CitiesApi(api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this city.

try:
    api_response = api_instance.cities_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CitiesApi->cities_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this city. | 

### Return type

[**City**](City.md)

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

