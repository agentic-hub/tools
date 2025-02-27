from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WhatsappCredentials

class WhatsappSendtemplateToolInput(BaseModel):
    recipient_phone_number: Optional[str] = Field(None, description="Phone number of the recipient of the message")
    template: Optional[str] = Field(None, description="Name of the template")
    media_path: Optional[str] = Field(None, description="Use a link, an ID, or n8n to upload an audio file")
    operation: Optional[str] = Field(None, description="Operation")
    messaging_product: Optional[str] = Field(None, description="Messaging Product")
    components: Optional[Dict[str, Any]] = Field(None, description="Components")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    media_property_name: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded")
    phone_number_id: Optional[str] = Field(None, description="The ID of the business account's phone number from which the message will be sent from")


class WhatsappSendtemplateTool(BaseTool):
    name: str = "whatsapp_sendtemplate"
    connector_id: str = "nodes-base.whatsApp"
    description: str = "Tool for whatsApp sendTemplate operation - sendTemplate operation"
    args_schema: type[BaseModel] | None = WhatsappSendtemplateToolInput
    credentials: Optional[WhatsappCredentials] = None
