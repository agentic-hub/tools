from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FacebookgraphapiCredentials(BaseModel):
    """Credentials for facebookGraphApi authentication."""
    facebook_graph_api: Optional[Dict[str, Any]] = Field(None, description="facebookGraphApi")

class FacebookgraphapiDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FacebookgraphapiCredentials] = Field(None, description="Custom credentials for authentication")
    send_binary_data: Optional[bool] = Field(None, description="Whether binary data should be sent as body")
    graph_api_version: Optional[str] = Field(None, description="The version of the Graph API to be used in the request")
    binary_property_name: Optional[str] = Field(None, description="For Form-Data Multipart, they can be provided in the format: <code>\"sendKey1:binaryProperty1,sendKey2:binaryProperty2</code>")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    http_request_method: Optional[str] = Field(None, description="The HTTP Method to be used for the request")
    edge: Optional[str] = Field(None, description="Edge of the node on which to operate. Edges represent collections of objects which are attached to the node.")
    node: Optional[str] = Field(None, description="The node on which to operate. A node is an individual object with a unique ID. For example, there are many User node objects, each with a unique ID representing a person on Facebook.")
    host_url: Optional[str] = Field(None, description="The Host URL of the request. Almost all requests are passed to the graph.facebook.com host URL. The single exception is video uploads, which use graph-video.facebook.com.")
    allow_unauthorized_certs: Optional[bool] = Field(None, description="Whether to connect even if SSL certificate validation is not possible")


class FacebookgraphapiDefaultTool(BaseTool):
    name = "facebookgraphapi_default"
    description = "Tool for facebookGraphApi default operation - default operation"
    
    def __init__(self, credentials: Optional[FacebookgraphapiCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the facebookGraphApi default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running facebookGraphApi default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running facebookGraphApi default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the facebookGraphApi default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
