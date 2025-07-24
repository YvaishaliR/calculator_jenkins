import json
import calculator

def handler(event, context):
    op = event.get("operation")
    a = event.get("a")
    b = event.get("b")

    result = None
    if op == "add":
        result = calculator.add(a, b)
    elif op == "subtract":
        result = calculator.subtract(a, b)
    elif op == "multiply":
        result = calculator.multiply(a, b)

    return {
        "statusCode": 200,
        "body": json.dumps({"result": result})
    }
