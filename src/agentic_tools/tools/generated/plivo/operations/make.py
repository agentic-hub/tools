from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PlivoCredentials

class PlivoMakeToolInput(BaseModel):
    to: Optional[str] = Field(None, description="Phone number to make the call to")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="Message to send")
    answer_url: Optional[str] = Field(None, description="URL to be invoked by Plivo once the call is answered. It should return the XML to handle the call once answered.")
    answer_method: Optional[str] = Field(None, description="HTTP verb to be used when invoking the Answer URL")
    from: Optional[str] = Field(None, description="Caller ID for the call to make")
    operation: Optional[str] = Field(None, description="Operation")


class PlivoMakeTool(BaseTool):
    name: str = "plivo_make"
    description: str = "Tool for plivo make operation - make operation"
    args_schema: type[BaseModel] | None = PlivoMakeToolInput
    credentials: Optional[PlivoCredentials] = None
