from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WhatsappSendtemplateToolInput(BaseModel):
    recipientPhoneNumber: Optional[str] = Field(None, description="Phone number of the recipient of the message")
    template: Optional[str] = Field(None, description="Name of the template")
    mediaPath: Optional[str] = Field(None, description="Use a link, an ID, or n8n to upload an audio file")
    operation: Optional[str] = Field(None, description="Operation")
    messagingProduct: Optional[str] = Field(None, description="Messaging Product")
    components: Optional[Dict[str, Any]] = Field(None, description="Components")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    mediaPropertyName: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded")
    phoneNumberId: Optional[str] = Field(None, description="The ID of the business account's phone number from which the message will be sent from")


class WhatsappSendtemplateTool(BaseTool):
    name = "whatsapp_sendtemplate"
    description = "Tool for whatsApp sendTemplate operation - sendTemplate operation"
    
    def _run(self, **kwargs):
        """Run the whatsApp sendTemplate operation."""
        # Implement the tool logic here
        return f"Running whatsApp sendTemplate operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the whatsApp sendTemplate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
