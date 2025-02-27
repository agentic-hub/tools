from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AmqpCredentials

class AmqpDefaultToolInput(BaseModel):
    sink: Optional[str] = Field(None, description="Name of the queue of topic to publish to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    header_parameters_json: Optional[str] = Field(None, description="Header parameters as JSON (flat object). Sent as application_properties in amqp-message meta info.")


class AmqpDefaultTool(BaseTool):
    name: str = "amqp_default"
    connector_id: str = "nodes-base.amqp"
    description: str = "Tool for amqp default operation - default operation"
    args_schema: type[BaseModel] | None = AmqpDefaultToolInput
    credentials: Optional[AmqpCredentials] = None
