from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MatrixCredentials

class MatrixJoinToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="The room related to the event")
    user_id: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")
    room_id_or_alias: Optional[str] = Field(None, description="Room ID or Alias")


class MatrixJoinTool(BaseTool):
    name: str = "matrix_join"
    description: str = "Tool for matrix join operation - join operation"
    args_schema: type[BaseModel] | None = MatrixJoinToolInput
    credentials: Optional[MatrixCredentials] = None
