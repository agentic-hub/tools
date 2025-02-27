from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KafkaCredentials

class KafkaDefaultToolInput(BaseModel):
    use_key: Optional[bool] = Field(None, description="Whether to use a message key")
    event_name: Optional[str] = Field(None, description="Namespace and Name of Schema in Schema Registry (namespace.name)")
    header_parameters_json: Optional[str] = Field(None, description="Header parameters as JSON (flat object)")
    message: Optional[str] = Field(None, description="The message to be sent")
    send_input_data: Optional[bool] = Field(None, description="Whether to send the the data the node receives as JSON to Kafka")
    schema_registry_url: Optional[str] = Field(None, description="URL of the schema registry")
    headers_ui: Optional[Dict[str, Any]] = Field(None, description="Headers")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    use_schema_registry: Optional[bool] = Field(None, description="Whether to use Confluent Schema Registry")
    topic: Optional[str] = Field(None, description="Name of the queue of topic to publish to")
    key: Optional[str] = Field(None, description="The message key")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class KafkaDefaultTool(BaseTool):
    name: str = "kafka_default"
    connector_id: str = "nodes-base.kafka"
    description: str = "Tool for kafka default operation - default operation"
    args_schema: type[BaseModel] | None = KafkaDefaultToolInput
    credentials: Optional[KafkaCredentials] = None
