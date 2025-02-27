from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BrandfetchCredentials

class BrandfetchIndustryToolInput(BaseModel):
    image_types: Optional[str] = Field(None, description="imageTypes")
    image_formats: Optional[str] = Field(None, description="imageFormats")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name of the company")


class BrandfetchIndustryTool(BaseTool):
    name: str = "brandfetch_industry"
    description: str = "Tool for Brandfetch industry operation - industry operation"
    args_schema: type[BaseModel] | None = BrandfetchIndustryToolInput
    credentials: Optional[BrandfetchCredentials] = None
