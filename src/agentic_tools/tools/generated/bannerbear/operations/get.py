from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BannerbearCredentials

class BannerbearGetToolInput(BaseModel):
    template_id: Optional[str] = Field(None, description="Unique identifier for the template")
    image_id: Optional[str] = Field(None, description="Unique identifier for the image")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class BannerbearGetTool(BaseTool):
    name: str = "bannerbear_get"
    connector_id: str = "nodes-base.bannerbear"
    description: str = "Tool for bannerbear get operation - get operation"
    args_schema: type[BaseModel] | None = BannerbearGetToolInput
    credentials: Optional[BannerbearCredentials] = None
