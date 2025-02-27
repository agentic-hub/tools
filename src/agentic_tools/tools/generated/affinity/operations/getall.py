from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AffinityCredentials

class AffinityGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    list_entry_id: Optional[str] = Field(None, description="The unique ID of the list entry object to be retrieved")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="The unique ID of the list whose list entries are to be retrieved. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    person_id: Optional[str] = Field(None, description="Unique identifier for the person")
    emails: Optional[str] = Field(None, description="The email addresses of the person")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    organization_id: Optional[str] = Field(None, description="Unique identifier for the organization")


class AffinityGetallTool(BaseTool):
    name: str = "affinity_getall"
    connector_id: str = "nodes-base.affinity"
    description: str = "Tool for affinity getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = AffinityGetallToolInput
    credentials: Optional[AffinityCredentials] = None
