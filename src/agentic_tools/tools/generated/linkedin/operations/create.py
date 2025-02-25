from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LinkedinCredentials(BaseModel):
    """Credentials for linkedIn authentication."""
    linked_in_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="linkedInOAuth2Api")
    linked_in_community_management_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="linkedInCommunityManagementOAuth2Api")

class LinkedinCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[LinkedinCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    organization: Optional[str] = Field(None, description="URN of Organization as which the post should be posted as")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    person: Optional[str] = Field(None, description="Person as which the post should be posted as. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="Authentication")
    post_as: Optional[str] = Field(None, description="If to post on behalf of a user or an organization")
    text: Optional[str] = Field(None, description="The primary content of the post")
    share_media_category: Optional[str] = Field(None, description="Media Category")
    operation: Optional[str] = Field(None, description="Operation")


class LinkedinCreateTool(BaseTool):
    name = "linkedin_create"
    description = "Tool for linkedIn create operation - create operation"
    
    def __init__(self, credentials: Optional[LinkedinCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the linkedIn create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running linkedIn create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running linkedIn create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the linkedIn create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
