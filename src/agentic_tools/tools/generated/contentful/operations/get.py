from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ContentfulCredentials(BaseModel):
    """Credentials for contentful authentication."""
    contentful_api: Optional[Dict[str, Any]] = Field(None, description="contentfulApi")

class ContentfulGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ContentfulCredentials] = Field(None, description="Custom credentials for authentication")
    source: Optional[str] = Field(None, description="Pick where your data comes from, delivery or preview API")
    content_type_id: Optional[str] = Field(None, description="Content Type ID")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    entry_id: Optional[str] = Field(None, description="Entry ID")
    asset_id: Optional[str] = Field(None, description="Asset ID")
    environment_id: Optional[str] = Field(None, description="The ID for the Contentful environment (e.g. master, staging, etc.). Depending on your plan, you might not have environments. In that case use \"master\".")
    operation: Optional[str] = Field(None, description="Operation")


class ContentfulGetTool(BaseTool):
    name = "contentful_get"
    description = "Tool for contentful get operation - get operation"
    
    def __init__(self, credentials: Optional[ContentfulCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the contentful get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running contentful get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running contentful get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the contentful get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
