from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogletranslateCredentials

class GoogletranslateTranslateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    translate_to: Optional[str] = Field(None, description="The language to use for translation of the input text, set to one of the language codes listed in <a href=\"https://cloud.google.com/translate/docs/languages\">Language Support</a>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="Authentication")
    text: Optional[str] = Field(None, description="The input text to translate")
    operation: Optional[str] = Field(None, description="Operation")


class GoogletranslateTranslateTool(BaseTool):
    name: str = "googletranslate_translate"
    connector_id: str = "nodes-base.googleTranslate"
    description: str = "Tool for googleTranslate translate operation - translate operation"
    args_schema: type[BaseModel] | None = GoogletranslateTranslateToolInput
    credentials: Optional[GoogletranslateCredentials] = None
