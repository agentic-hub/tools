from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwselbCredentials

class AwselbGetmanyToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    certificate_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    load_balancer_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    listener_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subnets: Optional[str] = Field(None, description="subnets")
    operation: Optional[str] = Field(None, description="Operation")


class AwselbGetmanyTool(BaseTool):
    name: str = "awselb_getmany"
    description: str = "Tool for awsElb getMany operation - getMany operation"
    args_schema: type[BaseModel] | None = AwselbGetmanyToolInput
    credentials: Optional[AwselbCredentials] = None
