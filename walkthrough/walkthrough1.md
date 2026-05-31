# Rule-Based Chatbot — Complete Walkthrough

DecodeLabs · Project 1 · Batch 2026. This guide replaces inline code comments: architecture, every feature, commands, testing, and how to extend the bot.

---

## 1. What this project is

A **rule-based chatbot** with **no machine learning**. It matches user text against a fixed **intent dictionary** (`INTENT_MAP`) and returns predefined answers. Lookup is **O(1)** via Python `dict.get()` — there is **no if-elif ladder** for intents.

Two ways to use it:

| Interface | File | Best for |
|-----------|------|----------|
| Terminal | `chatbot.py` | Spec submission, tests, learning IPO flow |
| Browser | `front.html` | Demo UI, quick replies, visual chat |

Supporting files:

| File | Role |
|------|------|
| `ARCHITECTURE.md` | IPO diagram + why dict lookup is O(1) |
| `test_chatbot.py` | Automated checks (sanitization, intents, fallback) |
| `../walkthrough/walkthrough1.md` | This document |

---

## 2. Architecture (IPO model)

```
USER types message
       │
       ▼
┌──────────────────────────────────────┐
│ INPUT — sanitize_input()             │
│ raw_input → lower + strip            │
│ e.g. "  HeLLo  " → "hello"           │
└──────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│ PROCESS — process_intent()           │
│ INTENT_MAP.get(clean_input, fallback)│
│ callables run for live time/date     │
└──────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│ OUTPUT — emit_response()             │
│ prints "Chatbot: ..."                │
└──────────────────────────────────────┘
```

**Heartbeat:** `main()` runs `while True` until you type `exit`, `quit`, or `bye`, or press `Ctrl+C`.

**Anti-pattern avoided:** Do not add `elif` chains for new intents. Only add keys to `INTENT_MAP`.

More detail: read `ARCHITECTURE.md`.

---

## 3. What each part of `chatbot.py` does

| Name | Type | What it does |
|------|------|----------------|
| `_GREETING`, `_HELP`, `_FALLBACK` | Constants | Shared reply text and default unknown reply |
| `EXIT_COMMANDS` | `frozenset` | Words that stop the loop: `exit`, `quit`, `bye` |
| `_time_response()` | Function | Builds live time string when user asks for time |
| `_date_response()` | Function | Builds live date string when user asks for date |
| `_time_based_greeting_response()` | Function | Morning / afternoon / evening from current hour |
| `INTENT_MAP` | `dict` | Maps normalized user phrase → string **or** callable (for time/date) |
| `sanitize_input()` | Function | Input phase: `.lower().strip()` |
| `process_intent()` | Function | Process phase: `.get()` + run callable if needed |
| `emit_response()` | Function | Output phase: print bot line |
| `main()` | Function | Welcome banner, infinite loop, exit handling |

**Important rule:** Keys in `INTENT_MAP` must match **exactly** what the user types **after** sanitization. `"Hello"` and `"  HELLO  "` both become `"hello"` and match the `"hello"` key.

**Callable values:** For answers that change every second (time/date), the dict stores a function (`_time_response`, `_date_response`). After lookup, `process_intent` calls it once and returns the string.

---

## 4. All built-in functionalities

### 4.1 Conversation intents

| Category | You can type (after sanitization) | Bot behavior |
|----------|-----------------------------------|--------------|
| Greetings | `hello`, `hi`, `hey`, `greetings` | Welcome message |
| Help | `help`, `what can you do?`, `what can you do` | Lists what the bot supports |
| Time | `time`, `what time is it?`, `what time is it` | Current local time (HH:MM) |
| Date | `date`, `what is the date?`, `what is the date` | Current local date (YYYY-MM-DD) |
| Time-based greet | `greet`, `smart greeting`, `time greeting` | Good morning (5–11), afternoon (12–17), evening (otherwise) |
| Unknown | anything not in the table | `I do not understand.` |

### 4.2 Input sanitization

- Leading/trailing spaces removed.
- Full string lowercased.
- Example: `"  HeLLo  "` → `"hello"` → greeting reply.

### 4.3 Empty input

- Blank lines are ignored (no reply, loop continues).

### 4.4 Exit

- `exit`, `quit`, or `bye` → goodbye message and program ends.
- `Ctrl+C` → goodbye and program ends (KeyboardInterrupt).

### 4.5 Browser UI (`front.html`)

Same intent map as Python (in JavaScript). Extra UI features:

- Dark chat layout, typing indicator, message timestamps
- Quick-reply buttons (Hello, What can you do?, Current time, Smart greet)
- `Enter` to send, `Shift+Enter` for new line in the text box

---

## 5. Commands you need to know

### 5.1 Go to the project folder

```powershell
cd C:\Users\karra\.gemini\antigravity\scratch\IA\rule_based_chatbot
```

### 5.2 Run the terminal chatbot

```powershell
python chatbot.py
```

Sample session:

```
You: hello
Chatbot: Hello! How can I help you today?
You: time
Chatbot: The current time is 14:30.
You: gibberish
Chatbot: I do not understand.
You: exit
Chatbot: Goodbye! Have a great day learning AI!
```

### 5.3 Run automated tests

```powershell
python -m unittest test_chatbot.py -v
```

All tests should pass (`OK`).

### 5.4 Open the browser chatbot

