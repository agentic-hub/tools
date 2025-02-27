from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SalesmateCredentials

class SalesmateCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    type: Optional[str] = Field(None, description="This field displays activity type such as call, meeting etc")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    raw_data: Optional[bool] = Field(None, description="Whether the data should include the fields details")
    id: Optional[str] = Field(None, description="Company ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    filters_json: Optional[str] = Field(None, description="Filters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    stage: Optional[str] = Field(None, description="Stage")
    primary_contact: Optional[str] = Field(None, description="Primary contact for the deal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    currency: Optional[str] = Field(None, description="Currency")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    title: Optional[str] = Field(None, description="Title")
    owner: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    pipeline: Optional[str] = Field(None, description="Pipeline")


class SalesmateCreateTool(BaseTool):
    name: str = "salesmate_create"
    connector_id: str = "nodes-base.salesmate"
    description: str = "Tool for salesmate create operation - create operation"
    args_schema: type[BaseModel] | None = SalesmateCreateToolInput
    credentials: Optional[SalesmateCredentials] = None
