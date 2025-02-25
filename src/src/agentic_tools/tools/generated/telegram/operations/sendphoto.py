from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TelegramSendphotoToolInput(BaseModel):
    replyKeyboardOptions: Optional[Dict[str, Any]] = Field(None, description="Reply Keyboard Options")
    inlineKeyboard: Optional[Dict[str, Any]] = Field(None, description="Adds an inline keyboard that appears right next to the message it belongs to")
    replyMarkup: Optional[str] = Field(None, description="Additional interface options")
    replyKeyboard: Optional[Dict[str, Any]] = Field(None, description="Adds a custom keyboard with reply options")
    binaryPropertyName: Optional[str] = Field(None, description="Name of the binary property that contains the data to upload")
    file: Optional[str] = Field(None, description="Photo to send. Pass a file_id to send a photo that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get a photo from the Internet.")
    binaryData: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    operation: Optional[str] = Field(None, description="Operation")
    replyKeyboardRemove: Optional[Dict[str, Any]] = Field(None, description="Reply Keyboard Remove")
    queryId: Optional[str] = Field(None, description="Unique identifier for the query to be answered")
    chatId: Optional[str] = Field(None, description="Unique identifier for the target chat or username of the target channel (in the format @channelusername)")
    messageId: Optional[str] = Field(None, description="Unique identifier of the message to delete")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    forceReply: Optional[Dict[str, Any]] = Field(None, description="Force Reply")


class TelegramSendphotoTool(BaseTool):
    name = "telegram_sendphoto"
    description = "Tool for telegram sendPhoto operation - sendPhoto operation"
    
    def _run(self, **kwargs):
        """Run the telegram sendPhoto operation."""
        # Implement the tool logic here
        return f"Running telegram sendPhoto operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the telegram sendPhoto operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
