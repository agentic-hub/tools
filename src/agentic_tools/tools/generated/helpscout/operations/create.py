from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HelpscoutCreateToolInput(BaseModel):
    mailboxId: Optional[str] = Field(None, description="ID of a mailbox where the conversation is being created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    customerId: Optional[str] = Field(None, description="Customer ID")
    emailsUi: Optional[Dict[str, Any]] = Field(None, description="Emails")
    text: Optional[str] = Field(None, description="The chat text")
    type: Optional[str] = Field(None, description="Conversation type")
    resolveData: Optional[bool] = Field(None, description="By default the response only contain the ID to resource. If this option gets activated, it will resolve the data automatically.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    socialProfilesUi: Optional[Dict[str, Any]] = Field(None, description="Social Profiles")
    websitesUi: Optional[Dict[str, Any]] = Field(None, description="Websites")
    subject: Optional[str] = Field(None, description="Conversation’s subject")
    addressUi: Optional[Dict[str, Any]] = Field(None, description="Address")
    operation: Optional[str] = Field(None, description="Operation")
    phonesUi: Optional[Dict[str, Any]] = Field(None, description="Phones")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    conversationId: Optional[str] = Field(None, description="Conversation ID")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Conversation status")
    attachmentsUi: Optional[Dict[str, Any]] = Field(None, description="Array of supported attachments to add to the message")
    threadsUi: Optional[Dict[str, Any]] = Field(None, description="Threads")
    chatsUi: Optional[Dict[str, Any]] = Field(None, description="Chat Handles")


class HelpscoutCreateTool(BaseTool):
    name = "helpscout_create"
    description = "Tool for helpScout create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the helpScout create operation."""
        # Implement the tool logic here
        return f"Running helpScout create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the helpScout create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
