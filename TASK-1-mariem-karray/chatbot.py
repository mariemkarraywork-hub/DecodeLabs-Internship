import datetime
from collections.abc import Callable

_GREETING = "Hello! How can I help you today?"
_HELP = (
    "I can respond to greetings, help, time/date, and a time-based greet. "
    "Try: hello, help, time, date, greet."
)
_FALLBACK = "I do not understand."

EXIT_COMMANDS = frozenset({"exit", "quit", "bye"})


def _time_response() -> str:
    now = datetime.datetime.now().strftime("%H:%M")
    return f"The current time is {now}."


def _date_response() -> str:
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"Today's date is {today}."


def _time_based_greeting_response() -> str:
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning! How can I help you today?"
    if 12 <= hour < 18:
        return "Good afternoon! How can I help you today?"
    return "Good evening! How can I help you today?"


INTENT_MAP: dict[str, str | Callable[[], str]] = {
    "hello": _GREETING,
    "hi": _GREETING,
    "hey": _GREETING,
    "greetings": _GREETING,
    "help": _HELP,
    "what can you do?": _HELP,
    "what can you do": _HELP,
    "time": _time_response,
    "what time is it?": _time_response,
    "what time is it": _time_response,
    "date": _date_response,
    "what is the date?": _date_response,
    "what is the date": _date_response,
    "greet": _time_based_greeting_response,
    "smart greeting": _time_based_greeting_response,
    "time greeting": _time_based_greeting_response,
}


def sanitize_input(raw_input: str) -> str:
    return raw_input.lower().strip()


def process_intent(clean_input: str) -> str:
    response = INTENT_MAP.get(clean_input, _FALLBACK)
    return response() if callable(response) else response


def emit_response(response: str) -> None:
    print(f"Chatbot: {response}")


def main() -> None:
    print("=====================================================")
    print(" Welcome to the Rule-Based AI Chatbot!")
    print("Type 'exit', 'quit', or 'bye' to stop the conversation.")
    print("=====================================================\n")

    while True:
        try:
            raw_input = input("You: ")
            clean_input = sanitize_input(raw_input)

            if clean_input in EXIT_COMMANDS:
                emit_response("Goodbye! Have a great day learning AI!")
                break

            if not clean_input:
                continue

            response = process_intent(clean_input)
            emit_response(response)

        except KeyboardInterrupt:
            print("\nChatbot: Goodbye! Have a great day!")
            break


if __name__ == "__main__":
    main()
