from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TelegramCredentials(BaseModel):
    """Credentials for telegram authentication."""
    telegram_api: Optional[Dict[str, Any]] = Field(None, description="telegramApi")

class TelegramSendchatactionToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TelegramCredentials] = Field(None, description="Custom credentials for authentication")
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
    action: Optional[str] = Field(None, description="Type of action to broadcast. Choose one, depending on what the user is about to receive. The status is set for 5 seconds or less (when a message arrives from your bot).")
    force_reply: Optional[Dict[str, Any]] = Field(None, description="Force Reply")


class TelegramSendchatactionTool(BaseTool):
    name = "telegram_sendchataction"
    description = "Tool for telegram sendChatAction operation - sendChatAction operation"
    
    def __init__(self, credentials: Optional[TelegramCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the telegram sendChatAction operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running telegram sendChatAction operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running telegram sendChatAction operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the telegram sendChatAction operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
