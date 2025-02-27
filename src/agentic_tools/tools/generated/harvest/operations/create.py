from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HarvestCredentials

class HarvestCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    budget_by: Optional[str] = Field(None, description="The email of the user or \"none\"")
    is_billable: Optional[bool] = Field(None, description="Whether the project is billable or not")
    spent_date: Optional[str] = Field(None, description="Date the expense occurred")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="The last name of the user")
    email: Optional[str] = Field(None, description="The email of the user")
    bill_by: Optional[str] = Field(None, description="The method by which the project is invoiced")
    id: Optional[str] = Field(None, description="The ID of the client you are retrieving")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    task_id: Optional[str] = Field(None, description="The ID of the task to associate with the time entry")
    name: Optional[str] = Field(None, description="The name of the client")
    expense_category_id: Optional[str] = Field(None, description="The ID of the expense category this expense is being tracked against")
    client_id: Optional[str] = Field(None, description="The ID of the client associated with this contact")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    first_name: Optional[str] = Field(None, description="The first name of the contact")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    project_id: Optional[str] = Field(None, description="The ID of the project associated with this expense")
    authentication: Optional[str] = Field(None, description="Authentication")


class HarvestCreateTool(BaseTool):
    name: str = "harvest_create"
    description: str = "Tool for harvest create operation - create operation"
    args_schema: type[BaseModel] | None = HarvestCreateToolInput
    credentials: Optional[HarvestCredentials] = None
