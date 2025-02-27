from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StoryblokCredentials

class StoryblokGetToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Management API")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    identifier: Optional[str] = Field(None, description="The ID or slug of the story to get")
    space: Optional[str] = Field(None, description="The name of the space. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    story_id: Optional[str] = Field(None, description="Numeric ID of the story")
    operation: Optional[str] = Field(None, description="Operation")


class StoryblokGetTool(BaseTool):
    name: str = "storyblok_get"
    connector_id: str = "nodes-base.storyblok"
    description: str = "Tool for storyblok get operation - get operation"
    args_schema: type[BaseModel] | None = StoryblokGetToolInput
    credentials: Optional[StoryblokCredentials] = None
