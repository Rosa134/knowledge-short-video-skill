# AI Explainer Patterns

Use this reference for AI concept videos.

## Default Structure

```text
Hook -> Mental Model -> Mechanism -> Use Cases -> Limitations -> Takeaway
```

## Common Visual Templates

| Topic | Best Visual |
|---|---|
| RAG | query -> retrieve -> rerank -> generate -> verify flow |
| Agent | goal -> plan -> tool call -> observe -> revise loop |
| MCP | app, tool server, model, permission boundaries |
| Context engineering | input budget, memory, retrieval, compression layers |
| Evaluation | dataset, rubric, judge, regression dashboard |
| Multimodal | text, image, audio streams into model |
| Workflow automation | trigger, branch, tool, human approval, log |

## Accuracy Rules

- Prefer official docs, papers, repository README, or vendor documentation for current AI facts.
- Separate "what the system does" from "why teams use it".
- Include at least one limitation or failure mode.
- Do not imply autonomy, reliability, or safety that the system does not have.
- For current model capabilities, verify externally before making specific claims.

## Example Takeaways

- "RAG 的核心不是存知识，而是在回答前供应可信上下文。"
- "Agent 的关键不是会聊天，而是能在反馈里改下一步动作。"
- "MCP 把工具接入从一次性集成，变成可复用的协议边界。"
