from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LonescaleCredentials

class Lonescale__custom_api_call__ToolInput(BaseModel):
    list: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Create a new list")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type of your list")


class Lonescale__custom_api_call__Tool(BaseTool):
    name: str = "lonescale___custom_api_call__"
    description: str = "Tool for loneScale __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Lonescale__custom_api_call__ToolInput
    credentials: Optional[LonescaleCredentials] = None
