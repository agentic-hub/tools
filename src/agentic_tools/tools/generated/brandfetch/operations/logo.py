from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BrandfetchCredentials

class BrandfetchLogoToolInput(BaseModel):
    image_types: Optional[str] = Field(None, description="imageTypes")
    download: Optional[bool] = Field(None, description="Name of the binary property to which to write the data of the read file")
    image_formats: Optional[str] = Field(None, description="imageFormats")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name of the company")


class BrandfetchLogoTool(BaseTool):
    name: str = "brandfetch_logo"
    description: str = "Tool for Brandfetch logo operation - logo operation"
    args_schema: type[BaseModel] | None = BrandfetchLogoToolInput
    credentials: Optional[BrandfetchCredentials] = None
