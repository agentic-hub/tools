from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BrandfetchCredentials

class BrandfetchCompanyToolInput(BaseModel):
    image_types: Optional[str] = Field(None, description="imageTypes")
    image_formats: Optional[str] = Field(None, description="imageFormats")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name of the company")


class BrandfetchCompanyTool(BaseTool):
    name: str = "brandfetch_company"
    connector_id: str = "nodes-base.Brandfetch"
    description: str = "Tool for Brandfetch company operation - company operation"
    args_schema: type[BaseModel] | None = BrandfetchCompanyToolInput
    credentials: Optional[BrandfetchCredentials] = None
