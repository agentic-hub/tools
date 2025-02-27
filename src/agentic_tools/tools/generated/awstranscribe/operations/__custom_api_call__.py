from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwstranscribeCredentials

class Awstranscribe__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Awstranscribe__custom_api_call__Tool(BaseTool):
    name: str = "awstranscribe___custom_api_call__"
    description: str = "Tool for awsTranscribe __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awstranscribe__custom_api_call__ToolInput
    credentials: Optional[AwstranscribeCredentials] = None
