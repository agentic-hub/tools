from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CopperCredentials

class CopperGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of the task to retrieve")
    opportunity_id: Optional[str] = Field(None, description="ID of the opportunity to retrieve")
    name: Optional[str] = Field(None, description="Name of the company to create")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project_id: Optional[str] = Field(None, description="ID of the project to retrieve")
    person_id: Optional[str] = Field(None, description="ID of the person to retrieve")
    lead_id: Optional[str] = Field(None, description="ID of the lead to retrieve")
    company_id: Optional[str] = Field(None, description="ID of the company to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    filter_fields: Optional[Dict[str, Any]] = Field(None, description="Filters")


class CopperGetTool(BaseTool):
    name: str = "copper_get"
    description: str = "Tool for copper get operation - get operation"
    args_schema: type[BaseModel] | None = CopperGetToolInput
    credentials: Optional[CopperCredentials] = None
