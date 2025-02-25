from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StoryblokGetToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Management API")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    identifier: Optional[str] = Field(None, description="The ID or slug of the story to get")
    space: Optional[str] = Field(None, description="The name of the space. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    storyId: Optional[str] = Field(None, description="Numeric ID of the story")
    operation: Optional[str] = Field(None, description="Operation")


class StoryblokGetTool(BaseTool):
    name = "storyblok_get"
    description = "Tool for storyblok get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the storyblok get operation."""
        # Implement the tool logic here
        return f"Running storyblok get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the storyblok get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
