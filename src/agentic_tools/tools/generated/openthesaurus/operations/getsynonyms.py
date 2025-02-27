from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OpenthesaurusGetsynonymsToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    text: Optional[str] = Field(None, description="The word to get synonyms for")
    operation: Optional[str] = Field(None, description="Operation")


class OpenthesaurusGetsynonymsTool(BaseTool):
    name: str = "openthesaurus_getsynonyms"
    description: str = "Tool for openThesaurus getSynonyms operation - getSynonyms operation"
    args_schema: type[BaseModel] | None = OpenthesaurusGetsynonymsToolInput
