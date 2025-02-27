from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CopperCredentials

class CopperUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of the task to update")
    opportunity_id: Optional[str] = Field(None, description="ID of the opportunity to update")
    name: Optional[str] = Field(None, description="Name of the company to create")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project_id: Optional[str] = Field(None, description="ID of the project to update")
    person_id: Optional[str] = Field(None, description="ID of the person to update")
    lead_id: Optional[str] = Field(None, description="ID of the lead to update")
    company_id: Optional[str] = Field(None, description="ID of the company to update")
    operation: Optional[str] = Field(None, description="Operation")
    filter_fields: Optional[Dict[str, Any]] = Field(None, description="Filters")


class CopperUpdateTool(BaseTool):
    name: str = "copper_update"
    connector_id: str = "nodes-base.copper"
    description: str = "Tool for copper update operation - update operation"
    args_schema: type[BaseModel] | None = CopperUpdateToolInput
    credentials: Optional[CopperCredentials] = None
