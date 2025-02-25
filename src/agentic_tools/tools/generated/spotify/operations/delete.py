from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SpotifyCredentials(BaseModel):
    """Credentials for spotify authentication."""
    spotify_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="spotifyOAuth2Api")

class SpotifyDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SpotifyCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    track_id: Optional[str] = Field(None, description="The track's Spotify URI or its ID. The track to add/delete from the playlist.")
    id: Optional[str] = Field(None, description="The artist's Spotify URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class SpotifyDeleteTool(BaseTool):
    name = "spotify_delete"
    description = "Tool for spotify delete operation - delete operation"
    
    def __init__(self, credentials: Optional[SpotifyCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the spotify delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running spotify delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running spotify delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the spotify delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
