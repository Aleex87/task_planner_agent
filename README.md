# Task Planner Agent

## Setup Instructions

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd task_planner_agent
```

---

### 2. Install dependencies

This project uses **uv** for environment and dependency management.

Make sure you have uv installed, then run:

```bash
uv sync
```

This will install all required dependencies in a virtual environment.

---

### 3. Run the project

```bash
uv run python main.py
```

---

## What the Project Does

The **Task Planner Agent** helps users transform vague goals into clear, structured, and actionable plans.

The agent can:

* Break down a goal into smaller steps
* Organize tasks logically
* Suggest next actions
* Answer follow-up questions directly
* Maintain conversational context using memory

---

## Project Structure

```
task_planner_agent/
│
├── main.py          # Entry point of the application
├── agent.py         # Agent logic and orchestration
├── prompts.py       # System prompt (agent behavior)
├── tools.py         # Custom tools (task creation & prioritization)
├── memory.py        # Conversation memory handling
│
└── util/            # Provided utilities (DO NOT MODIFY)
    ├── models.py
    ├── streaming_utils.py
    ├── pretty_print.py
    ├── tools.py
    └── embeddings.py
```

---

## Key Concepts

* **Prompt Engineering**
  The agent behavior is controlled through a structured system prompt.

* **Tool Usage**
  The agent can use tools to generate and organize task lists.

* **Conversational Memory**
  Previous interactions are stored to maintain context.

* **Streaming Output**
  Responses are streamed in real-time with styled output:

  * Agent responses (blue)
  * Tool calls (yellow)
  * Tool results (green)

---

## Usage

Start the program and enter a goal:

```text
I want to build a Python project
```

The agent will generate a structured plan.

You can also ask follow-up questions:

```text
Why should I use exceptions?
```

The agent will respond directly without creating a new plan.

To exit the program, type:

```text
exit
```

---

## Notes

* The `util/` folder contains pre-built components and must not be modified.
* The agent is designed to remain simple, clear, and aligned with the course level.
* Tool usage is controlled through prompt design to ensure appropriate behavior.

---

## Author

Alessandro Abbate