Double-click `front.html`, or:

```powershell
Start-Process .\front.html
```

Optional local server (if the browser blocks some features):

```powershell
python -m http.server 8080
```

Then open: `http://localhost:8080/front.html`

### 5.5 Stop the terminal chatbot

- Type `exit`, `quit`, or `bye`, **or**
- Press `Ctrl+C`

---

## 6. Manual testing checklist

Run `python chatbot.py` and verify:

- [ ] `hello` → greeting
- [ ] `  HeLLo  ` → same greeting (sanitization)
- [ ] `help` → help text
- [ ] `time` → shows current time
- [ ] `date` → shows today’s date
- [ ] `greet` → Good morning, afternoon, or evening (depends on clock)
- [ ] `status` or `project` → `I do not understand.` (removed intents)
- [ ] random text → `I do not understand.`
- [ ] `exit` → goodbye and program stops

Then open `front.html` and try the quick-reply chips and the same phrases in the chat box.

---

## 7. How to add a new feature

Always extend the **dictionary**, never an if-elif chain for intents.

### 7.1 Simple fixed reply (same answer every time)

**Step 1 — `chatbot.py`:** Add one or more keys inside `INTENT_MAP` (keys must be lowercase; users can type any casing):

```python
"good morning": "Good morning! Hope you have a productive day.",
"thanks": "You're welcome!",
```

Reuse an existing constant if several phrases share one answer:

```python
"thanks": _GREETING,
"thank you": _GREETING,
```

**Step 2 — `front.html`:** Add the same keys inside the JavaScript `INTENT_MAP` object (search for `const INTENT_MAP`):

```javascript
"good morning": "Good morning! Hope you have a productive day.",
thanks: "You're welcome!",
```

**Step 3 — Tests (recommended):** In `test_chatbot.py`, add a test method, e.g.:

```python
def test_good_morning(self):
    self.assertIn("Good morning", process_intent("good morning"))
```

Run: `python -m unittest test_chatbot.py -v`

**Step 4 — Walkthrough:** Add the new phrase to section 4.1 table in this file so you remember it later.

### 7.2 Live / dynamic reply (changes each time)

**Python:** Create a function, then point intents at it (like `_time_response`):

```python
def _joke_response() -> str:
    return "Why do programmers prefer dark mode? Because light attracts bugs!"

INTENT_MAP = {
    ...
    "joke": _joke_response,
    "tell me a joke": _joke_response,
}
```

**Browser:** Use a function value in `INTENT_MAP`:

```javascript
joke: () => "Why do programmers prefer dark mode? Because light attracts bugs!",
```

### 7.3 New quick-reply button (browser only)

In `front.html`, find `<div class="quick-replies">` and add:

```html
<button class="quick-reply-btn" data-msg="good morning">☀️ Good morning</button>
```

`data-msg` must match a key in `INTENT_MAP` after sanitization (lowercase).

### 7.4 Change fallback message

**Python:** Edit `_FALLBACK` in `chatbot.py`.

**Browser:** Edit `const FALLBACK` in `front.html`.

**Tests:** Update `test_unknown_uses_fallback` if the exact string changed.

### 7.5 Add a new exit word

**Python:** Add to `EXIT_COMMANDS`, e.g. `frozenset({"exit", "quit", "bye", "goodbye"})`.

**Tests:** Update `TestExitCommands` expected set.

Browser does not exit the page on bye; it only replies via intents unless you add custom JS.

### 7.6 Change welcome banner or colors

| What | Where |
|------|--------|
| Terminal welcome text | `main()` print lines in `chatbot.py` |
| Browser title / header | `<header>` and `<title>` in `front.html` |
| Colors / theme | `:root { ... }` CSS variables in `front.html` |
| First bot message on load | `DOMContentLoaded` block at bottom of `front.html` |

### 7.7 Multiple phrases → one answer

Duplicate keys with the same value (or same function):

```python
"bye": _GREETING,
"good day": _GREETING,
```

Do **not** use substring matching (`if "time" in text`) unless you deliberately leave the dict model — the project spec requires exact key lookup after sanitization.

---

## 8. File structure

```
rule_based_chatbot/
├── chatbot.py          # Terminal bot (IPO + INTENT_MAP)
├── front.html          # Browser UI + JS intent map
├── test_chatbot.py     # Unit tests
├── ARCHITECTURE.md     # IPO + O(1) explanation
└── ../walkthrough/walkthrough1.md
```

---

## 9. Common mistakes

| Mistake | Fix |
|---------|-----|
| New intent not working | Key must match `clean_input` exactly (lowercase, stripped) |
| Works in Python, not in browser | Add the same key to JS `INTENT_MAP` in `front.html` |
| Used `elif` for intents | Remove it; use dict keys only |
| Typo in key | `"what time is it"` vs `"what time is it?"` are different keys — add both if needed |
| Forgot to run tests | `python -m unittest test_chatbot.py -v` |

---

## 10. Quick reference

| Goal | Command or location |
|------|---------------------|
| Start terminal bot | `python chatbot.py` |
| Run tests | `python -m unittest test_chatbot.py -v` |
| Open web UI | `Start-Process .\front.html` |
| Add intent | `INTENT_MAP` in `chatbot.py` + `front.html` |
| Understand IPO / O(1) | `ARCHITECTURE.md` |
| Full behavior list | Section 4 of this file |
