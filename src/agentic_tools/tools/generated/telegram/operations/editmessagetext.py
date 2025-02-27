from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TelegramCredentials

class TelegramEditmessagetextToolInput(BaseModel):
    reply_keyboard_options: Optional[Dict[str, Any]] = Field(None, description="Reply Keyboard Options")
    inline_keyboard: Optional[Dict[str, Any]] = Field(None, description="Adds an inline keyboard that appears right next to the message it belongs to")
    reply_markup: Optional[str] = Field(None, description="Additional interface options")
    reply_keyboard: Optional[Dict[str, Any]] = Field(None, description="Adds a custom keyboard with reply options")
    message_type: Optional[str] = Field(None, description="The type of the message to edit")
    text: Optional[str] = Field(None, description="Text of the message to be sent")
    inline_message_id: Optional[str] = Field(None, description="Unique identifier of the inline message to edit")
    file: Optional[str] = Field(None, description="Animation to send. Pass a file_id to send an animation that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get an animation from the Internet.")
    operation: Optional[str] = Field(None, description="Operation")
    reply_keyboard_remove: Optional[Dict[str, Any]] = Field(None, description="Reply Keyboard Remove")
    query_id: Optional[str] = Field(None, description="Unique identifier for the query to be answered")
    chat_id: Optional[str] = Field(None, description="Unique identifier for the target chat or username of the target channel (in the format @channelusername). To find your chat ID ask @get_id_bot.")
    message_id: Optional[str] = Field(None, description="Unique identifier of the message to edit")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    force_reply: Optional[Dict[str, Any]] = Field(None, description="Force Reply")


class TelegramEditmessagetextTool(BaseTool):
    name: str = "telegram_editmessagetext"
    description: str = "Tool for telegram editMessageText operation - editMessageText operation"
    args_schema: type[BaseModel] | None = TelegramEditmessagetextToolInput
    credentials: Optional[TelegramCredentials] = None
