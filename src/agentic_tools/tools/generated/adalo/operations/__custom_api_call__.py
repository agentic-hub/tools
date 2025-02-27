from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AdaloCredentials

class Adalo__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    collection_id: Optional[str] = Field(None, description="Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation")
    operation: Optional[str] = Field(None, description="Operation")


class Adalo__custom_api_call__Tool(BaseTool):
    name: str = "adalo___custom_api_call__"
    description: str = "Tool for adalo __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Adalo__custom_api_call__ToolInput
    credentials: Optional[AdaloCredentials] = None
