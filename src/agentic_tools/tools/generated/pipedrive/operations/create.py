from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PipedriveCredentials

class PipedriveCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="The content of the note to create")
    file_id: Optional[float] = Field(None, description="ID of the file to delete")
    type: Optional[str] = Field(None, description="Type of the activity like \"call\", \"meeting\", etc")
    org_id: Optional[float] = Field(None, description="ID of the organization this deal will be associated with")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    person_id: Optional[float] = Field(None, description="ID of the person this deal will be associated with")
    activity_id: Optional[float] = Field(None, description="ID of the activity to delete")
    subject: Optional[str] = Field(None, description="The subject of the activity to create")
    operation: Optional[str] = Field(None, description="Operation")
    product_attachment_id: Optional[str] = Field(None, description="ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    done: Optional[str] = Field(None, description="Whether the activity is done or not")
    name: Optional[str] = Field(None, description="The name of the organization to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    associate_with: Optional[str] = Field(None, description="Type of entity to link to this deal")
    person_id: Optional[float] = Field(None, description="ID of the person to delete")
    organization_id: Optional[float] = Field(None, description="ID of the organization to link to this lead")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    deal_id: Optional[float] = Field(None, description="ID of the deal to delete")
    term: Optional[str] = Field(None, description="The search term to look for. Minimum 2 characters (or 1 if using exact_match).")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    organization_id: Optional[float] = Field(None, description="ID of the organization to delete")
    authentication: Optional[str] = Field(None, description="Authentication")
    note_id: Optional[float] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="The title of the deal to create")
    lead_id: Optional[str] = Field(None, description="ID of the lead to delete")


class PipedriveCreateTool(BaseTool):
    name: str = "pipedrive_create"
    description: str = "Tool for pipedrive create operation - create operation"
    args_schema: type[BaseModel] | None = PipedriveCreateToolInput
    credentials: Optional[PipedriveCredentials] = None
