# api.FeedbackThemesApi

All URIs are relative to *http://localhost:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feedback_themes_list**](FeedbackThemesApi.md#feedback_themes_list) | **GET** /feedback-themes/ | 


# **feedback_themes_list**
> InlineResponse2002 feedback_themes_list(search=search, ordering=ordering, page=page)



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
api_instance = api.FeedbackThemesApi(api.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.feedback_themes_list(search=search, ordering=ordering, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedbackThemesApi->feedback_themes_list: %s\n" % e)
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
api_instance = api.FeedbackThemesApi(api.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.feedback_themes_list(search=search, ordering=ordering, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedbackThemesApi->feedback_themes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

