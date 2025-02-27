from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CortexCredentials

class CortexExecuteToolInput(BaseModel):
    json_object: Optional[bool] = Field(None, description="Choose between providing JSON object or seperated attributes")
    object_data: Optional[str] = Field(None, description="Entity Object (JSON)")
    resource: Optional[str] = Field(None, description="Choose a resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    observable_value: Optional[str] = Field(None, description="Enter the observable value")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    entity_type: Optional[str] = Field(None, description="Choose the Data type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    responder: Optional[str] = Field(None, description="Choose the responder. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    analyzer: Optional[str] = Field(None, description="Choose the analyzer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    observable_type: Optional[str] = Field(None, description="Choose the observable type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Parameters")
    tlp: Optional[str] = Field(None, description="The TLP of the analyzed observable")
    operation: Optional[str] = Field(None, description="Choose an operation")


class CortexExecuteTool(BaseTool):
    name: str = "cortex_execute"
    connector_id: str = "nodes-base.cortex"
    description: str = "Tool for cortex execute operation - execute operation"
    args_schema: type[BaseModel] | None = CortexExecuteToolInput
    credentials: Optional[CortexCredentials] = None
