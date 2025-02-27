from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import UrlscanioCredentials

class UrlscanioGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class UrlscanioGetallTool(BaseTool):
    name: str = "urlscanio_getall"
    description: str = "Tool for urlScanIo getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = UrlscanioGetallToolInput
    credentials: Optional[UrlscanioCredentials] = None
