# coding: utf-8

"""
    Mednet EDC API

    The Mednet EDC (Electronic Data Capture) REST API provides a single-point of access for reading data stored across iMednet data services. This specification documents all available endpoints in the latest version of the API. 

    The version of the OpenAPI document: 1.3.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.record_list import RecordList  # noqa: E501

class TestRecordList(unittest.TestCase):
    """RecordList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecordList:
        """Test RecordList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecordList`
        """
        model = RecordList()  # noqa: E501
        if include_optional:
            return RecordList(
                metadata = openapi_client.models.metadata.Metadata(
                    status = '', 
                    method = '', 
                    path = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    error = { }, ),
                pagination = openapi_client.models.pagination.Pagination(
                    current_page = 56, 
                    size = 56, 
                    total_pages = 56, 
                    total_elements = 56, 
                    sort = [
                        openapi_client.models.sort.Sort(
                            property = '', 
                            direction = 'ASC', )
                        ], ),
                data = [
                    openapi_client.models.record.Record(
                        study_key = '', 
                        interval_id = 56, 
                        form_id = 56, 
                        form_key = '', 
                        site_id = 56, 
                        record_id = 56, 
                        record_oid = '', 
                        record_type = '', 
                        record_status = '', 
                        deleted = True, 
                        date_created = '', 
                        date_modified = '', 
                        subject_id = 56, 
                        subject_oid = '', 
                        subject_key = '', 
                        visit_id = 56, 
                        parent_record_id = 56, 
                        keywords = [
                            openapi_client.models.keyword.Keyword(
                                keyword_name = '', 
                                keyword_key = '', 
                                keyword_id = 56, 
                                date_added = '', )
                            ], 
                        record_data = { }, )
                    ]
            )
        else:
            return RecordList(
        )
        """

    def testRecordList(self):
        """Test RecordList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
