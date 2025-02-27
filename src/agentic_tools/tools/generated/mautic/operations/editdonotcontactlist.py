from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MauticCredentials

class MauticEditdonotcontactlistToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    channel: Optional[str] = Field(None, description="Channel")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    company_id: Optional[str] = Field(None, description="The ID of the company to update")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    action: Optional[str] = Field(None, description="Action")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Contact ID")


class MauticEditdonotcontactlistTool(BaseTool):
    name: str = "mautic_editdonotcontactlist"
    description: str = "Tool for mautic editDoNotContactList operation - editDoNotContactList operation"
    args_schema: type[BaseModel] | None = MauticEditdonotcontactlistToolInput
    credentials: Optional[MauticCredentials] = None
