from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ApitemplateioCredentials

class Apitemplateio__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Apitemplateio__custom_api_call__Tool(BaseTool):
    name: str = "apitemplateio___custom_api_call__"
    description: str = "Tool for apiTemplateIo __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Apitemplateio__custom_api_call__ToolInput
    credentials: Optional[ApitemplateioCredentials] = None
