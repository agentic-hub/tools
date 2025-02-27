from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogledocsCredentials

class GoogledocsUpdateToolInput(BaseModel):
    document_url: Optional[str] = Field(None, description="The ID in the document URL (or just paste the whole URL)")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    actions_ui: Optional[Dict[str, Any]] = Field(None, description="Actions applied to update the document")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")


class GoogledocsUpdateTool(BaseTool):
    name: str = "googledocs_update"
    description: str = "Tool for googleDocs update operation - update operation"
    args_schema: type[BaseModel] | None = GoogledocsUpdateToolInput
    credentials: Optional[GoogledocsCredentials] = None
