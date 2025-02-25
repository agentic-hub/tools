from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ElasticsecurityCredentials(BaseModel):
    """Credentials for elasticSecurity authentication."""
    elastic_security_api: Optional[Dict[str, Any]] = Field(None, description="elasticSecurityApi")

class ElasticsecurityDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ElasticsecurityCredentials] = Field(None, description="Custom credentials for authentication")
    comment_id: Optional[str] = Field(None, description="ID of the case comment to retrieve")
    tag: Optional[str] = Field(None, description="Tag to attach to the case. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    case_id: Optional[str] = Field(None, description="Case ID")
    connector_type: Optional[str] = Field(None, description="Connector Type")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    comment: Optional[str] = Field(None, description="Comment")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class ElasticsecurityDeleteTool(BaseTool):
    name = "elasticsecurity_delete"
    description = "Tool for elasticSecurity delete operation - delete operation"
    
    def __init__(self, credentials: Optional[ElasticsecurityCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the elasticSecurity delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running elasticSecurity delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running elasticSecurity delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the elasticSecurity delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
