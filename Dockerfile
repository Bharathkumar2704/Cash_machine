FROM python:3.9.12
COPY requirements.txt .
ADD Cash_Machine.py .
COPY input.txt .
CMD ["python" , "./Cash_Machine.py"]