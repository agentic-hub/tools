from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogledocsCredentials

class GoogledocsGetToolInput(BaseModel):
    document_url: Optional[str] = Field(None, description="The ID in the document URL (or just paste the whole URL)")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")


class GoogledocsGetTool(BaseTool):
    name: str = "googledocs_get"
    description: str = "Tool for googleDocs get operation - get operation"
    args_schema: type[BaseModel] | None = GoogledocsGetToolInput
    credentials: Optional[GoogledocsCredentials] = None
