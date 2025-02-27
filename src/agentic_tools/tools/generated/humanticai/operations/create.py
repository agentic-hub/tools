from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HumanticaiCredentials

class HumanticaiCreateToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="The LinkedIn profile URL or email ID for creating a Humantic profile. If you are sending the resume, this should be a unique string.")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    send_resume: Optional[bool] = Field(None, description="Whether to send a resume for a resume based analysis")
    operation: Optional[str] = Field(None, description="Operation")


class HumanticaiCreateTool(BaseTool):
    name: str = "humanticai_create"
    connector_id: str = "nodes-base.humanticAi"
    description: str = "Tool for humanticAi create operation - create operation"
    args_schema: type[BaseModel] | None = HumanticaiCreateToolInput
    credentials: Optional[HumanticaiCredentials] = None
