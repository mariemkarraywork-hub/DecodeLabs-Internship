# Architectural Code Explanation

## IPO data flow

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ INPUT       │     │ PROCESS          │     │ OUTPUT          │
│ raw_input   │ ──► │ INTENT_MAP.get() │ ──► │ emit_response() │
│ sanitize_   │     │ (+ callable if   │     │ print to user   │
│ input()     │     │  time/date)      │     │                 │
└─────────────┘     └──────────────────┘     └─────────────────┘
```

1. **Input:** `input('You: ')` captures `raw_input`. `sanitize_input()` produces `clean_input` (`.lower().strip()`).
2. **Process:** `process_intent(clean_input)` performs a single dictionary lookup. Unknown intents resolve to the fallback string in one `.get()` call.
3. **Output:** `emit_response()` prints the final message (`Chatbot: ...`).

Exit commands are checked on `clean_input` before process/output so the loop terminates cleanly.

## Why dictionary lookup is O(1)

Python `dict` is a hash table. Average-case `INTENT_MAP.get(key, default)` is **O(1)**:

- Hash the key → find bucket → return value (or default).

An **if-elif ladder** scans conditions sequentially: **O(n)** in the number of rules, with growing maintenance cost.

With 20 intents, dict lookup is one hash operation; elif may compare up to 20 times. At scale, dict lookup time stays effectively constant; elif grows linearly.

**Atomic fallback:** `INTENT_MAP.get(clean_input, _FALLBACK)` combines lookup and default in one expression — no separate `if key not in map` branch for unknown inputs.
