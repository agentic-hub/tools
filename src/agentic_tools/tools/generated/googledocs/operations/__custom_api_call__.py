from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogledocsCredentials

class Googledocs__custom_api_call__ToolInput(BaseModel):
    document_url: Optional[str] = Field(None, description="The ID in the document URL (or just paste the whole URL)")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")


class Googledocs__custom_api_call__Tool(BaseTool):
    name: str = "googledocs___custom_api_call__"
    description: str = "Tool for googleDocs __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googledocs__custom_api_call__ToolInput
    credentials: Optional[GoogledocsCredentials] = None
