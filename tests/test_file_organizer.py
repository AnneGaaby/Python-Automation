import tempfile
import unittest
from pathlib import Path

from examples.file_organizer import category_for, organize


class FileOrganizerTests(unittest.TestCase):
    def test_category_for_image(self):
        self.assertEqual(category_for(Path("photo.PNG")), "images")

    def test_preview_does_not_move_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary)
            sample = source / "notes.txt"
            sample.write_text("demo", encoding="utf-8")

            moves = organize(source)

            self.assertEqual(len(moves), 1)
            self.assertTrue(sample.exists())
            self.assertFalse((source / "documents" / "notes.txt").exists())

    def test_apply_moves_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary)
            sample = source / "notes.txt"
            sample.write_text("demo", encoding="utf-8")

            organize(source, apply=True)

            self.assertFalse(sample.exists())
            self.assertTrue((source / "documents" / "notes.txt").exists())


if __name__ == "__main__":
    unittest.main()
