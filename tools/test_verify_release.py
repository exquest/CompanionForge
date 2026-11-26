"""Unit tests for verify_release. Run: python3 -m unittest discover tools"""

import unittest

from verify_release import ROOT, section_code_block

HEADING = "## Artifact 1 — Project Instructions"


def doc(*lines: str) -> str:
    return "\n".join(lines) + "\n"


class SectionCodeBlockTests(unittest.TestCase):
    def test_returns_block_under_heading(self):
        text = doc("# Title", HEADING, "", "```text", "line one", "line two", "```")
        self.assertEqual(section_code_block(text, HEADING), "line one\nline two")

    def test_accepts_untagged_and_tilde_fences(self):
        for opener, closer in (("```", "```"), ("~~~", "~~~"), ("````md", "````")):
            with self.subTest(opener=opener):
                text = doc(HEADING, opener, "body", closer)
                self.assertEqual(section_code_block(text, HEADING), "body")

    def test_does_not_read_a_block_from_a_later_section(self):
        text = doc(
            HEADING, "Paste the block below.", "```", "instructions", "```",
            "## Artifact 3 — Kickoff prompt", "```text", "New Companion", "```",
        )
        self.assertEqual(section_code_block(text, HEADING), "instructions")
        no_block = doc(
            HEADING, "Prose only.",
            "## Artifact 3 — Kickoff prompt", "```text", "New Companion", "```",
        )
        self.assertIsNone(section_code_block(no_block, HEADING))

    def test_subheading_stays_inside_the_section(self):
        text = doc(HEADING, "### Notes", "```", "body", "```")
        self.assertEqual(section_code_block(text, HEADING), "body")

    def test_setext_heading_ends_the_section(self):
        for underline in ("---", "==="):
            with self.subTest(underline=underline):
                text = doc(HEADING, "Next section", underline, "```", "later", "```")
                self.assertIsNone(section_code_block(text, HEADING))

    def test_thematic_break_does_not_end_the_section(self):
        for text in (
            doc(HEADING, "Prose", "", "---", "```", "body", "```"),
            doc(HEADING, "---", "```", "body", "```"),
        ):
            with self.subTest(text=text):
                self.assertEqual(section_code_block(text, HEADING), "body")

    def test_opening_fence_indent_is_removed_from_content(self):
        text = doc(HEADING, "  ```", "  a", "    b", " c", "  ```")
        self.assertEqual(section_code_block(text, HEADING), "a\n  b\nc")

    def test_lines_break_only_at_markdown_line_endings(self):
        crlf = doc(HEADING, "```", "a", "b", "```").replace("\n", "\r\n")
        self.assertEqual(section_code_block(crlf, HEADING), "a\nb")
        separator = doc(HEADING, "```", "a ## b\x0c```", "```")
        self.assertEqual(section_code_block(separator, HEADING), "a ## b\x0c```")

    def test_only_a_bare_matching_fence_closes_the_block(self):
        text = doc(
            HEADING, "````text", "```python", "code", "```", "~~~", "````",
        )
        self.assertEqual(
            section_code_block(text, HEADING), "```python\ncode\n```\n~~~"
        )
        tagged_line = doc(HEADING, "```", "```python", "x", "```")
        self.assertEqual(section_code_block(tagged_line, HEADING), "```python\nx")

    def test_heading_named_in_prose_is_not_the_section(self):
        text = doc(
            f"See {HEADING} below.", "```", "wrong", "```", HEADING, "```", "right", "```",
        )
        self.assertEqual(section_code_block(text, HEADING), "right")

    def test_missing_heading_or_unclosed_fence_returns_none(self):
        self.assertIsNone(section_code_block(doc("## Other", "```", "x", "```"), HEADING))
        self.assertIsNone(section_code_block(doc(HEADING, "```text", "x"), HEADING))

    def test_measures_the_shipped_chatgpt_instructions(self):
        text = (ROOT / "CompanionForge_SelfUpdating_ChatGPT.md").read_text(encoding="utf-8")
        block = section_code_block(text, HEADING)
        self.assertIsNotNone(block)
        self.assertTrue(block.startswith("You are the self-updating ChatGPT Companion Forge."))
        self.assertNotIn("## Artifact", block)
        self.assertLessEqual(len(block), 4500)


if __name__ == "__main__":
    unittest.main()
