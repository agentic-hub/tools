from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MediumCredentials(BaseModel):
    """Credentials for medium authentication."""
    medium_api: Optional[Dict[str, Any]] = Field(None, description="mediumApi")
    medium_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="mediumOAuth2Api")

class MediumCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MediumCredentials] = Field(None, description="Custom credentials for authentication")
    publication: Optional[bool] = Field(None, description="Whether you are posting for a publication")
    content: Optional[str] = Field(None, description="The body of the post, in a valid semantic HTML fragment, or Markdown")
    resource: Optional[str] = Field(None, description="Resource")
    publication_id: Optional[str] = Field(None, description="Publication IDs. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="Title of the post. Max Length : 100 characters.")
    content_format: Optional[str] = Field(None, description="The format of the content to be posted")
    operation: Optional[str] = Field(None, description="Operation")


class MediumCreateTool(BaseTool):
    name = "medium_create"
    description = "Tool for medium create operation - create operation"
    
    def __init__(self, credentials: Optional[MediumCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the medium create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running medium create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running medium create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the medium create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
