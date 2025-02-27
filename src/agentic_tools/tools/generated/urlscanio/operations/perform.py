from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import UrlscanioCredentials

class UrlscanioPerformToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    url: Optional[str] = Field(None, description="URL to scan")
    operation: Optional[str] = Field(None, description="Operation")


class UrlscanioPerformTool(BaseTool):
    name: str = "urlscanio_perform"
    description: str = "Tool for urlScanIo perform operation - perform operation"
    args_schema: type[BaseModel] | None = UrlscanioPerformToolInput
    credentials: Optional[UrlscanioCredentials] = None
