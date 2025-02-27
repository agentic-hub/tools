from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MarkdownDefaultToolInput(BaseModel):
    html: Optional[str] = Field(None, description="The HTML to be converted to markdown")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    markdown: Optional[str] = Field(None, description="The Markdown to be converted to html")
    destination_key: Optional[str] = Field(None, description="The field to put the output in. Specify nested fields using dots, e.g.\"level1.level2.newKey\".")
    mode: Optional[str] = Field(None, description="Mode")


class MarkdownDefaultTool(BaseTool):
    name: str = "markdown_default"
    connector_id: str = "nodes-base.markdown"
    description: str = "Tool for markdown default operation - default operation"
    args_schema: type[BaseModel] | None = MarkdownDefaultToolInput
