import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional

HISTORY_PATH = Path("history/pipeline_history.json")
HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)

def _now():
    return datetime.now(timezone.utc).isoformat()

@dataclass
class TrackerSession:
    run_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    start_time: str = field(default_factory=_now)
    stages: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    args: Dict[str, Any] = field(default_factory=dict)

    def set_args(self, args: Dict[str, Any]):
        self.args = args

    def start_stage(self, name: str):
        self.stages[name] = {
            "start_time": _now(),
            "duration_sec": None,
            "data": None,
            "error": None
        }

    def end_stage(self, name: str, duration: Optional[float] = None, data: Any = None):
        if name not in self.stages:
            self.start_stage(name)  # Ensure stage exists
        stage = self.stages[name]
        if duration is not None:
            stage["duration_sec"] = round(duration, 4)
        stage["data"] = data

    def log_error(self, name: str, error: str):
        if name not in self.stages:
            self.start_stage(name)
        self.stages[name]["error"] = error
        self.stages[name]["end_time"] = _now()

    def finalize(self):
        end_time = datetime.now(timezone.utc)
        start_time_obj = datetime.fromisoformat(self.start_time)
        total_duration = round((end_time - start_time_obj).total_seconds(), 4)

        record = {
            "run_id": self.run_id,
            "start_time": self.start_time,
            "args": self.args,
            "stages": self.stages,
            "completed_at": end_time.isoformat(),
            "total_duration_sec": total_duration
        }

        # Load existing history if present
        if HISTORY_PATH.exists():
            try:
                with open(HISTORY_PATH, "r") as f:
                    history = json.load(f)
                if not isinstance(history, list):
                    history = []
            except json.JSONDecodeError:
                history = []
        else:
            history = []

        history.append(record)
        with open(HISTORY_PATH, "w") as f:
            json.dump(history, f, indent=2)

