
![header Ontbo](https://github.com/user-attachments/assets/780ad7c3-2e95-41a7-8459-7cfdd2ce2504)

  <p align="center"><strong>Make AIs understand your users.</strong></p>
  <p align="center">👉 Cognitive Context API for your AI Agents</p>
  <p align="center">🌐 Homepage:<a href="https://www.ontbo.com">https://www.ontbo.com</a></p>
  <p align="center">🤖 Developper hub:<a href="https://api.ontbo.com">https://api.ontbo.com</a></p>
  <p align="center">📄 Datasheet: <a href="./static/datasheet.pdf">here</a></p>
  <p align="center">Enjoying ONTBO? ⭐️ us to support the project!</p>

  <div>
    <h2> Introduction </h2>

Ontbo API provides a cognitive context layer for AI agents.
It adds long-term memory, persistent context, and reasoning-driven retrieval, enabling AI systems to deliver highly relevant answers and remain consistent over time.
Ontbo API plugs into any LLM stack and helps teams build reliable, scalable AI systems.

 <p> If your assistants hallucinate, token bills spike, and user context lives in 12 different silos – <strong>ONTBO fixes that🔥.</strong></p>
    <p>Plug a <b>cognitive layer</b> in front of your LLMs/Agents and stop duct-taping prompt engineering.<br>
    Your agents become sharper.</p>
    <p><strong>Memory stores. Context understands.</strong></p>
  </div>


  <div>
    <h2>🧩 Main Features</h2>
    <ul>
      <li><strong>Context Layer</strong> → multi-agent, reasoning-based retrieval that packs only the facts that matter</li>
      <li><strong>Lifecycle Management</strong> → facts are versioned, updated, and conflict-resolved automatically</li>
      <li><strong>Autonomous CoT Orchestration</strong> → self-directed reasoning → fewer tokens, faster replies, higher accuracy</li>
      <li><strong>Data Governance</strong> → white-box by design — full traceability, provenance, and user-level control baked in</li>
    </ul>
  </div>

<div>
    <h2>🎯 Use Cases</h2>
    <ul>
      <li><strong>Personal AI</strong> → not memory. Awareness that adapts to you in real time</li>
      <li><strong>Customer Support</strong> → not logs. Clear user story that resolves issues on the first touch</li>
      <li><strong>Healthcare</strong> → not raw data. Connect all the dots for reliable patient profiles → safer adaptive care</li>
      <li><strong>Developer &amp; Creator Copilots</strong> → not autocomplete. Repo + workflow intelligence that guides the next move</li>
    </ul>
  </div>


<h2>🚀 Get started (seriously, 5 min)</h2>

1️⃣ Create your account and fetch your api key→ <a href="https://api.ontbo.com">https://api.ontbo.com</a>

2️⃣ Install the lib
```
pip install ontbo
```

3️⃣ Your first application in a few lines of code.
```py
from ontbo import Ontbo, SceneMessage

ontbo = Ontbo(token="<YOU_API_KEY_HERE>")
profile = ontbo.create_profile("alice_test")
scene = profile.create_scene("scene_test")

scene.add_messages(
  [SceneMessage(content="Hello, my name is Alice!")], 
  update_now=True)

print(profile.query_facts("What the user's name?"))
```

  <p>💡 Not using Python? See directly our Web API reference → <a href="https://api.ontbo.com/api/tests/docs">https://api.ontbo.com/api/tests/docs</a></p>
  </div>

<h2> 🤖 Why Ontbo? </h2>

The biggest bottleneck for AI agents isn't the model—it's the **context**. 
Stop duct-taping prompt engineering and messy RAG pipelines. Ontbo provides a specialized **Cognitive Context API** that acts as a sophisticated memory layer for your LLMs.

* **📉 Cut Token Waste:** Don't resend the same facts. Ontbo optimizes what goes into the prompt.
* **🚫 Kill Hallucinations:** Ground your agent with verified, retrieved facts in real-time.
* **🧠 Human-like Memory:** Manage complex user histories and cross-session knowledge effortlessly.
* **⚡ Dev-First:** Integrates with your existing stack in minutes.

  <div>
    <h2>⚡ Research Insights - Why you Win ?</h2>
    <table>
      <tr>
        <th><i>Metric</i></th>
        <th><i>ONTBO</i></th>
        <th><i>SoTA</i></th>
      </tr>
      <tr>
        <td><i>Recall context</i></td>
        <td><b>🔥 91%</b></td>
        <td>70%</td>
      </tr>
      <tr>
        <td><i>Token cost</i></td>
        <td><b>💸 -95%</b></td>
        <td>Full-data retrieval</td>
      </tr>
      <tr>
        <td><i>Latency</i></td>
        <td><b>⚡ 40 ms (P50)</b></td>
        <td>&gt;200 ms</td>
      </tr>
      <tr>
        <td><i>Model creation speed</i></td>
        <td><b>🚀 +200%</b></td>
        <td>Baseline</td>
      </tr>
    </table>
    <p>🔄 <b>4 retrieval modes</b>: best-performance, chain-of-thought, balanced, low-latency<br>
    ✔️ pick precision/latency/cost tradeoffs per request</p>
  </div>

---
  
## ⚡️ Performance Showcase: ChatGPT 5.2 x Ontbo API

Context fragmentation is the silent killer of AI efficiency. See how Ontbo transforms a standard LLM interaction by providing a sophisticated cognitive memory layer.

### 🎬 Comparative Demo
[![Watch the Demo](https://img.youtube.com/vi/e0uITdv5xlc/maxresdefault.jpg)](https://www.youtube.com/watch?v=e0uITdv5xlc)

| Feature | ChatGPT (5.2 thinking) | ChatGPT + Ontbo API |
| :--- | :--- | :--- |
| **Context Retention** | Limited / "Forgetful" | **Persistent & Cognitive** |
| **Retrieval Accuracy** | Basic RAG (Messy) | **Specialized Memory Layer** |
| **Logic Consistency** | Dribbles over long sessions | **Maintains High-Fidelity Logic** |

> **Key Takeaway:** While standard models struggle with "duct-taped" prompt engineering, Ontbo ensures your agent actually *understands* the historical context of the conversation.

<div>
    <h2>🏗 Strategic Benefits (Product &amp; Infra)</h2>
    <ul>
      <li><strong>Product</strong> → sharper, context-aware responses → higher CSAT &amp; conversions</li>
      <li><strong>Infra</strong> → big LLM token savings &amp; lower inference load → measurable cost reductions</li>
      <li><strong>Moat</strong> → fine-grained, context-rich personalization with traceable provenance</li>
      <li><strong>Ops</strong> → faster model creation &amp; iteration (+200%), predictable scaling, fewer cold starts</li>
    </ul>
  </div>

<img width="3509" height="2481" alt="Benchmark Ontbo_2026" src="https://github.com/user-attachments/assets/27301fb8-7834-4dba-af52-098824243db5" />
 <p> This is not merely another vendor-biased benchmark. This performance analysis, comparing ChatGPT 5.2 without Ontbo API and ChatGPT 5.2 with Ontbo API, follows a rigorous methodology formally validated by the Cambridge University Scientific Board in December 2025. Based on 19 items (demographics, cognition, health, finances…).
Performance was measured across more than 500 multi-turn conversations, comparing intrinsic hashtag#LLM memory with an external conversational memory layer.

➡️ This benchmark shows what happens when an external cognitive context layer works alongside leading models, with long-term reasoning reaching up to 93% recall accuracy. 
➡️ It’s not a RAG, not memory tools, not a buffer. <p>

  <div>
    <h2>📚 Documentation &amp; Support</h2>
    <ul>
      <li><strong>API reference docs:</strong> <a href="https://api.ontbo.com/api/tests/docs">https://api.ontbo.com/api/tests/docs</a></li>
      <li><strong>Community:</strong> <a href="https://discord.com/invite/N8h4ZBJb">Discord</a> · <a href="https://x.com/ONTBO_AI">X</a></li>
      <li><strong>Contact:</strong> <a href="mailto:contact@ontbo.com">contact@ontbo.com</a></li>
    </ul>
  </div>

  <div>
    <h2>🤝 License &amp; Contributions</h2>
    <ul>
      <li><strong>License: </strong><a href="./LICENSE">Apache 2.0</a></li>
      <li><strong>Contributions:</strong> PRs welcome. Open issues for bugs/feature requests</li>
      <li><strong>Security:</strong> responsible disclosure at contact@ontbo.com</li>
    </ul>
  </div>

  <br><p>✨ Let’s build something people didn’t think was possible.<br>
  🔥 Go break things (and tell us what you build).</p>


<b>If you find this useful, please give us a ⭐ to help others find us!</b>
</p>

</body>
</html>























