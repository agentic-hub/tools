from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LonescaleCredentials

class LonescaleCreateToolInput(BaseModel):
    list: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    name: Optional[str] = Field(None, description="Name of your list")
    resource: Optional[str] = Field(None, description="Create a new list")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type of your list")


class LonescaleCreateTool(BaseTool):
    name: str = "lonescale_create"
    connector_id: str = "nodes-base.loneScale"
    description: str = "Tool for loneScale create operation - create operation"
    args_schema: type[BaseModel] | None = LonescaleCreateToolInput
    credentials: Optional[LonescaleCredentials] = None
