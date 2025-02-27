from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import YoutubeCredentials

class YoutubeDeleteToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    video_id: Optional[str] = Field(None, description="ID of the video")
    category_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    channel_id: Optional[str] = Field(None, description="ID of the channel")
    region_code: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property: Optional[str] = Field(None, description="Input Binary Field")
    playlist_id: Optional[str] = Field(None, description="Playlist ID")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    part: Optional[str] = Field(None, description="part")
    playlist_item_id: Optional[str] = Field(None, description="Playlist Item ID")
    title: Optional[str] = Field(None, description="The playlist's title")


class YoutubeDeleteTool(BaseTool):
    name: str = "youtube_delete"
    connector_id: str = "nodes-base.youTube"
    description: str = "Tool for youTube delete operation - delete operation"
    args_schema: type[BaseModel] | None = YoutubeDeleteToolInput
    credentials: Optional[YoutubeCredentials] = None
