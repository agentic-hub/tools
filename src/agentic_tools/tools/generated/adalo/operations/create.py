from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AdaloCredentials

class AdaloCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    data_to_send: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    collection_id: Optional[str] = Field(None, description="Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation")
    operation: Optional[str] = Field(None, description="Operation")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Field must be defined in the collection, otherwise it will be ignored. If field defined in the collection is not set here, it will be set to null.")


class AdaloCreateTool(BaseTool):
    name: str = "adalo_create"
    description: str = "Tool for adalo create operation - create operation"
    args_schema: type[BaseModel] | None = AdaloCreateToolInput
    credentials: Optional[AdaloCredentials] = None
