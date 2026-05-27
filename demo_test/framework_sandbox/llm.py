import os
from dataclasses import dataclass, field
from typing import Optional, List, Dict
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

@dataclass
class OpenAiClient:
    """
    一个用于调用任何兼容OpenAI接口的LLM服务的客户端。
    """
    model: Optional[str] = None
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    timeout: int = None
    client: OpenAI = field(init=False, repr=False)

    def __post_init__(self):
        self.api_key = self.api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = self.base_url or os.getenv("OPENAI_BASE_URL")
        self.model = self.model or os.getenv("OPENAI_MODEL_NAME")
        self.timeout = self.timeout or int(os.getenv("LLM_TIMEOUT", 60))
        if not self.api_key:
            raise ValueError("Missing api_key")

        kwargs = {"api_key": self.api_key}
        if self.base_url:
            kwargs["base_url"] = self.base_url
        if not self.model:
            raise ValueError("Missing model")
        if self.timeout:
            kwargs["timeout"] = self.timeout
        self.client = OpenAI(**kwargs)

    def think(self, messages: List[Dict[str, str]], temperature: float = 0) -> str:
        """
        调用大语言模型进行思考，并返回其响应。
        """
        print(f"🧠 正在调用 {self.model} 模型...")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True,
            )

            # 处理流式响应
            print("✅ 大语言模型响应成功:")
            collected_content = []
            for chunk in response:
                if not chunk.choices:
                    continue
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                collected_content.append(content)
            print()  # 在流式输出结束后换行
            return "".join(collected_content)

        except Exception as e:
            print(f"❌ 调用LLM API时发生错误: {e}")
            return None


# --- 客户端使用示例 ---
if __name__ == '__main__':
    try:
        llmClient = OpenAiClient()

        exampleMessages = [
            {"role": "system", "content": "You are a helpful assistant that writes Python code."},
            {"role": "user", "content": "写一个快速排序算法"}
        ]

        print("--- 调用LLM ---")
        responseText = llmClient.think(exampleMessages)
        if responseText:
            print("\n\n--- 完整模型响应 ---")
            print(responseText)

    except ValueError as e:
        print(e)