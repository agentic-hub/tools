from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleslidesCredentials

class GoogleslidesCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="Title of the presentation to create")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleslidesCreateTool(BaseTool):
    name: str = "googleslides_create"
    description: str = "Tool for googleSlides create operation - create operation"
    args_schema: type[BaseModel] | None = GoogleslidesCreateToolInput
    credentials: Optional[GoogleslidesCredentials] = None
