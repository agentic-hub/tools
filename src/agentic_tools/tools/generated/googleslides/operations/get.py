from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleslidesCredentials

class GoogleslidesGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    page_object_id: Optional[str] = Field(None, description="ID of the page object to retrieve")
    authentication: Optional[str] = Field(None, description="Authentication")
    presentation_id: Optional[str] = Field(None, description="ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleslidesGetTool(BaseTool):
    name: str = "googleslides_get"
    connector_id: str = "nodes-base.googleSlides"
    description: str = "Tool for googleSlides get operation - get operation"
    args_schema: type[BaseModel] | None = GoogleslidesGetToolInput
    credentials: Optional[GoogleslidesCredentials] = None
