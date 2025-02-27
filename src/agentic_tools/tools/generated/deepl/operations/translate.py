from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DeeplCredentials

class DeeplTranslateToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    translate_to: Optional[str] = Field(None, description="Language to translate to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    text: Optional[str] = Field(None, description="Input text to translate")
    operation: Optional[str] = Field(None, description="Operation")


class DeeplTranslateTool(BaseTool):
    name: str = "deepl_translate"
    connector_id: str = "nodes-base.deepL"
    description: str = "Tool for deepL translate operation - translate operation"
    args_schema: type[BaseModel] | None = DeeplTranslateToolInput
    credentials: Optional[DeeplCredentials] = None
