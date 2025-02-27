from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DemioCredentials

class DemioRegisterToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    event_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    first_name: Optional[str] = Field(None, description="The registrant's first name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="The registrant's email address")
    operation: Optional[str] = Field(None, description="Operation")


class DemioRegisterTool(BaseTool):
    name: str = "demio_register"
    description: str = "Tool for demio register operation - register operation"
    args_schema: type[BaseModel] | None = DemioRegisterToolInput
    credentials: Optional[DemioCredentials] = None
