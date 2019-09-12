# api
Routes of Veros project

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = api.AccountsApi(api.ApiClient(configuration))
data = api.JSONWebToken() # JSONWebToken | 

try:
    api_response = api_instance.accounts_login(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_login: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8000/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**accounts_login**](docs/AccountsApi.md#accounts_login) | **POST** /accounts/login/ | 
*AccountsApi* | [**accounts_password_reset**](docs/AccountsApi.md#accounts_password_reset) | **POST** /accounts/password_reset/ | 
*AccountsApi* | [**accounts_password_reset_confirm**](docs/AccountsApi.md#accounts_password_reset_confirm) | **POST** /accounts/password_reset_confirm/ | 
*AccountsApi* | [**accounts_registration**](docs/AccountsApi.md#accounts_registration) | **POST** /accounts/registration/ | 
*AccountsApi* | [**accounts_send_verify_email**](docs/AccountsApi.md#accounts_send_verify_email) | **GET** /accounts/send-verify-email/{email}/ | 
*AccountsApi* | [**accounts_verify_email**](docs/AccountsApi.md#accounts_verify_email) | **GET** /accounts/{id}/verify-email/{key}/ | 
*CitiesApi* | [**cities_list**](docs/CitiesApi.md#cities_list) | **GET** /cities/ | 
*CitiesApi* | [**cities_read**](docs/CitiesApi.md#cities_read) | **GET** /cities/{id}/ | 
*CountriesApi* | [**countries_list**](docs/CountriesApi.md#countries_list) | **GET** /countries/ | 
*CountriesApi* | [**countries_read**](docs/CountriesApi.md#countries_read) | **GET** /countries/{id}/ | 
*DirectionsApi* | [**directions_list**](docs/DirectionsApi.md#directions_list) | **GET** /directions/ | 
*DirectionsApi* | [**directions_read**](docs/DirectionsApi.md#directions_read) | **GET** /directions/{id}/ | 
*FeedbackThemesApi* | [**feedback_themes_list**](docs/FeedbackThemesApi.md#feedback_themes_list) | **GET** /feedback-themes/ | 
*FundcardsApi* | [**fundcards_list**](docs/FundcardsApi.md#fundcards_list) | **GET** /fundcards/ | 
*FundcardsApi* | [**fundcards_read**](docs/FundcardsApi.md#fundcards_read) | **GET** /fundcards/{id}/ | 
*FundcardsPublicApi* | [**fundcards_public_donate**](docs/FundcardsPublicApi.md#fundcards_public_donate) | **POST** /fundcards-public/{id}/donate/ | 
*FundcardsPublicApi* | [**fundcards_public_list**](docs/FundcardsPublicApi.md#fundcards_public_list) | **GET** /fundcards-public/ | 
*FundcardsPublicApi* | [**fundcards_public_read**](docs/FundcardsPublicApi.md#fundcards_public_read) | **GET** /fundcards-public/{id}/ | 
*FundraisingTypesApi* | [**fundraising_types_list**](docs/FundraisingTypesApi.md#fundraising_types_list) | **GET** /fundraising-types/ | 
*FundraisingTypesApi* | [**fundraising_types_read**](docs/FundraisingTypesApi.md#fundraising_types_read) | **GET** /fundraising-types/{id}/ | 
*OrganizationsApi* | [**organizations_list**](docs/OrganizationsApi.md#organizations_list) | **GET** /organizations/ | 
*OrganizationsApi* | [**organizations_read**](docs/OrganizationsApi.md#organizations_read) | **GET** /organizations/{id}/ | 
*PaymentTypesApi* | [**payment_types_list**](docs/PaymentTypesApi.md#payment_types_list) | **GET** /payment-types/ | 
*PaymentTypesApi* | [**payment_types_read**](docs/PaymentTypesApi.md#payment_types_read) | **GET** /payment-types/{id}/ | 


## Documentation For Models

 - [BadRequestResponse](docs/BadRequestResponse.md)
 - [City](docs/City.md)
 - [CityLight](docs/CityLight.md)
 - [Country](docs/Country.md)
 - [CountryLight](docs/CountryLight.md)
 - [Direction](docs/Direction.md)
 - [FeedbackTheme](docs/FeedbackTheme.md)
 - [FundCard](docs/FundCard.md)
 - [FundCardDonate](docs/FundCardDonate.md)
 - [FundCardPublicList](docs/FundCardPublicList.md)
 - [FundCardPublicRetrieve](docs/FundCardPublicRetrieve.md)
 - [FundraisingType](docs/FundraisingType.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [JSONWebToken](docs/JSONWebToken.md)
 - [Organization](docs/Organization.md)
 - [OrganizationLight](docs/OrganizationLight.md)
 - [PasswordReset](docs/PasswordReset.md)
 - [PasswordResetConfirm](docs/PasswordResetConfirm.md)
 - [PaymentType](docs/PaymentType.md)
 - [UserFull](docs/UserFull.md)
 - [UserLight](docs/UserLight.md)
 - [UserLoginResponse](docs/UserLoginResponse.md)
 - [UserRegistration](docs/UserRegistration.md)


## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




