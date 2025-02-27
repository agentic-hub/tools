from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BitwardenCredentials

class BitwardenGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    access_all: Optional[bool] = Field(None, description="Whether to allow this group to access all collections within the organization, instead of only its associated collections. If set to true, this option overrides any collection assignments.")
    operation: Optional[str] = Field(None, description="Operation")


class BitwardenGetallTool(BaseTool):
    name: str = "bitwarden_getall"
    description: str = "Tool for bitwarden getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = BitwardenGetallToolInput
    credentials: Optional[BitwardenCredentials] = None
