from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WebhookDefaultToolInput(BaseModel):
    responseData: Optional[str] = Field(None, description="What data should be returned. If it should return all items as an array or only the first item as object.")
    httpMethod: Optional[str] = Field(None, description="The HTTP method to listen to")
    webhookNotice: Optional[str] = Field(None, description="Insert a 'Respond to Webhook' node to control when and how you respond. <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/\" target=\"_blank\">More details</a>")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="The way to authenticate")
    responseMode: Optional[str] = Field(None, description="When and how to respond to the webhook")
    responseBinaryPropertyName: Optional[str] = Field(None, description="Name of the binary property to return")
    responseCode: Optional[float] = Field(None, description="The HTTP Response code to return")
    path: Optional[str] = Field(None, description="The path to listen to")


class WebhookDefaultTool(BaseTool):
    name = "webhook_default"
    description = "Tool for webhook default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the webhook default operation."""
        # Implement the tool logic here
        return f"Running webhook default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the webhook default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
