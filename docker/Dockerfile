FROM python:3.8
WORKDIR /code
RUN pip install amazon-textract-textractor amazon-textract-prettyprinter
COPY main.py /code/main.py
CMD [ "python", "/code/main.py" ] 
