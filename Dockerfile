FROM python:3.10-slim

WORKDIR /app

COPY . .

CMD ["python", "-m", "unittest", "test_calculator.py"]
