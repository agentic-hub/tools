from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwselbCredentials

class AwselbCreateToolInput(BaseModel):
    schema: Optional[str] = Field(None, description="Schema")
    name: Optional[str] = Field(None, description="This name must be unique per region per account, can have a maximum of 32 characters")
    certificate_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    load_balancer_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer")
    listener_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subnets: Optional[str] = Field(None, description="subnets")
    ip_address_type: Optional[str] = Field(None, description="The type of IP addresses used by the subnets for your load balancer")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class AwselbCreateTool(BaseTool):
    name: str = "awselb_create"
    connector_id: str = "nodes-base.awsElb"
    description: str = "Tool for awsElb create operation - create operation"
    args_schema: type[BaseModel] | None = AwselbCreateToolInput
    credentials: Optional[AwselbCredentials] = None
