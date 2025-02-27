from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MatrixCredentials

class MatrixKickToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    reason: Optional[str] = Field(None, description="Reason for kick")
    user_id: Optional[str] = Field(None, description="The fully qualified user ID")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixKickTool(BaseTool):
    name: str = "matrix_kick"
    description: str = "Tool for matrix kick operation - kick operation"
    args_schema: type[BaseModel] | None = MatrixKickToolInput
    credentials: Optional[MatrixCredentials] = None
