from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BannerbearCredentials

class BannerbearCreateToolInput(BaseModel):
    template_id: Optional[str] = Field(None, description="The template ID you want to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    modifications_ui: Optional[Dict[str, Any]] = Field(None, description="Modifications")


class BannerbearCreateTool(BaseTool):
    name: str = "bannerbear_create"
    description: str = "Tool for bannerbear create operation - create operation"
    args_schema: type[BaseModel] | None = BannerbearCreateToolInput
    credentials: Optional[BannerbearCredentials] = None
