from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StoryblokGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Management API")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    space: Optional[str] = Field(None, description="The name of the space. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    storyId: Optional[str] = Field(None, description="Numeric ID of the story")
    operation: Optional[str] = Field(None, description="Operation")


class StoryblokGetallTool(BaseTool):
    name = "storyblok_getall"
    description = "Tool for storyblok getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the storyblok getAll operation."""
        # Implement the tool logic here
        return f"Running storyblok getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the storyblok getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
