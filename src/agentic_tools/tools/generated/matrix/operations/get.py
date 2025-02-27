from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MatrixCredentials

class MatrixGetToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="The room related to the event")
    user_id: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    operation: Optional[str] = Field(None, description="Operation")
    event_id: Optional[str] = Field(None, description="The room related to the event")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixGetTool(BaseTool):
    name: str = "matrix_get"
    connector_id: str = "nodes-base.matrix"
    description: str = "Tool for matrix get operation - get operation"
    args_schema: type[BaseModel] | None = MatrixGetToolInput
    credentials: Optional[MatrixCredentials] = None
