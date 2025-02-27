from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DiscordCredentials

class DiscordSendToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the message (up to 2000 characters)")
    files: Optional[Dict[str, Any]] = Field(None, description="Files")
    role: Optional[str] = Field(None, description="role")
    channel_id: Optional[Dict[str, Any]] = Field(None, description="Select the channel by name, URL, or ID")
    guild_id: Optional[Dict[str, Any]] = Field(None, description="Select the server (guild) that your bot is connected to")
    user_id: Optional[Dict[str, Any]] = Field(None, description="Select the user you want to assign a role to")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    embeds: Optional[Dict[str, Any]] = Field(None, description="Embeds")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the channel")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    send_to: Optional[str] = Field(None, description="Send message to a channel or DM to a user")
    message_id: Optional[str] = Field(None, description="The ID of the message")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Connection Type")


class DiscordSendTool(BaseTool):
    name: str = "discord_send"
    connector_id: str = "nodes-base.discord"
    description: str = "Tool for discord send operation - send operation"
    args_schema: type[BaseModel] | None = DiscordSendToolInput
    credentials: Optional[DiscordCredentials] = None
