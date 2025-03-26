FROM joyzoursky/python-chromedriver:latest

WORKDIR  global_widgets

ADD requirements.in .

RUN pip install -r requirements.in

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/global_widgets/"

ENTRYPOINT ["python", "src/check_site.py"]