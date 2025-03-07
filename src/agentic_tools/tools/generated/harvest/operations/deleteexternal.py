from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HarvestCredentials

class HarvestDeleteexternalToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    spent_date: Optional[str] = Field(None, description="Date the expense occurred")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the time entry whose external reference you are deleting")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    task_id: Optional[str] = Field(None, description="The ID of the task to associate with the time entry")
    name: Optional[str] = Field(None, description="The name of the client")
    client_id: Optional[str] = Field(None, description="The ID of the client associated with this contact")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    first_name: Optional[str] = Field(None, description="The first name of the contact")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    project_id: Optional[str] = Field(None, description="The ID of the project associated with this expense")
    authentication: Optional[str] = Field(None, description="Authentication")


class HarvestDeleteexternalTool(BaseTool):
    name: str = "harvest_deleteexternal"
    connector_id: str = "nodes-base.harvest"
    description: str = "Tool for harvest deleteExternal operation - deleteExternal operation"
    args_schema: type[BaseModel] | None = HarvestDeleteexternalToolInput
    credentials: Optional[HarvestCredentials] = None
