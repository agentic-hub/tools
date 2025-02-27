from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WhatsappCredentials

class WhatsappMediauploadToolInput(BaseModel):
    recipient_phone_number: Optional[str] = Field(None, description="Phone number of the recipient of the message")
    media_path: Optional[str] = Field(None, description="Use a link, an ID, or n8n to upload an audio file")
    operation: Optional[str] = Field(None, description="Operation")
    messaging_product: Optional[str] = Field(None, description="Messaging Product")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    media_property_name: Optional[str] = Field(None, description="Name of the binary property which contains the data for the file to be uploaded")
    phone_number_id: Optional[str] = Field(None, description="The ID of the business account's phone number from which the message will be sent from")


class WhatsappMediauploadTool(BaseTool):
    name: str = "whatsapp_mediaupload"
    connector_id: str = "nodes-base.whatsApp"
    description: str = "Tool for whatsApp mediaUpload operation - mediaUpload operation"
    args_schema: type[BaseModel] | None = WhatsappMediauploadToolInput
    credentials: Optional[WhatsappCredentials] = None
