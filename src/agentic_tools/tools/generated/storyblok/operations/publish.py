from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StoryblokCredentials

class StoryblokPublishToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Management API")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    space: Optional[str] = Field(None, description="The name of the space. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    story_id: Optional[str] = Field(None, description="Numeric ID of the story")
    operation: Optional[str] = Field(None, description="Operation")


class StoryblokPublishTool(BaseTool):
    name: str = "storyblok_publish"
    connector_id: str = "nodes-base.storyblok"
    description: str = "Tool for storyblok publish operation - publish operation"
    args_schema: type[BaseModel] | None = StoryblokPublishToolInput
    credentials: Optional[StoryblokCredentials] = None
