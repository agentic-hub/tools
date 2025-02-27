from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BitwardenCredentials

class BitwardenUpdategroupsToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    member_id: Optional[str] = Field(None, description="The identifier of the member")
    access_all: Optional[bool] = Field(None, description="Whether to allow this group to access all collections within the organization, instead of only its associated collections. If set to true, this option overrides any collection assignments.")
    group_ids: Optional[str] = Field(None, description="Comma-separated list of IDs of groups to set for a member")
    operation: Optional[str] = Field(None, description="Operation")


class BitwardenUpdategroupsTool(BaseTool):
    name: str = "bitwarden_updategroups"
    connector_id: str = "nodes-base.bitwarden"
    description: str = "Tool for bitwarden updateGroups operation - updateGroups operation"
    args_schema: type[BaseModel] | None = BitwardenUpdategroupsToolInput
    credentials: Optional[BitwardenCredentials] = None
