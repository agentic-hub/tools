from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HtmlGeneratehtmltemplateToolInput(BaseModel):
    html: Optional[str] = Field(None, description="HTML template to render")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    notice: Optional[str] = Field(None, description="<b>Tips</b>: Type ctrl+space for completions. Use <code>{{ }}</code> for expressions and <code>&lt;style&gt;</code> tags for CSS. JS in <code>&lt;script&gt;</code> tags is included but not executed in n8n.")
    extraction_values: Optional[Dict[str, Any]] = Field(None, description="Extraction Values")
    operation: Optional[str] = Field(None, description="Operation")
    data_property_name: Optional[str] = Field(None, description="Input Binary Field")


class HtmlGeneratehtmltemplateTool(BaseTool):
    name: str = "html_generatehtmltemplate"
    description: str = "Tool for html generateHtmlTemplate operation - generateHtmlTemplate operation"
    args_schema: type[BaseModel] | None = HtmlGeneratehtmltemplateToolInput
