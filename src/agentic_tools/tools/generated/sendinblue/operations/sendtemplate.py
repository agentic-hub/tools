from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendinblueSendtemplateToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    templateId: Optional[str] = Field(None, description="Template ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueSendtemplateTool(BaseTool):
    name = "sendinblue_sendtemplate"
    description = "Tool for sendInBlue sendTemplate operation - sendTemplate operation"
    
    def _run(self, **kwargs):
        """Run the sendInBlue sendTemplate operation."""
        # Implement the tool logic here
        return f"Running sendInBlue sendTemplate operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendInBlue sendTemplate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
