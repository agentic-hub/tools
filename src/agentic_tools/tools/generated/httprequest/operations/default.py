from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HttprequestDefaultToolInput(BaseModel):
    node_credential_type: Optional[str] = Field(None, description="nodeCredentialType")
    curl_import: Optional[str] = Field(None, description="curlImport")
    specify_body: Optional[str] = Field(None, description="The body can be specified using explicit fields (<code>keypair</code>) or using a JavaScript object (<code>json</code>)")
    specify_headers: Optional[str] = Field(None, description="Specify Headers")
    input_data_field_name: Optional[str] = Field(None, description="The name of the incoming field containing the binary file data to be processed")
    send_headers: Optional[bool] = Field(None, description="Whether the request has headers or not")
    body_parameters: Optional[Dict[str, Any]] = Field(None, description="Body Parameters")
    specify_query: Optional[str] = Field(None, description="Specify Query Parameters")
    send_query: Optional[bool] = Field(None, description="Whether the request has query params or not")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    url: Optional[str] = Field(None, description="The URL to make the request to")
    body: Optional[str] = Field(None, description="Body")
    info_message: Optional[str] = Field(None, description="You can view the raw requests this node makes in your browser's developer console")
    raw_content_type: Optional[str] = Field(None, description="Content Type")
    send_body: Optional[bool] = Field(None, description="Whether the request has a body or not")
    json_body: Optional[str] = Field(None, description="JSON")
    json_query: Optional[str] = Field(None, description="JSON")
    content_type: Optional[str] = Field(None, description="Content-Type to use to send body parameters")
    json_headers: Optional[str] = Field(None, description="JSON")
    google_api_warning: Optional[str] = Field(None, description="Make sure you have specified the scope(s) for the Service Account in the credential")
    method: Optional[str] = Field(None, description="The request method to use")
    query_parameters: Optional[Dict[str, Any]] = Field(None, description="Query Parameters")
    authentication: Optional[str] = Field(None, description="Authentication")
    header_parameters: Optional[Dict[str, Any]] = Field(None, description="Header Parameters")
    generic_auth_type: Optional[str] = Field(None, description="genericAuthType")


class HttprequestDefaultTool(BaseTool):
    name = "httprequest_default"
    description = "Tool for httpRequest default operation - default operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the httpRequest default operation."""
        # Implement the tool logic here
        return f"Running httpRequest default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the httpRequest default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
