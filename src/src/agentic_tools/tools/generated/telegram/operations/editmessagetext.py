from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TelegramEditmessagetextToolInput(BaseModel):
    replyKeyboardOptions: Optional[Dict[str, Any]] = Field(None, description="Reply Keyboard Options")
    inlineKeyboard: Optional[Dict[str, Any]] = Field(None, description="Adds an inline keyboard that appears right next to the message it belongs to")
    replyMarkup: Optional[str] = Field(None, description="Additional interface options")
    replyKeyboard: Optional[Dict[str, Any]] = Field(None, description="Adds a custom keyboard with reply options")
    messageType: Optional[str] = Field(None, description="The type of the message to edit")
    text: Optional[str] = Field(None, description="Text of the message to be sent")
    inlineMessageId: Optional[str] = Field(None, description="Unique identifier of the inline message to edit")
    file: Optional[str] = Field(None, description="Animation to send. Pass a file_id to send an animation that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get an animation from the Internet.")
    operation: Optional[str] = Field(None, description="Operation")
    replyKeyboardRemove: Optional[Dict[str, Any]] = Field(None, description="Reply Keyboard Remove")
    queryId: Optional[str] = Field(None, description="Unique identifier for the query to be answered")
    chatId: Optional[str] = Field(None, description="Unique identifier for the target chat or username of the target channel (in the format @channelusername). To find your chat ID ask @get_id_bot.")
    messageId: Optional[str] = Field(None, description="Unique identifier of the message to edit")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    forceReply: Optional[Dict[str, Any]] = Field(None, description="Force Reply")


class TelegramEditmessagetextTool(BaseTool):
    name = "telegram_editmessagetext"
    description = "Tool for telegram editMessageText operation - editMessageText operation"
    
    def _run(self, **kwargs):
        """Run the telegram editMessageText operation."""
        # Implement the tool logic here
        return f"Running telegram editMessageText operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the telegram editMessageText operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
