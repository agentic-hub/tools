from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OrbitCredentials

class OrbitCreateToolInput(BaseModel):
    member_id: Optional[str] = Field(None, description="Member ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    workspace_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    note: Optional[str] = Field(None, description="Note")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    url: Optional[str] = Field(None, description="Supply any URL and Orbit will do its best job to parse out a title, description, and image")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resolve_identities: Optional[bool] = Field(None, description="By default, the response just includes the reference of the identity. When set to true the identities will be resolved automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title")


class OrbitCreateTool(BaseTool):
    name: str = "orbit_create"
    connector_id: str = "nodes-base.orbit"
    description: str = "Tool for orbit create operation - create operation"
    args_schema: type[BaseModel] | None = OrbitCreateToolInput
    credentials: Optional[OrbitCredentials] = None
