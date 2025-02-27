from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MatrixCredentials

class MatrixLeaveToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    user_id: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixLeaveTool(BaseTool):
    name: str = "matrix_leave"
    connector_id: str = "nodes-base.matrix"
    description: str = "Tool for matrix leave operation - leave operation"
    args_schema: type[BaseModel] | None = MatrixLeaveToolInput
    credentials: Optional[MatrixCredentials] = None
