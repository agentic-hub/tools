from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BannerbearCredentials

class BannerbearGetallToolInput(BaseModel):
    template_id: Optional[str] = Field(None, description="The template ID you want to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class BannerbearGetallTool(BaseTool):
    name: str = "bannerbear_getall"
    connector_id: str = "nodes-base.bannerbear"
    description: str = "Tool for bannerbear getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = BannerbearGetallToolInput
    credentials: Optional[BannerbearCredentials] = None
