from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleslidesCredentials

class GoogleslidesGetslidesToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    presentation_id: Optional[str] = Field(None, description="ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleslidesGetslidesTool(BaseTool):
    name: str = "googleslides_getslides"
    description: str = "Tool for googleSlides getSlides operation - getSlides operation"
    args_schema: type[BaseModel] | None = GoogleslidesGetslidesToolInput
    credentials: Optional[GoogleslidesCredentials] = None
