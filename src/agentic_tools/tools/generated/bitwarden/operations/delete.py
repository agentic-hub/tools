from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BitwardenCredentials

class BitwardenDeleteToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    member_id: Optional[str] = Field(None, description="The identifier of the member")
    access_all: Optional[bool] = Field(None, description="Whether to allow this group to access all collections within the organization, instead of only its associated collections. If set to true, this option overrides any collection assignments.")
    collection_id: Optional[str] = Field(None, description="The identifier of the collection")
    group_id: Optional[str] = Field(None, description="The identifier of the group")
    operation: Optional[str] = Field(None, description="Operation")


class BitwardenDeleteTool(BaseTool):
    name: str = "bitwarden_delete"
    connector_id: str = "nodes-base.bitwarden"
    description: str = "Tool for bitwarden delete operation - delete operation"
    args_schema: type[BaseModel] | None = BitwardenDeleteToolInput
    credentials: Optional[BitwardenCredentials] = None
