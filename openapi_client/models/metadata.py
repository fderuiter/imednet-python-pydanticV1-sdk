# coding: utf-8

"""
    Mednet EDC API

    The Mednet EDC (Electronic Data Capture) REST API provides a single-point of access for reading data stored across iMednet data services. This specification documents all available endpoints in the latest version of the API. 

    The version of the OpenAPI document: 1.3.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.components_schemas_metadata_error import ComponentsSchemasMetadataError

class Metadata(BaseModel):
    """
    Metadata
    """
    status: Optional[StrictStr] = Field(default=None, description="HTTP status of the response (e.g., OK or ERROR)")
    method: Optional[StrictStr] = Field(default=None, description="HTTP method of the request")
    path: Optional[StrictStr] = Field(default=None, description="Requested URI path")
    timestamp: Optional[datetime] = Field(default=None, description="Timestamp when response was generated")
    error: Optional[ComponentsSchemasMetadataError] = None
    __properties = ["status", "method", "path", "timestamp", "error"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Metadata:
        """Create an instance of Metadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Metadata:
        """Create an instance of Metadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Metadata.parse_obj(obj)

        _obj = Metadata.parse_obj({
            "status": obj.get("status"),
            "method": obj.get("method"),
            "path": obj.get("path"),
            "timestamp": obj.get("timestamp"),
            "error": ComponentsSchemasMetadataError.from_dict(obj.get("error")) if obj.get("error") is not None else None
        })
        return _obj


