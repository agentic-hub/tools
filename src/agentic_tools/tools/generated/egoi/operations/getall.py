from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import EgoiCredentials

class EgoiGetallToolInput(BaseModel):
    list: Optional[str] = Field(None, description="ID of list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="Email address for a subscriber")
    contact_id: Optional[str] = Field(None, description="Contact ID of the subscriber")
    operation: Optional[str] = Field(None, description="Operation")


class EgoiGetallTool(BaseTool):
    name: str = "egoi_getall"
    description: str = "Tool for egoi getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = EgoiGetallToolInput
    credentials: Optional[EgoiCredentials] = None
