from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MatrixCreateToolInput(BaseModel):
    roomId: Optional[str] = Field(None, description="The channel to send the message to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    messageType: Optional[str] = Field(None, description="The type of message to send")
    text: Optional[str] = Field(None, description="The text to send")
    roomAlias: Optional[str] = Field(None, description="Room Alias")
    userId: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    fallbackText: Optional[str] = Field(None, description="A plain text message to display in case the HTML cannot be rendered by the Matrix client")
    preset: Optional[str] = Field(None, description="Preset")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")
    messageFormat: Optional[str] = Field(None, description="The format of the message's body")
    roomName: Optional[str] = Field(None, description="Room Name")


class MatrixCreateTool(BaseTool):
    name = "matrix_create"
    description = "Tool for matrix create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the matrix create operation."""
        # Implement the tool logic here
        return f"Running matrix create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the matrix create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
