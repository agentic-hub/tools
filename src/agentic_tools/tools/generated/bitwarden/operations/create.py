from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BitwardenCredentials

class BitwardenCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    name: Optional[str] = Field(None, description="The name of the group to create")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="The email of the member to update")
    access_all: Optional[bool] = Field(None, description="Whether to allow this group to access all collections within the organization, instead of only its associated collections. If set to true, this option overrides any collection assignments.")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class BitwardenCreateTool(BaseTool):
    name: str = "bitwarden_create"
    description: str = "Tool for bitwarden create operation - create operation"
    args_schema: type[BaseModel] | None = BitwardenCreateToolInput
    credentials: Optional[BitwardenCredentials] = None
