from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendinblueCredentials

class SendinblueUpdateToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    update_attributes: Optional[Dict[str, Any]] = Field(None, description="Array of attributes to be updated")
    update_attribute_category_list: Optional[Dict[str, Any]] = Field(None, description="List of the values and labels that the attribute can take")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    update_attribute_category: Optional[str] = Field(None, description="Category of the attribute")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    update_attribute_name: Optional[str] = Field(None, description="Name of the existing attribute")
    update_attribute_value: Optional[str] = Field(None, description="Value of the attribute to update")


class SendinblueUpdateTool(BaseTool):
    name: str = "sendinblue_update"
    connector_id: str = "nodes-base.sendInBlue"
    description: str = "Tool for sendInBlue update operation - update operation"
    args_schema: type[BaseModel] | None = SendinblueUpdateToolInput
    credentials: Optional[SendinblueCredentials] = None
