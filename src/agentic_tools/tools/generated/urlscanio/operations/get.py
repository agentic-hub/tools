from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import UrlscanioCredentials

class UrlscanioGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    scan_id: Optional[str] = Field(None, description="ID of the scan to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class UrlscanioGetTool(BaseTool):
    name: str = "urlscanio_get"
    connector_id: str = "nodes-base.urlScanIo"
    description: str = "Tool for urlScanIo get operation - get operation"
    args_schema: type[BaseModel] | None = UrlscanioGetToolInput
    credentials: Optional[UrlscanioCredentials] = None
