ARG PYTHON_VERSION=3.8.9

FROM python:${PYTHON_VERSION}

WORKDIR /usr/ahu/code/
RUN python --version | tee -a start.log
COPY ./ ./restful-api-practice
WORKDIR /usr/ahu/code/restful-api-practice
RUN pip install -r requirement.txt
RUN flask --version | tee -a start.log
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]