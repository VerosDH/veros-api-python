# api.FundcardsApi

All URIs are relative to *http://localhost:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fundcards_list**](FundcardsApi.md#fundcards_list) | **GET** /fundcards/ | 
[**fundcards_read**](FundcardsApi.md#fundcards_read) | **GET** /fundcards/{id}/ | 


# **fundcards_list**
> InlineResponse2004 fundcards_list(directions=directions, fundraising_type=fundraising_type, payment_types=payment_types, disabled=disabled, search=search, ordering=ordering, limit=limit, offset=offset)



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

# Defining host is optional and default to http://localhost:8000/api/v1
configuration.host = "http://localhost:8000/api/v1"
# Create an instance of the API class
api_instance = api.FundcardsApi(api.ApiClient(configuration))
directions = 'directions_example' # str | Multiple values may be separated by commas. (optional)
fundraising_type = 'fundraising_type_example' # str | Multiple values may be separated by commas. (optional)
payment_types = 'payment_types_example' # str | Multiple values may be separated by commas. (optional)
disabled = 'disabled_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.fundcards_list(directions=directions, fundraising_type=fundraising_type, payment_types=payment_types, disabled=disabled, search=search, ordering=ordering, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsApi->fundcards_list: %s\n" % e)
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

# Defining host is optional and default to http://localhost:8000/api/v1
configuration.host = "http://localhost:8000/api/v1"
# Create an instance of the API class
api_instance = api.FundcardsApi(api.ApiClient(configuration))
directions = 'directions_example' # str | Multiple values may be separated by commas. (optional)
fundraising_type = 'fundraising_type_example' # str | Multiple values may be separated by commas. (optional)
payment_types = 'payment_types_example' # str | Multiple values may be separated by commas. (optional)
disabled = 'disabled_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.fundcards_list(directions=directions, fundraising_type=fundraising_type, payment_types=payment_types, disabled=disabled, search=search, ordering=ordering, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsApi->fundcards_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directions** | **str**| Multiple values may be separated by commas. | [optional] 
 **fundraising_type** | **str**| Multiple values may be separated by commas. | [optional] 
 **payment_types** | **str**| Multiple values may be separated by commas. | [optional] 
 **disabled** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **fundcards_read**
> FundCard fundcards_read(id)



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

# Defining host is optional and default to http://localhost:8000/api/v1
configuration.host = "http://localhost:8000/api/v1"
# Create an instance of the API class
api_instance = api.FundcardsApi(api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fund card.

try:
    api_response = api_instance.fundcards_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsApi->fundcards_read: %s\n" % e)
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

# Defining host is optional and default to http://localhost:8000/api/v1
configuration.host = "http://localhost:8000/api/v1"
# Create an instance of the API class
api_instance = api.FundcardsApi(api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fund card.

try:
    api_response = api_instance.fundcards_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsApi->fundcards_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this fund card. | 

### Return type

[**FundCard**](FundCard.md)

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

