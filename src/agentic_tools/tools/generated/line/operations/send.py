from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LineCredentials

class LineSendToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="Message")
    operation: Optional[str] = Field(None, description="Operation")


class LineSendTool(BaseTool):
    name: str = "line_send"
    description: str = "Tool for line send operation - send operation"
    args_schema: type[BaseModel] | None = LineSendToolInput
    credentials: Optional[LineCredentials] = None
