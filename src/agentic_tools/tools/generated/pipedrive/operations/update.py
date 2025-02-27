from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PipedriveCredentials

class PipedriveUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    encode_properties: Optional[bool] = Field(None, description="By default do custom properties have to be set as ID instead of their actual name. Also option fields have to be set as ID instead of their actual value. If this option gets set they get automatically encoded.")
    file_id: Optional[float] = Field(None, description="ID of the file to update")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    person_id: Optional[float] = Field(None, description="ID of the person this deal will be associated with")
    activity_id: Optional[float] = Field(None, description="ID of the activity to update")
    operation: Optional[str] = Field(None, description="Operation")
    product_attachment_id: Optional[str] = Field(None, description="ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    name: Optional[str] = Field(None, description="The name of the organization to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    associate_with: Optional[str] = Field(None, description="Type of entity to link to this deal")
    person_id: Optional[float] = Field(None, description="ID of the person to update")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    deal_id: Optional[float] = Field(None, description="ID of the deal to update")
    term: Optional[str] = Field(None, description="The search term to look for. Minimum 2 characters (or 1 if using exact_match).")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    organization_id: Optional[float] = Field(None, description="The ID of the organization to create")
    authentication: Optional[str] = Field(None, description="Authentication")
    note_id: Optional[float] = Field(None, description="ID of the note to update")
    title: Optional[str] = Field(None, description="The title of the deal to create")
    lead_id: Optional[str] = Field(None, description="ID of the lead to update")


class PipedriveUpdateTool(BaseTool):
    name: str = "pipedrive_update"
    description: str = "Tool for pipedrive update operation - update operation"
    args_schema: type[BaseModel] | None = PipedriveUpdateToolInput
    credentials: Optional[PipedriveCredentials] = None
