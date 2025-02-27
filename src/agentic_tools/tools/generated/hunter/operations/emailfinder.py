from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HunterCredentials

class HunterEmailfinderToolInput(BaseModel):
    lastname: Optional[str] = Field(None, description="The person's last name. It doesn't need to be in lowercase.")
    firstname: Optional[str] = Field(None, description="The person's first name. It doesn't need to be in lowercase.")
    operation: Optional[str] = Field(None, description="Operation to consume")
    domain: Optional[str] = Field(None, description="Domain name from which you want to find the email addresses. For example, \"stripe.com\".")


class HunterEmailfinderTool(BaseTool):
    name: str = "hunter_emailfinder"
    description: str = "Tool for hunter emailFinder operation - emailFinder operation"
    args_schema: type[BaseModel] | None = HunterEmailfinderToolInput
    credentials: Optional[HunterCredentials] = None
