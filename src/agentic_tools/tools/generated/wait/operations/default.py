from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WaitCredentials

class WaitDefaultToolInput(BaseModel):
    webhook_notice: Optional[str] = Field(None, description="The webhook URL will be generated at run time. It can be referenced with the <strong>$execution.resumeUrl</strong> variable. Send it somewhere before getting to this node. <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.wait\" target=\"_blank\">More info</a>")
    form_fields: Optional[Dict[str, Any]] = Field(None, description="Form Fields")
    limit_wait_time: Optional[bool] = Field(None, description="Whether the workflow will automatically resume execution after the specified limit type")
    resume_unit: Optional[str] = Field(None, description="Unit of the interval value")
    response_data: Optional[str] = Field(None, description="What data should be returned. If it should return all items as an array or only the first item as object.")
    limit_type: Optional[str] = Field(None, description="Sets the condition for the execution to resume. Can be a specified date or after some time.")
    form_notice: Optional[str] = Field(None, description="The form url will be generated at run time. It can be referenced with the <strong>$execution.resumeFormUrl</strong> variable. Send it somewhere before getting to this node. <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.wait\" target=\"_blank\">More info</a>")
    resume_amount: Optional[float] = Field(None, description="The time to wait")
    unit: Optional[str] = Field(None, description="The time unit of the Wait Amount value")
    date_time: Optional[str] = Field(None, description="The date and time to wait for before continuing")
    resume: Optional[str] = Field(None, description="Determines the waiting mode to use before the workflow continues")
    http_method: Optional[str] = Field(None, description="The HTTP method of the Webhook call")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    response_mode: Optional[str] = Field(None, description="When to respond to the form submission")
    form_title: Optional[str] = Field(None, description="Shown at the top of the form")
    form_description: Optional[str] = Field(None, description="Shown underneath the Form Title. Can be used to prompt the user on how to complete the form.")
    incoming_authentication: Optional[str] = Field(None, description="If and how incoming resume-webhook-requests to $execution.resumeUrl should be authenticated for additional security")
    amount: Optional[float] = Field(None, description="The time to wait")
    response_binary_property_name: Optional[str] = Field(None, description="Name of the binary property to return")
    max_date_and_time: Optional[str] = Field(None, description="Continue execution after the specified date and time")
    response_code: Optional[float] = Field(None, description="The HTTP Response code to return")


class WaitDefaultTool(BaseTool):
    name: str = "wait_default"
    connector_id: str = "nodes-base.wait"
    description: str = "Tool for wait default operation - default operation"
    args_schema: type[BaseModel] | None = WaitDefaultToolInput
    credentials: Optional[WaitCredentials] = None
