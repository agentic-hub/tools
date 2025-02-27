from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import EgoiCredentials

class EgoiGetToolInput(BaseModel):
    list: Optional[str] = Field(None, description="ID of list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    by: Optional[str] = Field(None, description="Search by")
    email: Optional[str] = Field(None, description="Email address for subscriber")
    contact_id: Optional[str] = Field(None, description="Contact ID of the subscriber")
    operation: Optional[str] = Field(None, description="Operation")


class EgoiGetTool(BaseTool):
    name: str = "egoi_get"
    description: str = "Tool for egoi get operation - get operation"
    args_schema: type[BaseModel] | None = EgoiGetToolInput
    credentials: Optional[EgoiCredentials] = None
