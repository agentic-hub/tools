from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AutomizyCredentials

class AutomizyUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    name: Optional[str] = Field(None, description="Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    list_id: Optional[str] = Field(None, description="List ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="Email")
    contact_id: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutomizyUpdateTool(BaseTool):
    name: str = "automizy_update"
    description: str = "Tool for automizy update operation - update operation"
    args_schema: type[BaseModel] | None = AutomizyUpdateToolInput
    credentials: Optional[AutomizyCredentials] = None
