from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Discord__custom_api_call__ToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the message (up to 2000 characters)")
    files: Optional[Dict[str, Any]] = Field(None, description="Files")
    role: Optional[str] = Field(None, description="role")
    channelId: Optional[Dict[str, Any]] = Field(None, description="Select the channel by name, URL, or ID")
    guildId: Optional[Dict[str, Any]] = Field(None, description="Select the server (guild) that your bot is connected to")
    userId: Optional[Dict[str, Any]] = Field(None, description="Select the user you want to assign a role to")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    embeds: Optional[Dict[str, Any]] = Field(None, description="Embeds")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the channel")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    messageId: Optional[str] = Field(None, description="The ID of the message")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Connection Type")


class Discord__custom_api_call__Tool(BaseTool):
    name = "discord___custom_api_call__"
    description = "Tool for discord __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the discord __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running discord __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the discord __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
