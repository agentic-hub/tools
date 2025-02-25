from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SpotifyPrevioussongToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The artist's Spotify URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class SpotifyPrevioussongTool(BaseTool):
    name = "spotify_previoussong"
    description = "Tool for spotify previousSong operation - previousSong operation"
    
    def _run(self, **kwargs):
        """Run the spotify previousSong operation."""
        # Implement the tool logic here
        return f"Running spotify previousSong operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the spotify previousSong operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
