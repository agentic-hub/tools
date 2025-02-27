from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PipedriveCredentials

class Pipedrive__custom_api_call__ToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    file_id: Optional[float] = Field(None, description="ID of the file to delete")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    person_id: Optional[float] = Field(None, description="ID of the person this deal will be associated with")
    activity_id: Optional[float] = Field(None, description="ID of the activity to delete")
    operation: Optional[str] = Field(None, description="Operation")
    product_attachment_id: Optional[str] = Field(None, description="ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    name: Optional[str] = Field(None, description="The name of the organization to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    associate_with: Optional[str] = Field(None, description="Type of entity to link to this deal")
    person_id: Optional[float] = Field(None, description="ID of the person to delete")
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


class Pipedrive__custom_api_call__Tool(BaseTool):
    name: str = "pipedrive___custom_api_call__"
    description: str = "Tool for pipedrive __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Pipedrive__custom_api_call__ToolInput
    credentials: Optional[PipedriveCredentials] = None
