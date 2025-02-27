from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TelegramCredentials

class TelegramAnswerqueryToolInput(BaseModel):
    reply_keyboard_options: Optional[Dict[str, Any]] = Field(None, description="Reply Keyboard Options")
    inline_keyboard: Optional[Dict[str, Any]] = Field(None, description="Adds an inline keyboard that appears right next to the message it belongs to")
    reply_markup: Optional[str] = Field(None, description="Additional interface options")
    reply_keyboard: Optional[Dict[str, Any]] = Field(None, description="Adds a custom keyboard with reply options")
    file: Optional[str] = Field(None, description="Animation to send. Pass a file_id to send an animation that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get an animation from the Internet.")
    operation: Optional[str] = Field(None, description="Operation")
    reply_keyboard_remove: Optional[Dict[str, Any]] = Field(None, description="Reply Keyboard Remove")
    query_id: Optional[str] = Field(None, description="Unique identifier for the query to be answered")
    chat_id: Optional[str] = Field(None, description="Unique identifier for the target chat or username of the target channel (in the format @channelusername)")
    message_id: Optional[str] = Field(None, description="Unique identifier of the message to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    force_reply: Optional[Dict[str, Any]] = Field(None, description="Force Reply")


class TelegramAnswerqueryTool(BaseTool):
    name: str = "telegram_answerquery"
    description: str = "Tool for telegram answerQuery operation - answerQuery operation"
    args_schema: type[BaseModel] | None = TelegramAnswerqueryToolInput
    credentials: Optional[TelegramCredentials] = None
