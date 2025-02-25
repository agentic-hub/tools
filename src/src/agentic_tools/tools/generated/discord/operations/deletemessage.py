from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DiscordDeletemessageToolInput(BaseModel):
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


class DiscordDeletemessageTool(BaseTool):
    name = "discord_deletemessage"
    description = "Tool for discord deleteMessage operation - deleteMessage operation"
    
    def _run(self, **kwargs):
        """Run the discord deleteMessage operation."""
        # Implement the tool logic here
        return f"Running discord deleteMessage operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the discord deleteMessage operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
