from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BrandfetchCredentials

class BrandfetchColorToolInput(BaseModel):
    image_types: Optional[str] = Field(None, description="imageTypes")
    image_formats: Optional[str] = Field(None, description="imageFormats")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name of the company")


class BrandfetchColorTool(BaseTool):
    name: str = "brandfetch_color"
    connector_id: str = "nodes-base.Brandfetch"
    description: str = "Tool for Brandfetch color operation - color operation"
    args_schema: type[BaseModel] | None = BrandfetchColorToolInput
    credentials: Optional[BrandfetchCredentials] = None
