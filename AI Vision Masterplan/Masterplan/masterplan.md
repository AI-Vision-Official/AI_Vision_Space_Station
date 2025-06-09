# Human-readable Markdown version
markdown_text = """

# AI Brain Workflow System

## Description:
Create a structured AI collaboration environment where AI and human can work together to reach certain goals, but also enables AI to function in an automated and evolving workflow using (or creating) AI agents. 
Doel: structured colleboration between Brigitte and AI on projects, with overview and memory.

---

## 📌 Goals

1. **Collaboration Environment between AI and Human**
   - AI workd together with Brigitte
   - With overview and memory

2. **DF & DFG usage as triggers**
   - **DF** = Start: start trigger: loads context and activates workflow
   - **DFG** = Stop: stop trigger: summarizes, saves, and updates files

3. **Blueprint and Masterplan as one evolving document**
   - Each session creates a log
   - Data saved in:
     - `state.json`
     - `blueprint.json`
     - `task-log.md`
     - `masterplan.md`

4. **AI fully understands the project state**
   - Reads state.json and blueprint.json
   - Knows goals, pending items, decisions

5. **Human-AI collaboration with GUI**
   - Tab: "AI Vision Team"
   - GUI is Python-based
   - DF/DFG triggers via ChatGPT or GUI
   - GitHub: private with token-based access
   - Local sync on PC boot and after each DFG
   - Sync script: git pull → commit → push (automated)


6. **Implemented redundancy and failover**
   - Backups in JSON, Markdown en database

---

## 🧠 Architecture

- **Agents**: Human GUI, Agent 1, Agent 2, ChatGPT Agent
- **Triggers**: DF and DFG
- **GitHub Repo**: Private, token-based access
- **Local sync**: On PC boot and after each DFG
- **Sync-script**: `git pull → commit → push` (automated)

---

## 📁 Structure and File system

### Directories
- `masterplan/blueprint.json`
- `masterplan/masterplan.md`
- `logs/state.json`
- `logs/task-log-YYYY-MM-DD.md`
- `agents/agent1.py`
- `gui_launcher/*.py`
- `api/*.js`
- `settings/settings.yaml`

### Lokale paden (voorbeeld)
- `L:/GIT/Projects/.../blueprint.json`
- `.../task-log-YYYY-MM-DD.md`
- `.../ai_vision_command_launcher.py`

---

## 🔁 Workflow (Triggers)

### DF (Start)
- Loads blueprint & state
- Starts workflow
- Activates agents, assigns tasks

### DFG (Stop)
- Summarizes (by AI)
- Update:
  - `state.json`
  - `blueprint.json`
  - `task-log`
  - `masterplan.md`
- Commit + push naar GitHub

---

## 📊 File type and definition

| File type    | Definition                  |
|--------------|-----------------------------|
| `.json`      | Machine memory (AI)         |
| `.md`        | Human Readable logs         |

---

## 🧪 Example masterplan-item

- **Date**: 2025-06-09  
- **Trigger**: DF by GUI  
- **Taken**: Drought analysis, Logistics scan  
- **Resultaten**:
  - Agent1: mapped high-risk drought zones
  - Agent2: ran aid delivery simulation
- **Insights**:
  - Use OSM overlays for faster mapping
  - Prioritize unstable regions

---

## ⏱️ Example `state.json`

```json
{
  "current_workflow": "drought-aid-africa",
  "step": "logistics-mapping",
  "agents_active": ["agent1", "agent2"],
  "last_trigger": "DF",
  "last_update": "2025-06-09T11:00Z"

    "agent_behavior_example": {
      "file": "agent1.py",
      "logic": [
        "Read blueprint",
        "Read state",
        "If workflow = drought-aid-africa → analyze",
        "Write task-log",
        "Update blueprint",
        "Update masterplan",
        "Update state",
        "Push to GitHub"
}
