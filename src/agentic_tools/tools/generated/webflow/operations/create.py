from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WebflowCredentials(BaseModel):
    """Credentials for webflow authentication."""
    webflow_api: Optional[Dict[str, Any]] = Field(None, description="webflowApi")
    webflow_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="webflowOAuth2Api")

class WebflowCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[WebflowCredentials] = Field(None, description="Custom credentials for authentication")
    live: Optional[bool] = Field(None, description="Whether the item should be published on the live site")
    item_id: Optional[str] = Field(None, description="ID of the item to operate on")
    resource: Optional[str] = Field(None, description="Resource")
    site_id: Optional[str] = Field(None, description="ID of the site containing the collection whose items to add to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="Authentication")
    collection_id: Optional[str] = Field(None, description="ID of the collection to add an item to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields")


class WebflowCreateTool(BaseTool):
    name = "webflow_create"
    description = "Tool for webflow create operation - create operation"
    
    def __init__(self, credentials: Optional[WebflowCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the webflow create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running webflow create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running webflow create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the webflow create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
