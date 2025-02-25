# compression operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all compression operation tools."""
    tools = []
    from .compress import CompressionCompressTool
    tools.append(CompressionCompressTool())
    from .decompress import CompressionDecompressTool
    tools.append(CompressionDecompressTool())
    return tools
