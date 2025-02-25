from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WaitDefaultToolInput(BaseModel):
    webhookNotice: Optional[str] = Field(None, description="The webhook URL will be generated at run time. It can be referenced with the <strong>$execution.resumeUrl</strong> variable. Send it somewhere before getting to this node. <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.wait\" target=\"_blank\">More info</a>")
    formFields: Optional[Dict[str, Any]] = Field(None, description="Form Fields")
    limitWaitTime: Optional[bool] = Field(None, description="Whether the workflow will automatically resume execution after the specified limit type")
    resumeUnit: Optional[str] = Field(None, description="Unit of the interval value")
    responseData: Optional[str] = Field(None, description="What data should be returned. If it should return all items as an array or only the first item as object.")
    limitType: Optional[str] = Field(None, description="Sets the condition for the execution to resume. Can be a specified date or after some time.")
    formNotice: Optional[str] = Field(None, description="The form url will be generated at run time. It can be referenced with the <strong>$execution.resumeFormUrl</strong> variable. Send it somewhere before getting to this node. <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.wait\" target=\"_blank\">More info</a>")
    resumeAmount: Optional[float] = Field(None, description="The time to wait")
    unit: Optional[str] = Field(None, description="The time unit of the Wait Amount value")
    dateTime: Optional[str] = Field(None, description="The date and time to wait for before continuing")
    resume: Optional[str] = Field(None, description="Determines the waiting mode to use before the workflow continues")
    httpMethod: Optional[str] = Field(None, description="The HTTP method of the Webhook call")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    responseMode: Optional[str] = Field(None, description="When to respond to the form submission")
    formTitle: Optional[str] = Field(None, description="Shown at the top of the form")
    formDescription: Optional[str] = Field(None, description="Shown underneath the Form Title. Can be used to prompt the user on how to complete the form.")
    incomingAuthentication: Optional[str] = Field(None, description="If and how incoming resume-webhook-requests to $execution.resumeUrl should be authenticated for additional security")
    amount: Optional[float] = Field(None, description="The time to wait")
    responseBinaryPropertyName: Optional[str] = Field(None, description="Name of the binary property to return")
    maxDateAndTime: Optional[str] = Field(None, description="Continue execution after the specified date and time")
    responseCode: Optional[float] = Field(None, description="The HTTP Response code to return")


class WaitDefaultTool(BaseTool):
    name = "wait_default"
    description = "Tool for wait default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the wait default operation."""
        # Implement the tool logic here
        return f"Running wait default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the wait default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
