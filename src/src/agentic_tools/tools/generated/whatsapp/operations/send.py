from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WhatsappSendToolInput(BaseModel):
    mediaId: Optional[str] = Field(None, description="ID of the media to be sent")
    latitude: Optional[float] = Field(None, description="Latitude")
    messageType: Optional[str] = Field(None, description="The type of the message")
    recipientPhoneNumber: Optional[str] = Field(None, description="Phone number of the recipient of the message")
    mediaPath: Optional[str] = Field(None, description="Use a link, an ID, or n8n to upload an audio file")
    operation: Optional[str] = Field(None, description="Operation")
    messagingProduct: Optional[str] = Field(None, description="Messaging Product")
    name: Optional[Dict[str, Any]] = Field(None, description="Name")
    longitude: Optional[float] = Field(None, description="Longitude")
    mediaFilename: Optional[str] = Field(None, description="The name of the file (required when using a file ID)")
    textBody: Optional[str] = Field(None, description="The body of the message (max 4096 characters)")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    mediaLink: Optional[str] = Field(None, description="Link of the media to be sent")
    mediaPropertyName: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded")
    phoneNumberId: Optional[str] = Field(None, description="The ID of the business account's phone number from which the message will be sent from")


class WhatsappSendTool(BaseTool):
    name = "whatsapp_send"
    description = "Tool for whatsApp send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the whatsApp send operation."""
        # Implement the tool logic here
        return f"Running whatsApp send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the whatsApp send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
