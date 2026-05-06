import json
import tempfile
import unittest
from pathlib import Path

from scripts import movie_sync


SAMPLE_SRT = """1
00:00:01,000 --> 00:00:03,000
The door is locked.

2
00:00:08,000 --> 00:00:10,000
I heard something upstairs.

3
00:00:30,000 --> 00:00:32,000
This later line must stay hidden.
"""


class MovieSyncTests(unittest.TestCase):
    def test_context_stays_before_safe_time(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subtitle = root / "sample.srt"
            index = root / "sample.movie-index.json"
            session = root / "sample.watch-session.json"
            subtitle.write_text(SAMPLE_SRT, encoding="utf-8")

            movie_sync.cmd_index(
                type("Args", (), {"subtitle": [str(subtitle)], "description": None, "movie": "Sample", "output": str(index)})
            )
            movie_sync.cmd_start(
                type(
                    "Args",
                    (),
                    {
                        "index": str(index),
                        "at": "00:00:12",
                        "rate": 1.0,
                        "safety_lag": 0.0,
                        "session": str(session),
                        "state_dir": None,
                    },
                )
            )

            payload = movie_sync.context_payload(session, before=20, after=0, require_open=True)
            texts = [cue["text"] for cue in payload["cues"]]
            self.assertIn("The door is locked.", texts)
            self.assertIn("I heard something upstairs.", texts)
            self.assertNotIn("This later line must stay hidden.", texts)

    def test_closed_session_blocks_ask_context(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            index = root / "sample.movie-index.json"
            session = root / "sample.watch-session.json"
            index.write_text(json.dumps({"movie": "Sample", "cues": []}), encoding="utf-8")
            session.write_text(
                json.dumps(
                    {
                        "index": str(index),
                        "mode": "closed",
                        "started_at_wall_utc": "2026-01-01T00:00:00+00:00",
                        "started_at_movie_seconds": 0,
                        "closed_at_movie_seconds": 12,
                        "safety_lag_seconds": 0,
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaises(SystemExit):
                movie_sync.context_payload(session, before=20, after=0, require_open=True)


if __name__ == "__main__":
    unittest.main()
