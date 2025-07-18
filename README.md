# openapi-client
The Mednet EDC (Electronic Data Capture) REST API provides a single-point of access for reading data stored across iMednet data services.
This specification documents all available endpoints in the latest version of the API.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.3.6
- Package version: 1.0.0
- Generator version: 7.14.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://edc.prod.imednetapi.com/api/v1/edc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://edc.prod.imednetapi.com/api/v1/edc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: securityKeyAuth
configuration.api_key['securityKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['securityKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AdministrationApi(api_client)
    study_key = 'study_key_example' # str | Study key identifying the study context for the request
    page = 0 # int | Page index to retrieve (0-based) (optional) (default to 0)
    size = 25 # int | Number of items to return per page (max 500) (optional) (default to 25)
    sort = 'sort_example' # str | Sorting criteria in the format `property,ASC` or `property,DESC`. Can be repeated. (optional)
    include_inactive = False # bool | For user listing, whether to include inactive users (optional) (default to False)

    try:
        # List users and their roles in a study
        api_response = api_instance.list_users(study_key, page=page, size=size, sort=sort, include_inactive=include_inactive)
        print("The response of AdministrationApi->list_users:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdministrationApi->list_users: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://edc.prod.imednetapi.com/api/v1/edc*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdministrationApi* | [**list_users**](docs/AdministrationApi.md#list_users) | **GET** /studies/{studyKey}/users | List users and their roles in a study
*CodingsApi* | [**list_codings**](docs/CodingsApi.md#list_codings) | **GET** /studies/{studyKey}/codings | List coding activities in a study
*FormsApi* | [**list_forms**](docs/FormsApi.md#list_forms) | **GET** /studies/{studyKey}/forms | List forms in a study
*IntervalsApi* | [**list_intervals**](docs/IntervalsApi.md#list_intervals) | **GET** /studies/{studyKey}/intervals | List intervals (visit definitions) in a study
*JobsApi* | [**get_job_status**](docs/JobsApi.md#get_job_status) | **GET** /studies/{studyKey}/jobs/{batchId} | Retrieve job status by batch ID
*QueriesApi* | [**list_queries**](docs/QueriesApi.md#list_queries) | **GET** /studies/{studyKey}/queries | List data queries in a study
*RecordRevisionsApi* | [**list_record_revisions**](docs/RecordRevisionsApi.md#list_record_revisions) | **GET** /studies/{studyKey}/recordRevisions | List record revisions (audit trail entries) in a study
*RecordsApi* | [**create_records**](docs/RecordsApi.md#create_records) | **POST** /studies/{studyKey}/records | Add new record or update subject/record data
*RecordsApi* | [**list_records**](docs/RecordsApi.md#list_records) | **GET** /studies/{studyKey}/records | List records (eCRF instances) in a study
*SitesApi* | [**list_sites**](docs/SitesApi.md#list_sites) | **GET** /studies/{studyKey}/sites | List sites for a study
*StudiesApi* | [**list_studies**](docs/StudiesApi.md#list_studies) | **GET** /studies | List studies accessible by API key
*SubjectsApi* | [**list_subjects**](docs/SubjectsApi.md#list_subjects) | **GET** /studies/{studyKey}/subjects | List subjects in a study
*VariablesApi* | [**list_variables**](docs/VariablesApi.md#list_variables) | **GET** /studies/{studyKey}/variables | List variables (fields) in a study
*VisitsApi* | [**list_visits**](docs/VisitsApi.md#list_visits) | **GET** /studies/{studyKey}/visits | List visits (subject visit instances) in a study


## Documentation For Models

 - [Coding](docs/Coding.md)
 - [CodingList](docs/CodingList.md)
 - [ComponentsSchemasIntervalFormsItem](docs/ComponentsSchemasIntervalFormsItem.md)
 - [ComponentsSchemasMetadataError](docs/ComponentsSchemasMetadataError.md)
 - [ComponentsSchemasRecordCreateRequestItem](docs/ComponentsSchemasRecordCreateRequestItem.md)
 - [Form](docs/Form.md)
 - [FormList](docs/FormList.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineObject5](docs/InlineObject5.md)
 - [Interval](docs/Interval.md)
 - [IntervalList](docs/IntervalList.md)
 - [Job](docs/Job.md)
 - [Keyword](docs/Keyword.md)
 - [Metadata](docs/Metadata.md)
 - [Pagination](docs/Pagination.md)
 - [Query](docs/Query.md)
 - [QueryComment](docs/QueryComment.md)
 - [QueryList](docs/QueryList.md)
 - [Record](docs/Record.md)
 - [RecordJobStatus](docs/RecordJobStatus.md)
 - [RecordList](docs/RecordList.md)
 - [RecordRevision](docs/RecordRevision.md)
 - [RecordRevisionList](docs/RecordRevisionList.md)
 - [Role](docs/Role.md)
 - [Site](docs/Site.md)
 - [SiteList](docs/SiteList.md)
 - [Sort](docs/Sort.md)
 - [Study](docs/Study.md)
 - [StudyList](docs/StudyList.md)
 - [Subject](docs/Subject.md)
 - [SubjectList](docs/SubjectList.md)
 - [User](docs/User.md)
 - [UserList](docs/UserList.md)
 - [Variable](docs/Variable.md)
 - [VariableList](docs/VariableList.md)
 - [Visit](docs/Visit.md)
 - [VisitList](docs/VisitList.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="apiKeyAuth"></a>
### apiKeyAuth

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

<a id="securityKeyAuth"></a>
### securityKeyAuth

- **Type**: API key
- **API key parameter name**: x-imn-security-key
- **Location**: HTTP header


## Author




