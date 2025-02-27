from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AutopilotCredentials

class AutopilotUpsertToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="Email address of the contact")
    contact_id: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutopilotUpsertTool(BaseTool):
    name: str = "autopilot_upsert"
    description: str = "Tool for autopilot upsert operation - upsert operation"
    args_schema: type[BaseModel] | None = AutopilotUpsertToolInput
    credentials: Optional[AutopilotCredentials] = None
