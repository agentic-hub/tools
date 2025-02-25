from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TelegramCredentials(BaseModel):
    """Credentials for telegram authentication."""
    telegram_api: Optional[Dict[str, Any]] = Field(None, description="telegramApi")

class TelegramEditmessagetextToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TelegramCredentials] = Field(None, description="Custom credentials for authentication")
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
    name = "telegram_editmessagetext"
    description = "Tool for telegram editMessageText operation - editMessageText operation"
    
    def __init__(self, credentials: Optional[TelegramCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the telegram editMessageText operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running telegram editMessageText operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running telegram editMessageText operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the telegram editMessageText operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
