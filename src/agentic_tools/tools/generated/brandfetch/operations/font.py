from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BrandfetchCredentials

class BrandfetchFontToolInput(BaseModel):
    image_types: Optional[str] = Field(None, description="imageTypes")
    image_formats: Optional[str] = Field(None, description="imageFormats")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name of the company")


class BrandfetchFontTool(BaseTool):
    name: str = "brandfetch_font"
    description: str = "Tool for Brandfetch font operation - font operation"
    args_schema: type[BaseModel] | None = BrandfetchFontToolInput
    credentials: Optional[BrandfetchCredentials] = None
