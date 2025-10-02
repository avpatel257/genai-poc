# LangGraph Examples and Tutorials

This folder contains Jupyter notebooks and Python scripts that demonstrate various LangGraph concepts and implementations. LangGraph is a powerful framework for building complex AI workflows using graph-based architecture. Each example builds upon previous concepts, showing progressive complexity from basic graphs to advanced agent systems with memory and human-in-the-loop interactions.

## Notebooks Overview

### 1. Simple Graph (`1_simple_graph.ipynb`)
**What it teaches:**
- Basic LangGraph graph construction with StateGraph
- Creating sequential workflows with nodes and edges
- State management using TypedDict
- Portfolio calculation example with currency conversion

**Key concepts:**
- `StateGraph` initialization and node management
- Sequential edge connections (`START` → `node1` → `node2` → `END`)
- State transformation through function nodes
- Graph visualization with Mermaid diagrams

**Example use case:** A simple portfolio calculator that applies fees and converts USD to INR

### 2. Graph with Conditional Logic (`2_graph_with_condition.ipynb`)
**What it teaches:**
- Implementing conditional branching in graphs
- Dynamic path selection based on state values
- Multiple conversion paths (INR vs EUR)
- Using `add_conditional_edges()` for decision making

**Key concepts:**
- Conditional edge routing
- Decision functions for path selection
- Multiple endpoint nodes
- Literal types for type safety

**Example use case:** Portfolio converter that chooses between INR or EUR conversion based on user preference

### 3. Basic Chatbot (`3_chatbot.ipynb`)
**What it teaches:**
- Building conversational AI with LangGraph
- Message state management using `add_messages`
- Integration with Ollama local models
- Interactive chat loops with persistent state

**Key concepts:**
- Message-based state architecture
- LLM integration with graph nodes
- Interactive conversation handling
- State persistence across interactions

**Example use case:** Simple chatbot that maintains conversation context

### 4. Tool Calling with Ollama (`4_tool_call-ollama.ipynb`)
**What it teaches:**
- Integrating external tools with AI agents
- Function calling capabilities with local models
- Tool binding and conditional execution
- Limitations of local models for tool usage

**Key concepts:**
- `@tool` decorator for function definition
- `bind_tools()` for LLM tool integration
- `ToolNode` and `tools_condition` for automated tool routing
- Tool execution flow management

**Example use case:** Stock price lookup agent (with noted limitations of local models)

### 5. Tool Calling with OpenAI (`4_tool_call-openai.ipynb`)
**What it teaches:**
- Improved tool calling with cloud-based models
- Better reasoning capabilities compared to local models
- Proper tool usage decision making
- Multiple tool interactions in single queries

**Key concepts:**
- OpenAI model integration (`ChatOpenAI`)
- Superior tool calling performance vs local models
- Complex calculation workflows using tools
- Tool result processing

**Example use case:** Advanced stock price calculations and multi-step reasoning

### 6. Advanced Tool Agent (`5_tool_call-_agent-openai.ipynb`)
**What it teaches:**
- Creating more sophisticated agent workflows
- Bidirectional tool-to-chatbot communication
- Enhanced reasoning loops with tool feedback
- Complex multi-step problem solving

**Key concepts:**
- `tools → chatbot` edge for enhanced reasoning
- Iterative tool usage and result processing
- Advanced agent architecture patterns
- Tool result interpretation and follow-up actions

**Example use case:** Intelligent stock trading calculations with complex reasoning

### 7. Memory and Persistence (`6_memory-openai.ipynb`)
**What it teaches:**
- Adding persistent memory to conversational agents
- Thread-based conversation management
- Context preservation across sessions
- Multi-user conversation handling

**Key concepts:**
- `MemorySaver` for state persistence
- Thread configuration for session management
- Cross-conversation context sharing
- Stateful agent interactions

**Example use case:** Multi-threaded stock trading assistant that remembers previous calculations

### 8. Human-in-the-Loop (HITL) (`8_human_in_the_loop_HITL.py`)
**What it teaches:**
- Implementing human approval workflows
- Interactive decision points in agent execution
- Interrupt and resume patterns
- Real-world AI safety and control mechanisms

**Key concepts:**
- `interrupt()` function for human input
- `Command(resume=...)` for continuation
- Approval workflows for critical actions
- Human oversight integration

**Example use case:** Stock purchase system requiring human approval for transactions

## Progressive Learning Path

The notebooks are designed to be followed in order:

1. **Basic Graphs** (1, 2) → Understand core LangGraph concepts
2. **Conversational AI** (3) → Learn message-based interactions  
3. **Tool Integration** (4, 4, 5) → Master function calling and agent capabilities
4. **Advanced Features** (6, 8) → Implement memory and human oversight


### Model Requirements:
- **Ollama** (for notebooks 3, 4): Install and pull `llama3.2`
- **OpenAI API** (for notebooks 4, 5, 6, 8): Set up API key in `.env` file

### Environment Setup:
Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Key Concepts Demonstrated

### Graph Architecture
- **Nodes**: Individual processing units (functions, LLMs, tools)
- **Edges**: Connections between nodes (sequential, conditional)
- **State**: Shared data structure flowing through the graph

### Agent Patterns
- **Simple Agents**: Basic LLM interactions
- **Tool-Using Agents**: Function calling and external integrations
- **Memory Agents**: Persistent conversation and context
- **Human-Supervised Agents**: Interactive approval workflows

### Advanced Features
- **Conditional Routing**: Dynamic path selection based on state
- **Tool Integration**: External function calling and reasoning
- **Memory Management**: Persistent state across sessions
- **Human Oversight**: Interactive decision points and approvals

## Common Use Cases

- **Financial Applications**: Stock price queries, portfolio calculations
- **Conversational AI**: Chatbots with memory and tool access
- **Workflow Automation**: Multi-step processes with human approval
- **Decision Support Systems**: AI-assisted decision making with oversight

## Model Comparison Notes

The notebooks demonstrate important differences between model types:
- **Local Models (Ollama)**: Good for privacy, but limited tool calling accuracy
- **Cloud Models (OpenAI)**: Superior reasoning and tool usage capabilities
- **Hybrid Approaches**: Combine local and cloud models based on needs

