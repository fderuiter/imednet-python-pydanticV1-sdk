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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class Role(BaseModel):
    """
    Role
    """
    date_created: Optional[conlist(StrictInt)] = Field(default=None, alias="dateCreated", description="Timestamp when the role assignment was created (as [year, month, day, hour, minute, second, nanosecond])")
    date_modified: Optional[conlist(StrictInt)] = Field(default=None, alias="dateModified", description="Timestamp when the role assignment was last modified")
    role_id: Optional[StrictStr] = Field(default=None, alias="roleId", description="Unique role ID (UUID)")
    community_id: Optional[StrictInt] = Field(default=None, alias="communityId", description="Community ID or level associated with the role")
    name: Optional[StrictStr] = Field(default=None, description="Name of the role")
    description: Optional[StrictStr] = Field(default=None, description="Description of the role")
    level: Optional[StrictInt] = Field(default=None, description="Role level or hierarchy")
    type: Optional[StrictStr] = Field(default=None, description="Role type/category")
    inactive: Optional[StrictBool] = Field(default=None, description="Whether the role is inactive")
    __properties = ["dateCreated", "dateModified", "roleId", "communityId", "name", "description", "level", "type", "inactive"]

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
    def from_json(cls, json_str: str) -> Role:
        """Create an instance of Role from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Role:
        """Create an instance of Role from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Role.parse_obj(obj)

        _obj = Role.parse_obj({
            "date_created": obj.get("dateCreated"),
            "date_modified": obj.get("dateModified"),
            "role_id": obj.get("roleId"),
            "community_id": obj.get("communityId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "level": obj.get("level"),
            "type": obj.get("type"),
            "inactive": obj.get("inactive")
        })
        return _obj


