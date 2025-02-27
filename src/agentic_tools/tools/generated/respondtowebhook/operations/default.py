from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RespondtowebhookDefaultToolInput(BaseModel):
    response_body: Optional[str] = Field(None, description="The HTTP response JSON data")
    redirect_url: Optional[str] = Field(None, description="The URL to redirect to")
    response_data_source: Optional[str] = Field(None, description="Response Data Source")
    general_notice: Optional[str] = Field(None, description="Verify that the \"Webhook\" node's \"Respond\" parameter is set to \"Using Respond to Webhook Node\". <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/\" target=\"_blank\">More details")
    webhook_notice: Optional[str] = Field(None, description="When using expressions, note that this node will only run for the first item in the input data")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    input_field_name: Optional[str] = Field(None, description="The name of the node input field with the binary data")
    respond_with: Optional[str] = Field(None, description="The data that should be returned")


class RespondtowebhookDefaultTool(BaseTool):
    name: str = "respondtowebhook_default"
    description: str = "Tool for respondToWebhook default operation - default operation"
    args_schema: type[BaseModel] | None = RespondtowebhookDefaultToolInput
