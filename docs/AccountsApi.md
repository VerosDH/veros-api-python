# veros_api.AccountsApi

All URIs are relative to *https://api.vedh.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_login**](AccountsApi.md#accounts_login) | **POST** /accounts/login/ | 
[**accounts_password_reset**](AccountsApi.md#accounts_password_reset) | **POST** /accounts/password_reset/ | 
[**accounts_password_reset_confirm**](AccountsApi.md#accounts_password_reset_confirm) | **POST** /accounts/password_reset_confirm/ | 
[**accounts_registration**](AccountsApi.md#accounts_registration) | **POST** /accounts/registration/ | 
[**accounts_send_verify_email**](AccountsApi.md#accounts_send_verify_email) | **GET** /accounts/send-verify-email/{email}/ | 
[**accounts_verify_email**](AccountsApi.md#accounts_verify_email) | **GET** /accounts/{id}/verify-email/{key}/ | 


# **accounts_login**
> UserLoginResponse accounts_login(data)



Retrieve auth token by pair of username & password.

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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
data = veros_api.JSONWebToken() # JSONWebToken | 

try:
    api_response = api_instance.accounts_login(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_login: %s\n" % e)
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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
data = veros_api.JSONWebToken() # JSONWebToken | 

try:
    api_response = api_instance.accounts_login(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JSONWebToken**](JSONWebToken.md)|  | 

### Return type

[**UserLoginResponse**](UserLoginResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**410** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_password_reset**
> PasswordReset accounts_password_reset(data)



View for working with user data.

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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
data = veros_api.PasswordReset() # PasswordReset | 

try:
    api_response = api_instance.accounts_password_reset(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_password_reset: %s\n" % e)
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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
data = veros_api.PasswordReset() # PasswordReset | 

try:
    api_response = api_instance.accounts_password_reset(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PasswordReset**](PasswordReset.md)|  | 

### Return type

[**PasswordReset**](PasswordReset.md)

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

# **accounts_password_reset_confirm**
> PasswordResetConfirm accounts_password_reset_confirm(data)



View for working with user data.

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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
data = veros_api.PasswordResetConfirm() # PasswordResetConfirm | 

try:
    api_response = api_instance.accounts_password_reset_confirm(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_password_reset_confirm: %s\n" % e)
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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
data = veros_api.PasswordResetConfirm() # PasswordResetConfirm | 

try:
    api_response = api_instance.accounts_password_reset_confirm(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_password_reset_confirm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PasswordResetConfirm**](PasswordResetConfirm.md)|  | 

### Return type

[**PasswordResetConfirm**](PasswordResetConfirm.md)

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

# **accounts_registration**
> UserFull accounts_registration(data)



Register user with first_name, last_name, email, phone, password1, password2 fields.

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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
data = veros_api.UserRegistration() # UserRegistration | 

try:
    api_response = api_instance.accounts_registration(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_registration: %s\n" % e)
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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
data = veros_api.UserRegistration() # UserRegistration | 

try:
    api_response = api_instance.accounts_registration(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserRegistration**](UserRegistration.md)|  | 

### Return type

[**UserFull**](UserFull.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_send_verify_email**
> object accounts_send_verify_email(email, search=search, ordering=ordering, page=page)



Send verify user email.

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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
email = 'email_example' # str | 
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.accounts_send_verify_email(email, search=search, ordering=ordering, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_send_verify_email: %s\n" % e)
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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
email = 'email_example' # str | 
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.accounts_send_verify_email(email, search=search, ordering=ordering, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_send_verify_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

**object**

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_verify_email**
> object accounts_verify_email(id, key)



Verify user email.

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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this User.
key = 'key_example' # str | 

try:
    api_response = api_instance.accounts_verify_email(id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_verify_email: %s\n" % e)
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
api_instance = veros_api.AccountsApi(veros_api.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this User.
key = 'key_example' # str | 

try:
    api_response = api_instance.accounts_verify_email(id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_verify_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **key** | **str**|  | 

### Return type

**object**

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

