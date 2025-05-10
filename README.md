# stage-tracker

A lightweight, zero-dependency Python library for tracking multi-stage pipeline executions.  
`stage-tracker` helps developers log structured run metadata, track stage durations, and debug complex flows — all with minimal effort.

---

## 📦 What is `stage-tracker`?

When you're running a pipeline — whether in AI research, cybersecurity defense, data processing, or experimentation — it's critical to:
- Capture what ran
- When it ran
- How long it took
- What went wrong (or right)

`stage-tracker` simplifies this with structured JSON output that records:
- Pipeline-level metadata (e.g., run ID, args, start/end time)
- Named **stages**, each with start time, duration, output data, and error info

This makes your system **observable, auditable**, and **debuggable**.

---

## ✨ Features

- 🔹 UUID-based `run_id` for traceability
- 🕒 ISO-formatted timestamps with timezone
- 📊 Track multiple stages independently or sequentially
- 💥 Record exception/error messages per stage
- 📁 Save output as a structured JSON file
- 🧼 Minimal, clean API with no third-party dependencies

---

## 🧑‍💻 Installation

```bash
pip install -e .
# Or using uv (recommended)
uv pip install -e .
```

---

## 🚀 Quick Start

```python
from stage_tracker import Tracker

# Initialize a tracker for a given run
tracker = Tracker(args="Reconnaissance_M1")

# Track stages
tracker.start_stage("Detection")
# ... run detection logic ...
tracker.end_stage("Detection", data={"status": "clean"})

tracker.start_stage("Enrichment")
# ... enrichment logic ...
tracker.end_stage("Enrichment", data={"added_cves": 3})

# Finalize and save
tracker.finalize("run_output.json")
```

Output (run_output.json):
```json
{
  "run_id": "af3c980c-3d22-46e8-83cd-7ff99abee586",
  "start_time": "2025-05-05T23:14:10.235518+00:00",
  "args": "Reconnaissance_M1",
  "stages": {
    "Detection": {
      "start_time": "...",
      "duration_sec": 3.42,
      "data": {"status": "clean"},
      "error": null
    },
    "Enrichment": {
      "start_time": "...",
      "duration_sec": 1.01,
      "data": {"added_cves": 3},
      "error": null
    }
  },
  "completed_at": "...",
  "total_duration_sec": 9.42
}
```

---

## 🧩 Use Cases

- 🔍 **AI/ML Experiments**: Measure durations of preprocessing, training, evaluation.
- 🛡 **Cybersecurity Pipelines**: Log detection, enrichment, and mitigation stages.
- ⚙️ **ETL/Batch Jobs**: Trace and debug stage-level runtime or failures.
- 📄 **Paper Reproducibility**: Attach structured logs for each experiment run.

---

## 🛠 How It Works

1. Instantiate `Tracker(args=...)`
2. For each stage:
   - Call `start_stage("StageName")`
   - Run logic
   - Call `end_stage("StageName", data=..., error=...)`
3. When done, call `tracker.finalize("output.json")`

Internally, it tracks timestamps, computes durations, and writes JSON output.

---

## 📂 Project Structure

```bash
stage-tracker/
├── stage_tracker/
│   ├── __init__.py
│   └── tracker.py
├── pyproject.toml
├── LICENSE
└── README.md
```

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## 🤝 Contributing

Pull requests are welcome. Feel free to fork and improve!
If you find a bug or want to request a feature, please open an issue and I'll do my best to review and address issues promptly.


---

## 📬 Contact

Maintained by Karim Ahmed.  
Email: karim.ahmed4815@gmail.com
GitHub: [rexmirak](github.com/rexmirak)