from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HumanticaiCredentials

class HumanticaiUpdateToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="This value is the same as the User ID that was provided when the analysis was created. Currently only supported for profiles created using LinkedIn URL.")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    send_resume: Optional[bool] = Field(None, description="Whether to send a resume for a resume of the user")
    text: Optional[str] = Field(None, description="Additional text written by the user")
    operation: Optional[str] = Field(None, description="Operation")


class HumanticaiUpdateTool(BaseTool):
    name: str = "humanticai_update"
    description: str = "Tool for humanticAi update operation - update operation"
    args_schema: type[BaseModel] | None = HumanticaiUpdateToolInput
    credentials: Optional[HumanticaiCredentials] = None
