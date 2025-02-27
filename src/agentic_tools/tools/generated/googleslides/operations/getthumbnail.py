from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleslidesCredentials

class GoogleslidesGetthumbnailToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Name of the binary property to which to write the data of the read page")
    resource: Optional[str] = Field(None, description="Resource")
    page_object_id: Optional[str] = Field(None, description="ID of the page object to retrieve")
    authentication: Optional[str] = Field(None, description="Authentication")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    presentation_id: Optional[str] = Field(None, description="ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleslidesGetthumbnailTool(BaseTool):
    name: str = "googleslides_getthumbnail"
    description: str = "Tool for googleSlides getThumbnail operation - getThumbnail operation"
    args_schema: type[BaseModel] | None = GoogleslidesGetthumbnailToolInput
    credentials: Optional[GoogleslidesCredentials] = None
