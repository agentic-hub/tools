from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GraphqlCredentials(BaseModel):
    """Credentials for graphql authentication."""
    http_basic_auth: Optional[Dict[str, Any]] = Field(None, description="httpBasicAuth")
    http_custom_auth: Optional[Dict[str, Any]] = Field(None, description="httpCustomAuth")
    http_digest_auth: Optional[Dict[str, Any]] = Field(None, description="httpDigestAuth")
    http_header_auth: Optional[Dict[str, Any]] = Field(None, description="httpHeaderAuth")
    http_query_auth: Optional[Dict[str, Any]] = Field(None, description="httpQueryAuth")
    o_auth1_api: Optional[Dict[str, Any]] = Field(None, description="oAuth1Api")
    o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="oAuth2Api")

class GraphqlDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GraphqlCredentials] = Field(None, description="Custom credentials for authentication")
    variables: Optional[str] = Field(None, description="Query variables")
    header_parameters_ui: Optional[Dict[str, Any]] = Field(None, description="The headers to send")
    request_method: Optional[str] = Field(None, description="The underlying HTTP request method to use")
    endpoint: Optional[str] = Field(None, description="The GraphQL endpoint")
    request_format: Optional[str] = Field(None, description="The format for the query payload")
    operation_name: Optional[str] = Field(None, description="Name of operation to execute")
    authentication: Optional[str] = Field(None, description="The way to authenticate")
    query: Optional[str] = Field(None, description="GraphQL query")
    allow_unauthorized_certs: Optional[bool] = Field(None, description="Whether to download the response even if SSL certificate validation is not possible")
    data_property_name: Optional[str] = Field(None, description="Name of the property to which to write the response data")
    response_format: Optional[str] = Field(None, description="The format in which the data gets returned from the URL")


class GraphqlDefaultTool(BaseTool):
    name = "graphql_default"
    description = "Tool for graphql default operation - default operation"
    
    def __init__(self, credentials: Optional[GraphqlCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the graphql default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running graphql default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running graphql default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the graphql default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
