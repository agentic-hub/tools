from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendyCredentials

class SendyDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    list_id: Optional[str] = Field(None, description="The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID.")
    email: Optional[str] = Field(None, description="Email address of the subscriber")
    operation: Optional[str] = Field(None, description="Operation")


class SendyDeleteTool(BaseTool):
    name: str = "sendy_delete"
    connector_id: str = "nodes-base.sendy"
    description: str = "Tool for sendy delete operation - delete operation"
    args_schema: type[BaseModel] | None = SendyDeleteToolInput
    credentials: Optional[SendyCredentials] = None
