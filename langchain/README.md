# LangChain Examples and Tutorials

This folder contains Jupyter notebooks that demonstrate various LangChain concepts and implementations. Each notebook focuses on specific aspects of working with LangChain, from basic model interactions to advanced routing techniques.

## Notebooks Overview

### 1. Simple Chain (`1_simple_chain.ipynb`)
**What it teaches:**
- Basic LangChain model integration with Ollama
- How to use `ChatOllama` for local language model interactions
- Simple model invocation and response handling
- Setting up a connection to local Ollama models (Gemma3)

**Key concepts:**
- LangChain LLM initialization
- Model invocation using `.invoke()` method
- Working with local AI models through Ollama

### 2. Simple Chain with LiteLLM (`2_simple_chain_with_litellm.ipynb`)
**What it teaches:**
- Advanced model routing using LiteLLM with LangChain
- How to configure multiple model providers in a single application
- Switching between different models (local Ollama models and OpenAI GPT-4)
- Asynchronous model interactions using `.ainvoke()`

**Key concepts:**
- `ChatLiteLLMRouter` configuration and usage
- Model routing with multiple providers (Ollama + OpenAI)
- Setting up model lists with different parameters
- Comparing responses from different models (Gemma3 vs GPT-4o)
- Asynchronous programming with LangChain
- Sentiment analysis example implementation

## Prerequisites

Before running these notebooks, ensure you have:

1. **Ollama installed and running locally** (for notebooks 1 and 2)
   - Install Ollama from [https://ollama.ai](https://ollama.ai)
   - Pull the required models: `ollama pull gemma3` and `ollama pull llama3.2`
   - Ensure Ollama is running on `http://localhost:11434`

2. **OpenAI API Key** (for notebook 2)
   - Set up your OpenAI API key in environment variables
   - Required for GPT-4o model interactions


## Common Use Cases Demonstrated

- **Text Classification**: Sentiment analysis examples
- **Model Comparison**: Comparing outputs from different AI models
- **Local vs Cloud Models**: Working with both local (Ollama) and cloud-based (OpenAI) models
- **Asynchronous Processing**: Using async/await for better performance

