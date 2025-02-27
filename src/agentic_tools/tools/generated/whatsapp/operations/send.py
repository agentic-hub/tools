from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WhatsappCredentials

class WhatsappSendToolInput(BaseModel):
    media_id: Optional[str] = Field(None, description="ID of the media to be sent")
    latitude: Optional[float] = Field(None, description="Latitude")
    message_type: Optional[str] = Field(None, description="The type of the message")
    recipient_phone_number: Optional[str] = Field(None, description="Phone number of the recipient of the message")
    media_path: Optional[str] = Field(None, description="Use a link, an ID, or n8n to upload an audio file")
    operation: Optional[str] = Field(None, description="Operation")
    messaging_product: Optional[str] = Field(None, description="Messaging Product")
    name: Optional[Dict[str, Any]] = Field(None, description="Name")
    longitude: Optional[float] = Field(None, description="Longitude")
    media_filename: Optional[str] = Field(None, description="The name of the file (required when using a file ID)")
    text_body: Optional[str] = Field(None, description="The body of the message (max 4096 characters)")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    media_link: Optional[str] = Field(None, description="Link of the media to be sent")
    media_property_name: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded")
    phone_number_id: Optional[str] = Field(None, description="The ID of the business account's phone number from which the message will be sent from")


class WhatsappSendTool(BaseTool):
    name: str = "whatsapp_send"
    description: str = "Tool for whatsApp send operation - send operation"
    args_schema: type[BaseModel] | None = WhatsappSendToolInput
    credentials: Optional[WhatsappCredentials] = None
