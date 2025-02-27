from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleslidesCredentials

class GoogleslidesReplacetextToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    text_ui: Optional[Dict[str, Any]] = Field(None, description="Texts To Replace")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    presentation_id: Optional[str] = Field(None, description="ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleslidesReplacetextTool(BaseTool):
    name: str = "googleslides_replacetext"
    description: str = "Tool for googleSlides replaceText operation - replaceText operation"
    args_schema: type[BaseModel] | None = GoogleslidesReplacetextToolInput
    credentials: Optional[GoogleslidesCredentials] = None
