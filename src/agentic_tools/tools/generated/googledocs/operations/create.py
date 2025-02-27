from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogledocsCredentials

class GoogledocsCreateToolInput(BaseModel):
    document_url: Optional[str] = Field(None, description="The ID in the document URL (or just paste the whole URL)")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    drive_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    title: Optional[str] = Field(None, description="Title")
    folder_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogledocsCreateTool(BaseTool):
    name: str = "googledocs_create"
    description: str = "Tool for googleDocs create operation - create operation"
    args_schema: type[BaseModel] | None = GoogledocsCreateToolInput
    credentials: Optional[GoogledocsCredentials] = None
