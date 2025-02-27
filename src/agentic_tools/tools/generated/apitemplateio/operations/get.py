from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ApitemplateioCredentials

class ApitemplateioGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class ApitemplateioGetTool(BaseTool):
    name: str = "apitemplateio_get"
    description: str = "Tool for apiTemplateIo get operation - get operation"
    args_schema: type[BaseModel] | None = ApitemplateioGetToolInput
    credentials: Optional[ApitemplateioCredentials] = None
