from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MatrixCredentials

class MatrixMeToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="The room related to the event")
    user_id: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixMeTool(BaseTool):
    name: str = "matrix_me"
    description: str = "Tool for matrix me operation - me operation"
    args_schema: type[BaseModel] | None = MatrixMeToolInput
    credentials: Optional[MatrixCredentials] = None
