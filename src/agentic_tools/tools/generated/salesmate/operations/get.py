from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SalesmateCredentials

class SalesmateGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    raw_data: Optional[bool] = Field(None, description="Whether the data should include the fields details")
    id: Optional[str] = Field(None, description="Company ID")
    operation: Optional[str] = Field(None, description="Operation")
    filters_json: Optional[str] = Field(None, description="Filters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title")
    owner: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class SalesmateGetTool(BaseTool):
    name: str = "salesmate_get"
    description: str = "Tool for salesmate get operation - get operation"
    args_schema: type[BaseModel] | None = SalesmateGetToolInput
    credentials: Optional[SalesmateCredentials] = None
