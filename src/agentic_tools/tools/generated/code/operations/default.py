from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CodeDefaultToolInput(BaseModel):
    language: Optional[str] = Field(None, description="Language")
    python_code: Optional[str] = Field(None, description="Python code to execute.<br><br>Tip: You can use built-in methods and variables like <code>_today</code> for dates and <code>_jmespath</code> for querying JSON structures. <a href=\"https://docs.n8n.io/code/builtin/\">Learn more</a>.")
    notice: Optional[str] = Field(None, description="Type <code>$</code> for a list of <a target=\"_blank\" href=\"https://docs.n8n.io/code-examples/methods-variables-reference/\">special vars/methods</a>. Debug by using <code>console.log()</code> statements and viewing their output in the browser console.")
    mode: Optional[str] = Field(None, description="Mode")
    js_code: Optional[str] = Field(None, description="JavaScript code to execute.<br><br>Tip: You can use luxon vars like <code>$today</code> for dates and <code>$jmespath</code> for querying JSON structures. <a href=\"https://docs.n8n.io/nodes/n8n-nodes-base.function\">Learn more</a>.")


class CodeDefaultTool(BaseTool):
    name: str = "code_default"
    description: str = "Tool for code default operation - default operation"
    args_schema: type[BaseModel] | None = CodeDefaultToolInput
