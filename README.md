# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

AutoGen is a framework that enables development of LLM applications using multiple agents that can converse with each other to solve task. AutoGen agents are customizable, conversable, and seamlessly allow human participation. They can operate in various modes that employ combinations of LLMs, human inputs, and tools.

![AutoGen Overview](./img/autogen_agentchat.png)

* AutoGen enables building next-gen LLM applications based on **multi-agent conversations** with minimal effort. It simplifies the orchestration, automation and optimization of a complex LLM workflow. It maximizes the performance of LLM models and overcome their weaknesses.
* It supports **diverse conversation patterns** for complex workflows. With customizable and conversable agents, developers can use AutoGen to build a wide range of conversation patterns concerning conversation autonomy,
the number of agents, and agent conversation topology.
* It provides a collection of working systems with different complexities. These systems span a **wide range of applications** from various domains and complexities. They demonstrate how AutoGen can easily support different conversation patterns.
* AutoGen provides a drop-in replacement of `openai.Completion` or `openai.ChatCompletion` as an **enhanced inference API**. It allows easy performance tuning, utilities like API unification & caching, and advanced usage patterns, such as error handling, multi-config inference, context programming etc.


## Installation

AutoGen requires **Python version >= 3.8**. Install AutoGen locally via:

```bash
pip install -e .
```

Minimal dependencies are installed without extra options. You can install extra options based on the feature you need.
For example, use the following to install the dependencies needed by the [`retrievechat`] option for the Retrieval Augmented Chat application.
```bash
pip install -e .[retrievechat]
```


## Quickstart

* Autogen enables the next-gen LLM applications with a generic multi-agent conversation framework. It offers customizable and conversable agents which integrate LLMs, tools and human.
By automating chat among multiple capable agents, one can easily make them collectively perform tasks autonomously or with human feedback, including tasks that require using tools via code. For example,
```python
from autogen import AssistantAgent, UserProxyAgent
assistant = AssistantAgent("assistant")
user_proxy = UserProxyAgent("user_proxy")
user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock price change YTD.")
# This initiates an automated chat between the two agents to solve the task
```

The figure below shows an example conversation flow with AutoGen.
![Agent Chat Example](./img/chat_example.png)

# Applications

- [A1: Math Problem Solving](./application/A1-math/README.md)

- [A2: Retrieval Augmented QA](./application/A2-retrieval-augmented-chat/README.md)

- [A3: Decision Making in Household Tasks](./application/A3-decision-making-ALFWorld/README.md)

- [A4: Supply-Chain Optimization](./application/A4-supply-chain-optimization/README.md)

- [A5: Dynamic Task Solving with Group Chat](./application/A5-dynamic-task-solving/README.md)

- [A6: Conversational Chess](./application/A6-conversational-chess/README.md)

- [A7: Decision Making for Browser Interactions](./application/A7-decision-making-MiniWob++/README.md)
