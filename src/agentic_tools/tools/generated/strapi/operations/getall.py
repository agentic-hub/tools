from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StrapiCredentials

class StrapiGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    entry_id: Optional[str] = Field(None, description="The ID of the entry to delete")
    content_type: Optional[str] = Field(None, description="Name of the content type")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class StrapiGetallTool(BaseTool):
    name: str = "strapi_getall"
    description: str = "Tool for strapi getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = StrapiGetallToolInput
    credentials: Optional[StrapiCredentials] = None
