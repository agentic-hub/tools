from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PushoverCredentials

class PushoverPushToolInput(BaseModel):
    user_key: Optional[str] = Field(None, description="The user/group key (not e-mail address) of your user (or you), viewable when logged into the <a href=\"https://pushover.net/\">dashboard</a> (often referred to as <code>USER_KEY</code> in the <a href=\"https://support.pushover.net/i44-example-code-and-pushover-libraries\">libraries</a> and code examples)")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    priority: Optional[str] = Field(None, description="Send as -2 to generate no notification/alert, -1 to always send as a quiet notification, 1 to display as high-priority and bypass the user's quiet hours, or 2 to also require confirmation from the user")
    expire: Optional[float] = Field(None, description="Specifies how many seconds your notification will continue to be retried for (every retry seconds)")
    message: Optional[str] = Field(None, description="Your message")
    operation: Optional[str] = Field(None, description="Operation")
    retry: Optional[float] = Field(None, description="Specifies how often (in seconds) the Pushover servers will send the same notification to the user. This parameter must have a value of at least 30 seconds between retries.")


class PushoverPushTool(BaseTool):
    name: str = "pushover_push"
    connector_id: str = "nodes-base.pushover"
    description: str = "Tool for pushover push operation - push operation"
    args_schema: type[BaseModel] | None = PushoverPushToolInput
    credentials: Optional[PushoverCredentials] = None
