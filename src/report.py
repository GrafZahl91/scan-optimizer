import json
from pathlib import Path


class Report:

    def save(self, job):

        out = Path("/debug") / job.name
        out.mkdir(parents=True, exist_ok=True)

        with open(out / "report.json", "w") as f:
            json.dump(
                job.report,
                f,
                indent=2,
            )
