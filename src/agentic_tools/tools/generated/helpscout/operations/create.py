from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HelpscoutCredentials

class HelpscoutCreateToolInput(BaseModel):
    mailbox_id: Optional[str] = Field(None, description="ID of a mailbox where the conversation is being created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    customer_id: Optional[str] = Field(None, description="Customer ID")
    emails_ui: Optional[Dict[str, Any]] = Field(None, description="Emails")
    text: Optional[str] = Field(None, description="The chat text")
    type: Optional[str] = Field(None, description="Conversation type")
    resolve_data: Optional[bool] = Field(None, description="By default the response only contain the ID to resource. If this option gets activated, it will resolve the data automatically.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    social_profiles_ui: Optional[Dict[str, Any]] = Field(None, description="Social Profiles")
    websites_ui: Optional[Dict[str, Any]] = Field(None, description="Websites")
    subject: Optional[str] = Field(None, description="Conversation’s subject")
    address_ui: Optional[Dict[str, Any]] = Field(None, description="Address")
    operation: Optional[str] = Field(None, description="Operation")
    phones_ui: Optional[Dict[str, Any]] = Field(None, description="Phones")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    conversation_id: Optional[str] = Field(None, description="Conversation ID")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Conversation status")
    attachments_ui: Optional[Dict[str, Any]] = Field(None, description="Array of supported attachments to add to the message")
    threads_ui: Optional[Dict[str, Any]] = Field(None, description="Threads")
    chats_ui: Optional[Dict[str, Any]] = Field(None, description="Chat Handles")


class HelpscoutCreateTool(BaseTool):
    name: str = "helpscout_create"
    description: str = "Tool for helpScout create operation - create operation"
    args_schema: type[BaseModel] | None = HelpscoutCreateToolInput
    credentials: Optional[HelpscoutCredentials] = None
