from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LinkedinCredentials

class Linkedin__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    post_as: Optional[str] = Field(None, description="If to post on behalf of a user or an organization")
    operation: Optional[str] = Field(None, description="Operation")


class Linkedin__custom_api_call__Tool(BaseTool):
    name: str = "linkedin___custom_api_call__"
    description: str = "Tool for linkedIn __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Linkedin__custom_api_call__ToolInput
    credentials: Optional[LinkedinCredentials] = None
