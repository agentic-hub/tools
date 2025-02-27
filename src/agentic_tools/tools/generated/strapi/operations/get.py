from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StrapiCredentials

class StrapiGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    entry_id: Optional[str] = Field(None, description="The ID of the entry to get")
    content_type: Optional[str] = Field(None, description="Name of the content type")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class StrapiGetTool(BaseTool):
    name: str = "strapi_get"
    description: str = "Tool for strapi get operation - get operation"
    args_schema: type[BaseModel] | None = StrapiGetToolInput
    credentials: Optional[StrapiCredentials] = None
