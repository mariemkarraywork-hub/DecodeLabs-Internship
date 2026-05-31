import unittest

from chatbot import (
    EXIT_COMMANDS,
    INTENT_MAP,
    _FALLBACK,
    process_intent,
    sanitize_input,
)


class TestSanitization(unittest.TestCase):
    def test_strips_and_lowercases(self):
        self.assertEqual(sanitize_input("  HeLLo  "), "hello")

    def test_empty_after_strip(self):
        self.assertEqual(sanitize_input("   "), "")


class TestIntentMatching(unittest.TestCase):
    def test_greeting(self):
        self.assertIn("Hello", process_intent("hello"))

    def test_help(self):
        self.assertIn("greetings", process_intent("help").lower())

    def test_time_intent_returns_time_string(self):
        self.assertIn("current time", process_intent("time").lower())

    def test_date_intent_returns_date_string(self):
        self.assertIn("today's date", process_intent("date").lower())

    def test_time_based_greeting(self):
        reply = process_intent("greet").lower()
        self.assertTrue(
            "good morning" in reply
            or "good afternoon" in reply
            or "good evening" in reply
        )

    def test_unknown_uses_fallback(self):
        self.assertEqual(process_intent("xyzzy nonsense"), _FALLBACK)


class TestKnowledgeBase(unittest.TestCase):
    def test_at_least_five_intent_categories(self):
        categories = {
            "greetings": {"hello", "hi"},
            "help": {"help"},
            "time": {"time"},
            "date": {"date"},
            "time_greeting": {"greet"},
        }
        for keys in categories.values():
            self.assertTrue(keys.issubset(INTENT_MAP.keys()))

    def test_get_fallback_atomic(self):
        self.assertEqual(INTENT_MAP.get("not_a_real_intent", _FALLBACK), _FALLBACK)


class TestExitCommands(unittest.TestCase):
    def test_exit_commands_defined(self):
        self.assertEqual(EXIT_COMMANDS, frozenset({"exit", "quit", "bye"}))


if __name__ == "__main__":
    unittest.main()
