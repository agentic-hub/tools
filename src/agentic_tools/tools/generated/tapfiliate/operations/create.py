from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TapfiliateCredentials

class TapfiliateCreateToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    lastname: Optional[str] = Field(None, description="The affiliate’s lastname")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The affiliate’s email")
    program_id: Optional[str] = Field(None, description="The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    key: Optional[str] = Field(None, description="Name of the metadata key to remove")
    affiliate_id: Optional[str] = Field(None, description="The ID of the affiliate")
    firstname: Optional[str] = Field(None, description="The affiliate’s firstname")
    operation: Optional[str] = Field(None, description="Operation")


class TapfiliateCreateTool(BaseTool):
    name: str = "tapfiliate_create"
    connector_id: str = "nodes-base.tapfiliate"
    description: str = "Tool for tapfiliate create operation - create operation"
    args_schema: type[BaseModel] | None = TapfiliateCreateToolInput
    credentials: Optional[TapfiliateCredentials] = None
