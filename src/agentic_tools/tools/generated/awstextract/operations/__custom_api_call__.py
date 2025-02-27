from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwstextractCredentials

class Awstextract__custom_api_call__ToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")


class Awstextract__custom_api_call__Tool(BaseTool):
    name: str = "awstextract___custom_api_call__"
    description: str = "Tool for awsTextract __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awstextract__custom_api_call__ToolInput
    credentials: Optional[AwstextractCredentials] = None
