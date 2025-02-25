from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WhatsappMediadeleteToolInput(BaseModel):
    mediaDeleteId: Optional[str] = Field(None, description="The ID of the media")
    recipientPhoneNumber: Optional[str] = Field(None, description="Phone number of the recipient of the message")
    mediaPath: Optional[str] = Field(None, description="Use a link, an ID, or n8n to upload an audio file")
    operation: Optional[str] = Field(None, description="Operation")
    messagingProduct: Optional[str] = Field(None, description="Messaging Product")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    mediaPropertyName: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded")
    phoneNumberId: Optional[str] = Field(None, description="The ID of the business account's phone number from which the message will be sent from")


class WhatsappMediadeleteTool(BaseTool):
    name = "whatsapp_mediadelete"
    description = "Tool for whatsApp mediaDelete operation - mediaDelete operation"
    
    def _run(self, **kwargs):
        """Run the whatsApp mediaDelete operation."""
        # Implement the tool logic here
        return f"Running whatsApp mediaDelete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the whatsApp mediaDelete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
