from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LingvanexCredentials

class LingvanexTranslateToolInput(BaseModel):
    translate_to: Optional[str] = Field(None, description="The language to use for translation of the input text, set to one of the language codes listed in <a href=\"https://cloud.google.com/translate/docs/languages\">Language Support</a>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    text: Optional[str] = Field(None, description="The input text to translate")
    operation: Optional[str] = Field(None, description="Operation")


class LingvanexTranslateTool(BaseTool):
    name: str = "lingvanex_translate"
    connector_id: str = "nodes-base.lingvaNex"
    description: str = "Tool for lingvaNex translate operation - translate operation"
    args_schema: type[BaseModel] | None = LingvanexTranslateToolInput
    credentials: Optional[LingvanexCredentials] = None
