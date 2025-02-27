from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DiscordCredentials

class DiscordGetallToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the message (up to 2000 characters)")
    files: Optional[Dict[str, Any]] = Field(None, description="Files")
    role: Optional[str] = Field(None, description="role")
    channel_id: Optional[Dict[str, Any]] = Field(None, description="Select the channel by name, URL, or ID")
    guild_id: Optional[Dict[str, Any]] = Field(None, description="Select the server (guild) that your bot is connected to")
    user_id: Optional[Dict[str, Any]] = Field(None, description="Select the user you want to assign a role to")
    after: Optional[str] = Field(None, description="The ID of the user after which to return the members")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    embeds: Optional[Dict[str, Any]] = Field(None, description="Embeds")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the channel")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message_id: Optional[str] = Field(None, description="The ID of the message")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Connection Type")


class DiscordGetallTool(BaseTool):
    name: str = "discord_getall"
    description: str = "Tool for discord getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = DiscordGetallToolInput
    credentials: Optional[DiscordCredentials] = None
