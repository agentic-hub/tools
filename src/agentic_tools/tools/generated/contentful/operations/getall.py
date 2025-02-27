from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ContentfulCredentials

class ContentfulGetallToolInput(BaseModel):
    source: Optional[str] = Field(None, description="Pick where your data comes from, delivery or preview API")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    environment_id: Optional[str] = Field(None, description="The ID for the Contentful environment (e.g. master, staging, etc.). Depending on your plan, you might not have environments. In that case use \"master\".")
    operation: Optional[str] = Field(None, description="Operation")


class ContentfulGetallTool(BaseTool):
    name: str = "contentful_getall"
    description: str = "Tool for contentful getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = ContentfulGetallToolInput
    credentials: Optional[ContentfulCredentials] = None
