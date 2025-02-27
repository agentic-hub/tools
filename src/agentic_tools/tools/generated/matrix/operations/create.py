from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MatrixCredentials

class MatrixCreateToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="The channel to send the message to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    message_type: Optional[str] = Field(None, description="The type of message to send")
    text: Optional[str] = Field(None, description="The text to send")
    room_alias: Optional[str] = Field(None, description="Room Alias")
    user_id: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    fallback_text: Optional[str] = Field(None, description="A plain text message to display in case the HTML cannot be rendered by the Matrix client")
    preset: Optional[str] = Field(None, description="Preset")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")
    message_format: Optional[str] = Field(None, description="The format of the message's body")
    room_name: Optional[str] = Field(None, description="Room Name")


class MatrixCreateTool(BaseTool):
    name: str = "matrix_create"
    description: str = "Tool for matrix create operation - create operation"
    args_schema: type[BaseModel] | None = MatrixCreateToolInput
    credentials: Optional[MatrixCredentials] = None
