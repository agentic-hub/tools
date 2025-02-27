from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MatrixCredentials

class MatrixUploadToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="Room ID to post. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    user_id: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    operation: Optional[str] = Field(None, description="Operation")
    media_type: Optional[str] = Field(None, description="Type of file being uploaded")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class MatrixUploadTool(BaseTool):
    name: str = "matrix_upload"
    description: str = "Tool for matrix upload operation - upload operation"
    args_schema: type[BaseModel] | None = MatrixUploadToolInput
    credentials: Optional[MatrixCredentials] = None
