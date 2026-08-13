import importlib.util
import unittest
from pathlib import Path


class EvidenceControlTests(unittest.TestCase):
    def test_controlled_evidence_validator_passes(self):
        root = Path(__file__).resolve().parents[1]
        script = root / "scripts" / "validate_evidence.py"
        spec = importlib.util.spec_from_file_location("validate_evidence", script)
        module = importlib.util.module_from_spec(spec)
        self.assertIsNotNone(spec.loader)
        spec.loader.exec_module(module)
        self.assertEqual(module.main(), 0)
