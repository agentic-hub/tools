from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendyCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    listId: Optional[str] = Field(None, description="The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID.")
    email: Optional[str] = Field(None, description="Email address of the subscriber")
    sendCampaign: Optional[bool] = Field(None, description="Whether to send the campaign as well and not just create a draft. Default is false.")
    title: Optional[str] = Field(None, description="The 'Title' of your campaign")
    subject: Optional[str] = Field(None, description="The 'Subject' of your campaign")
    htmlText: Optional[str] = Field(None, description="The 'HTML version' of your campaign")
    brandId: Optional[str] = Field(None, description="Brand ID")
    replyTo: Optional[str] = Field(None, description="The 'Reply to' of your campaign")
    fromName: Optional[str] = Field(None, description="The 'From name' of your campaign")
    fromEmail: Optional[str] = Field(None, description="The 'From email' of your campaign")
    operation: Optional[str] = Field(None, description="Operation")


class SendyCreateTool(BaseTool):
    name = "sendy_create"
    description = "Tool for sendy create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the sendy create operation."""
        # Implement the tool logic here
        return f"Running sendy create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendy create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
