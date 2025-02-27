from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ConvertkitCredentials

class ConvertkitUpdateToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="The subscriber's email address")
    id: Optional[str] = Field(None, description="The ID of your custom field")
    operation: Optional[str] = Field(None, description="Operation")
    label: Optional[str] = Field(None, description="The label of the custom field")


class ConvertkitUpdateTool(BaseTool):
    name: str = "convertkit_update"
    description: str = "Tool for convertKit update operation - update operation"
    args_schema: type[BaseModel] | None = ConvertkitUpdateToolInput
    credentials: Optional[ConvertkitCredentials] = None
