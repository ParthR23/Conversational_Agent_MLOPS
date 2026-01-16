def conversations():
    return [
        {"user": "Hello", "expected_route": "knowledge"},
        {"user": "What’s the weather?", "expected_route": "knowledge"},
        {"user": "Bye", "expected_route": "knowledge"}
    ]