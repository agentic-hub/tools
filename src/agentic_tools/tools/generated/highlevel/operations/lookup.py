from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HighlevelCredentials

class HighlevelLookupToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Lookup Contact by Email. If Email is not found it will try to find a contact by phone.")
    phone: Optional[str] = Field(None, description="Lookup Contact by Phone. It will first try to find a contact by Email and than by Phone.")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="Task ID")
    opportunity_id: Optional[str] = Field(None, description="Opportunity ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    title: Optional[str] = Field(None, description="Title")


class HighlevelLookupTool(BaseTool):
    name: str = "highlevel_lookup"
    description: str = "Tool for highLevel lookup operation - lookup operation"
    args_schema: type[BaseModel] | None = HighlevelLookupToolInput
    credentials: Optional[HighlevelCredentials] = None
