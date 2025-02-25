from langchain.tools import BaseTool


class BaseTool(BaseTool):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def run(self, **kwargs):
        pass
