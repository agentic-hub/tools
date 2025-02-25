from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StoryblokCredentials(BaseModel):
    """Credentials for storyblok authentication."""
    storyblok_content_api: Optional[Dict[str, Any]] = Field(None, description="storyblokContentApi")
    storyblok_management_api: Optional[Dict[str, Any]] = Field(None, description="storyblokManagementApi")

class StoryblokUnpublishToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[StoryblokCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Management API")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    space: Optional[str] = Field(None, description="The name of the space. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    story_id: Optional[str] = Field(None, description="Numeric ID of the story")
    operation: Optional[str] = Field(None, description="Operation")


class StoryblokUnpublishTool(BaseTool):
    name = "storyblok_unpublish"
    description = "Tool for storyblok unpublish operation - unpublish operation"
    
    def __init__(self, credentials: Optional[StoryblokCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the storyblok unpublish operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running storyblok unpublish operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running storyblok unpublish operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the storyblok unpublish operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
