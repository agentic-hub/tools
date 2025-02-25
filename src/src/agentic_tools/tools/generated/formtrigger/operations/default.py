from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FormtriggerDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    formNotice: Optional[str] = Field(None, description="In the 'Respond to Webhook' node, select 'Respond With JSON' and set the <strong>formSubmittedText</strong> key to display a custom response in the form, or the <strong>redirectURL</strong> key to redirect users to a URL")
    responseMode: Optional[str] = Field(None, description="When to respond to the form submission")
    formDescription: Optional[str] = Field(None, description="Shown underneath the Form Title. Can be used to prompt the user on how to complete the form.")
    formFields: Optional[Dict[str, Any]] = Field(None, description="Form Fields")
    formTitle: Optional[str] = Field(None, description="Shown at the top of the form")
    path: Optional[str] = Field(None, description="The final segment of the form's URL, both for test and production")


class FormtriggerDefaultTool(BaseTool):
    name = "formtrigger_default"
    description = "Tool for formTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the formTrigger default operation."""
        # Implement the tool logic here
        return f"Running formTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the formTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
