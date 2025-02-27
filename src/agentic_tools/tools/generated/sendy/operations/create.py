from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendyCredentials

class SendyCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    list_id: Optional[str] = Field(None, description="The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID.")
    email: Optional[str] = Field(None, description="Email address of the subscriber")
    send_campaign: Optional[bool] = Field(None, description="Whether to send the campaign as well and not just create a draft. Default is false.")
    title: Optional[str] = Field(None, description="The 'Title' of your campaign")
    subject: Optional[str] = Field(None, description="The 'Subject' of your campaign")
    html_text: Optional[str] = Field(None, description="The 'HTML version' of your campaign")
    brand_id: Optional[str] = Field(None, description="Brand ID")
    reply_to: Optional[str] = Field(None, description="The 'Reply to' of your campaign")
    from_name: Optional[str] = Field(None, description="The 'From name' of your campaign")
    from_email: Optional[str] = Field(None, description="The 'From email' of your campaign")
    operation: Optional[str] = Field(None, description="Operation")


class SendyCreateTool(BaseTool):
    name: str = "sendy_create"
    description: str = "Tool for sendy create operation - create operation"
    args_schema: type[BaseModel] | None = SendyCreateToolInput
    credentials: Optional[SendyCredentials] = None
