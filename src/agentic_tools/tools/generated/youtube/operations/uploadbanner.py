from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import YoutubeCredentials

class YoutubeUploadbannerToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    video_id: Optional[str] = Field(None, description="Video ID")
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


class YoutubeUploadbannerTool(BaseTool):
    name: str = "youtube_uploadbanner"
    connector_id: str = "nodes-base.youTube"
    description: str = "Tool for youTube uploadBanner operation - uploadBanner operation"
    args_schema: type[BaseModel] | None = YoutubeUploadbannerToolInput
    credentials: Optional[YoutubeCredentials] = None
