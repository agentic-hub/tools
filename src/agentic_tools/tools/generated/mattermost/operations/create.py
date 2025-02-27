from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MattermostCredentials

class MattermostCreateToolInput(BaseModel):
    post_id: Optional[str] = Field(None, description="ID of the post to react to. Obtainable from the post link: <code>https://mattermost.internal.n8n.io/[server]/pl/[postId]</code>")
    emoji_name: Optional[str] = Field(None, description="Emoji to use for this reaction")
    team_id: Optional[str] = Field(None, description="The Mattermost Team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    channel: Optional[str] = Field(None, description="The unique handle for the channel, will be present in the channel URL")
    display_name: Optional[str] = Field(None, description="The non-unique UI name for the channel")
    channel_id: Optional[str] = Field(None, description="The ID of the channel to soft delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    auth_service: Optional[str] = Field(None, description="Auth Service")
    auth_data: Optional[str] = Field(None, description="Auth Data")
    type: Optional[str] = Field(None, description="The type of channel to create")
    user_id: Optional[str] = Field(None, description="ID of the user sending the reaction. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    password: Optional[str] = Field(None, description="The password used for email authentication")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    message: Optional[str] = Field(None, description="The text to send")
    username: Optional[str] = Field(None, description="Username")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class MattermostCreateTool(BaseTool):
    name: str = "mattermost_create"
    description: str = "Tool for mattermost create operation - create operation"
    args_schema: type[BaseModel] | None = MattermostCreateToolInput
    credentials: Optional[MattermostCredentials] = None
