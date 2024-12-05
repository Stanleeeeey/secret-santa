FROM python:3.13
ADD main.py .
RUN pip install req.txt
CMD [“python”, “./main.py”] 