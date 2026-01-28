from langchain_aws import ChatBedrock

def get_llm():
    return ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        provider="anthropic",
        region_name="ap-south-1",
        model_kwargs={
            "temperature": 0,
            "max_tokens": 1024
        }
    )
