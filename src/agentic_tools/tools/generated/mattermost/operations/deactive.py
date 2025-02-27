from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MattermostCredentials

class MattermostDeactiveToolInput(BaseModel):
    post_id: Optional[str] = Field(None, description="ID of the post to delete")
    emoji_name: Optional[str] = Field(None, description="Emoji to use for this reaction")
    team_id: Optional[str] = Field(None, description="The Mattermost Team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    channel_id: Optional[str] = Field(None, description="The ID of the channel to soft delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    user_id: Optional[str] = Field(None, description="User GUID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    message: Optional[str] = Field(None, description="The text to send")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class MattermostDeactiveTool(BaseTool):
    name: str = "mattermost_deactive"
    description: str = "Tool for mattermost deactive operation - deactive operation"
    args_schema: type[BaseModel] | None = MattermostDeactiveToolInput
    credentials: Optional[MattermostCredentials] = None
