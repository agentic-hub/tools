from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendinblueCredentials

class SendinblueSendtemplateToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    template_id: Optional[str] = Field(None, description="Template ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueSendtemplateTool(BaseTool):
    name: str = "sendinblue_sendtemplate"
    description: str = "Tool for sendInBlue sendTemplate operation - sendTemplate operation"
    args_schema: type[BaseModel] | None = SendinblueSendtemplateToolInput
    credentials: Optional[SendinblueCredentials] = None
