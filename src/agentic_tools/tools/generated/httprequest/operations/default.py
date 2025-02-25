from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HttprequestDefaultToolInput(BaseModel):
    nodeCredentialType: Optional[str] = Field(None, description="nodeCredentialType")
    curlImport: Optional[str] = Field(None, description="curlImport")
    specifyBody: Optional[str] = Field(None, description="The body can be specified using explicit fields (<code>keypair</code>) or using a JavaScript object (<code>json</code>)")
    specifyHeaders: Optional[str] = Field(None, description="Specify Headers")
    inputDataFieldName: Optional[str] = Field(None, description="The name of the incoming field containing the binary file data to be processed")
    sendHeaders: Optional[bool] = Field(None, description="Whether the request has headers or not")
    bodyParameters: Optional[Dict[str, Any]] = Field(None, description="Body Parameters")
    specifyQuery: Optional[str] = Field(None, description="Specify Query Parameters")
    sendQuery: Optional[bool] = Field(None, description="Whether the request has query params or not")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    url: Optional[str] = Field(None, description="The URL to make the request to")
    body: Optional[str] = Field(None, description="Body")
    infoMessage: Optional[str] = Field(None, description="You can view the raw requests this node makes in your browser's developer console")
    rawContentType: Optional[str] = Field(None, description="Content Type")
    sendBody: Optional[bool] = Field(None, description="Whether the request has a body or not")
    jsonBody: Optional[str] = Field(None, description="JSON")
    jsonQuery: Optional[str] = Field(None, description="JSON")
    contentType: Optional[str] = Field(None, description="Content-Type to use to send body parameters")
    jsonHeaders: Optional[str] = Field(None, description="JSON")
    googleApiWarning: Optional[str] = Field(None, description="Make sure you have specified the scope(s) for the Service Account in the credential")
    method: Optional[str] = Field(None, description="The request method to use")
    queryParameters: Optional[Dict[str, Any]] = Field(None, description="Query Parameters")
    authentication: Optional[str] = Field(None, description="Authentication")
    headerParameters: Optional[Dict[str, Any]] = Field(None, description="Header Parameters")
    genericAuthType: Optional[str] = Field(None, description="genericAuthType")


class HttprequestDefaultTool(BaseTool):
    name = "httprequest_default"
    description = "Tool for httpRequest default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the httpRequest default operation."""
        # Implement the tool logic here
        return f"Running httpRequest default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the httpRequest default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
