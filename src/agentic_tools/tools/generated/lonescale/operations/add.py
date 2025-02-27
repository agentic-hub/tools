from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LonescaleCredentials

class LonescaleAddToolInput(BaseModel):
    list: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    company_additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    company_name: Optional[str] = Field(None, description="Contact company name")
    resource: Optional[str] = Field(None, description="Create a new list")
    people_additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    last_name: Optional[str] = Field(None, description="Contact last name")
    first_name: Optional[str] = Field(None, description="Contact first name")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type of your list")


class LonescaleAddTool(BaseTool):
    name: str = "lonescale_add"
    connector_id: str = "nodes-base.loneScale"
    description: str = "Tool for loneScale add operation - add operation"
    args_schema: type[BaseModel] | None = LonescaleAddToolInput
    credentials: Optional[LonescaleCredentials] = None
