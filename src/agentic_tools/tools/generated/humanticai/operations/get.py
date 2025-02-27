from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HumanticaiCredentials

class HumanticaiGetToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="This value is the same as the User ID that was provided when the analysis was created. This could be a LinkedIn URL, email ID, or a unique string in case of resume based analysis.")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    send_resume: Optional[bool] = Field(None, description="Whether to send a resume for a resume based analysis")
    operation: Optional[str] = Field(None, description="Operation")


class HumanticaiGetTool(BaseTool):
    name: str = "humanticai_get"
    connector_id: str = "nodes-base.humanticAi"
    description: str = "Tool for humanticAi get operation - get operation"
    args_schema: type[BaseModel] | None = HumanticaiGetToolInput
    credentials: Optional[HumanticaiCredentials] = None
