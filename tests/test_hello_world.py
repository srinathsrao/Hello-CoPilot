import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from hello_world import greet  # noqa: E402

HELLO_WORLD_SCRIPT = SRC_DIR / "hello_world.py"


class TestHelloWorld(unittest.TestCase):
    @patch("builtins.print")
    def test_greet_positive(self, mock_print):
        greet("CoPilot")
        mock_print.assert_called_once_with("Hello CoPilot")

    def test_main_missing_name_negative(self):
        result = subprocess.run(
            [sys.executable, str(HELLO_WORLD_SCRIPT)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("name", result.stderr.lower())


if __name__ == "__main__":
    unittest.main()
