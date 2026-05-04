import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm(model_name="gemini-3.1-flash-lite-preview", temperature=0):
    """
    Initializes and returns a Gemini model.
    Using gemini-3.1-flash-lite-preview as requested.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set.")
    
    return ChatGoogleGenerativeAI(
        model=model_name, 
        temperature=temperature, 
        google_api_key=api_key
    )

if __name__ == "__main__":
    try:
        llm = get_llm()
        print(f"Successfully initialized {llm.model}")
    except Exception as e:
        print(f"Initialization failed: {e}")
