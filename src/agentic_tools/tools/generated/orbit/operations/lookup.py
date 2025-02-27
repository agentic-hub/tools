from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OrbitCredentials

class OrbitLookupToolInput(BaseModel):
    member_id: Optional[str] = Field(None, description="Member ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The email address")
    workspace_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    id: Optional[str] = Field(None, description="The username at the source")
    operation: Optional[str] = Field(None, description="Operation")
    note: Optional[str] = Field(None, description="Note")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    search_by: Optional[str] = Field(None, description="Search By")
    username: Optional[str] = Field(None, description="The username at the source")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resolve_identities: Optional[bool] = Field(None, description="By default, the response just includes the reference of the identity. When set to true the identities will be resolved automatically.")
    source: Optional[str] = Field(None, description="Set to github, twitter, email, discourse or the source of any identities you've manually created")
    host: Optional[str] = Field(None, description="Host")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class OrbitLookupTool(BaseTool):
    name: str = "orbit_lookup"
    description: str = "Tool for orbit lookup operation - lookup operation"
    args_schema: type[BaseModel] | None = OrbitLookupToolInput
    credentials: Optional[OrbitCredentials] = None
