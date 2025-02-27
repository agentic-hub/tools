from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ContentfulCredentials

class ContentfulGetToolInput(BaseModel):
    source: Optional[str] = Field(None, description="Pick where your data comes from, delivery or preview API")
    content_type_id: Optional[str] = Field(None, description="Content Type ID")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    entry_id: Optional[str] = Field(None, description="Entry ID")
    asset_id: Optional[str] = Field(None, description="Asset ID")
    environment_id: Optional[str] = Field(None, description="The ID for the Contentful environment (e.g. master, staging, etc.). Depending on your plan, you might not have environments. In that case use \"master\".")
    operation: Optional[str] = Field(None, description="Operation")


class ContentfulGetTool(BaseTool):
    name: str = "contentful_get"
    description: str = "Tool for contentful get operation - get operation"
    args_schema: type[BaseModel] | None = ContentfulGetToolInput
    credentials: Optional[ContentfulCredentials] = None
