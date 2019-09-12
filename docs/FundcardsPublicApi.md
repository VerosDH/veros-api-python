# api.FundcardsPublicApi

All URIs are relative to *http://localhost:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fundcards_public_donate**](FundcardsPublicApi.md#fundcards_public_donate) | **POST** /fundcards-public/{id}/donate/ | 
[**fundcards_public_list**](FundcardsPublicApi.md#fundcards_public_list) | **GET** /fundcards-public/ | 
[**fundcards_public_read**](FundcardsPublicApi.md#fundcards_public_read) | **GET** /fundcards-public/{id}/ | 


# **fundcards_public_donate**
> FundCardDonate fundcards_public_donate(id, data)



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
api_instance = api.FundcardsPublicApi(api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fund card.
data = api.FundCardDonate() # FundCardDonate | 

try:
    api_response = api_instance.fundcards_public_donate(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsPublicApi->fundcards_public_donate: %s\n" % e)
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
api_instance = api.FundcardsPublicApi(api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fund card.
data = api.FundCardDonate() # FundCardDonate | 

try:
    api_response = api_instance.fundcards_public_donate(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsPublicApi->fundcards_public_donate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this fund card. | 
 **data** | [**FundCardDonate**](FundCardDonate.md)|  | 

### Return type

[**FundCardDonate**](FundCardDonate.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fundcards_public_list**
> InlineResponse2003 fundcards_public_list(directions=directions, fundraising_type=fundraising_type, payment_types=payment_types, ids=ids, search=search, ordering=ordering, country_id=country_id, country_name=country_name, organizer_type=organizer_type, limit=limit, offset=offset)



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
api_instance = api.FundcardsPublicApi(api.ApiClient(configuration))
directions = 'directions_example' # str | Multiple values may be separated by commas. (optional)
fundraising_type = 'fundraising_type_example' # str | Multiple values may be separated by commas. (optional)
payment_types = 'payment_types_example' # str | Multiple values may be separated by commas. (optional)
ids = 'ids_example' # str | Multiple values may be separated by commas. (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
country_id = 'country_id_example' # str | Country ID (optional)
country_name = 'country_name_example' # str | Country name (optional)
organizer_type = 'organizer_type_example' # str | Organizer Type (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.fundcards_public_list(directions=directions, fundraising_type=fundraising_type, payment_types=payment_types, ids=ids, search=search, ordering=ordering, country_id=country_id, country_name=country_name, organizer_type=organizer_type, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsPublicApi->fundcards_public_list: %s\n" % e)
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
api_instance = api.FundcardsPublicApi(api.ApiClient(configuration))
directions = 'directions_example' # str | Multiple values may be separated by commas. (optional)
fundraising_type = 'fundraising_type_example' # str | Multiple values may be separated by commas. (optional)
payment_types = 'payment_types_example' # str | Multiple values may be separated by commas. (optional)
ids = 'ids_example' # str | Multiple values may be separated by commas. (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
country_id = 'country_id_example' # str | Country ID (optional)
country_name = 'country_name_example' # str | Country name (optional)
organizer_type = 'organizer_type_example' # str | Organizer Type (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.fundcards_public_list(directions=directions, fundraising_type=fundraising_type, payment_types=payment_types, ids=ids, search=search, ordering=ordering, country_id=country_id, country_name=country_name, organizer_type=organizer_type, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsPublicApi->fundcards_public_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directions** | **str**| Multiple values may be separated by commas. | [optional] 
 **fundraising_type** | **str**| Multiple values may be separated by commas. | [optional] 
 **payment_types** | **str**| Multiple values may be separated by commas. | [optional] 
 **ids** | **str**| Multiple values may be separated by commas. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **country_id** | **str**| Country ID | [optional] 
 **country_name** | **str**| Country name | [optional] 
 **organizer_type** | **str**| Organizer Type | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **fundcards_public_read**
> FundCardPublicRetrieve fundcards_public_read(id)



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
api_instance = api.FundcardsPublicApi(api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fund card.

try:
    api_response = api_instance.fundcards_public_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsPublicApi->fundcards_public_read: %s\n" % e)
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
api_instance = api.FundcardsPublicApi(api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fund card.

try:
    api_response = api_instance.fundcards_public_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundcardsPublicApi->fundcards_public_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this fund card. | 

### Return type

[**FundCardPublicRetrieve**](FundCardPublicRetrieve.md)

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

