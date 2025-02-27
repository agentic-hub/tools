from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendinblueCredentials

class SendinblueDeleteToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    id: Optional[str] = Field(None, description="ID of the sender to delete")
    delete_attribute_name: Optional[str] = Field(None, description="Name of the attribute")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    delete_attribute_category: Optional[str] = Field(None, description="Category of the attribute")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueDeleteTool(BaseTool):
    name: str = "sendinblue_delete"
    connector_id: str = "nodes-base.sendInBlue"
    description: str = "Tool for sendInBlue delete operation - delete operation"
    args_schema: type[BaseModel] | None = SendinblueDeleteToolInput
    credentials: Optional[SendinblueCredentials] = None
