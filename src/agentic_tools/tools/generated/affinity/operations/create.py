from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AffinityCredentials

class AffinityCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="The last name of the person")
    list_entry_id: Optional[str] = Field(None, description="The unique ID of the list entry object to be retrieved")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the organization")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="The unique ID of the list whose list entries are to be retrieved. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    person_id: Optional[str] = Field(None, description="Unique identifier for the person")
    domain: Optional[str] = Field(None, description="The domain name of the organization")
    emails: Optional[str] = Field(None, description="The email addresses of the person")
    entity_id: Optional[str] = Field(None, description="The unique ID of the entity (person, organization, or opportunity) to add to this list")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    first_name: Optional[str] = Field(None, description="The first name of the person")
    organization_id: Optional[str] = Field(None, description="Unique identifier for the organization")


class AffinityCreateTool(BaseTool):
    name: str = "affinity_create"
    description: str = "Tool for affinity create operation - create operation"
    args_schema: type[BaseModel] | None = AffinityCreateToolInput
    credentials: Optional[AffinityCredentials] = None
