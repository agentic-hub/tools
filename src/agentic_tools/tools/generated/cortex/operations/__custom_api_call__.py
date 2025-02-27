from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CortexCredentials

class Cortex__custom_api_call__ToolInput(BaseModel):
    json_object: Optional[bool] = Field(None, description="Choose between providing JSON object or seperated attributes")
    object_data: Optional[str] = Field(None, description="Entity Object (JSON)")
    resource: Optional[str] = Field(None, description="Choose a resource")
    entity_type: Optional[str] = Field(None, description="Choose the Data type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    responder: Optional[str] = Field(None, description="Choose the responder. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Parameters")
    operation: Optional[str] = Field(None, description="Choose an operation")


class Cortex__custom_api_call__Tool(BaseTool):
    name: str = "cortex___custom_api_call__"
    description: str = "Tool for cortex __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Cortex__custom_api_call__ToolInput
    credentials: Optional[CortexCredentials] = None
