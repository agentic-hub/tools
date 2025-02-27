from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WebhookCredentials

class WebhookDefaultToolInput(BaseModel):
    response_data: Optional[str] = Field(None, description="What data should be returned. If it should return all items as an array or only the first item as object.")
    http_method: Optional[str] = Field(None, description="The HTTP method to listen to")
    webhook_notice: Optional[str] = Field(None, description="Insert a 'Respond to Webhook' node to control when and how you respond. <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/\" target=\"_blank\">More details</a>")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="The way to authenticate")
    response_mode: Optional[str] = Field(None, description="When and how to respond to the webhook")
    response_binary_property_name: Optional[str] = Field(None, description="Name of the binary property to return")
    response_code: Optional[float] = Field(None, description="The HTTP Response code to return")
    path: Optional[str] = Field(None, description="The path to listen to")


class WebhookDefaultTool(BaseTool):
    name: str = "webhook_default"
    description: str = "Tool for webhook default operation - default operation"
    args_schema: type[BaseModel] | None = WebhookDefaultToolInput
    credentials: Optional[WebhookCredentials] = None
