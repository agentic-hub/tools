from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendinblueCredentials

class SendinblueCreateToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    attribute_category_list: Optional[Dict[str, Any]] = Field(None, description="Contact Attribute List")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    attribute_type: Optional[str] = Field(None, description="Attribute Type")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the sender")
    attribute_value: Optional[str] = Field(None, description="Value of the attribute")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    attribute_category: Optional[str] = Field(None, description="Category of the attribute")
    attribute_name: Optional[str] = Field(None, description="Name of the attribute")
    create_contact_attributes: Optional[Dict[str, Any]] = Field(None, description="Array of attributes to be added")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueCreateTool(BaseTool):
    name: str = "sendinblue_create"
    connector_id: str = "nodes-base.sendInBlue"
    description: str = "Tool for sendInBlue create operation - create operation"
    args_schema: type[BaseModel] | None = SendinblueCreateToolInput
    credentials: Optional[SendinblueCredentials] = None
