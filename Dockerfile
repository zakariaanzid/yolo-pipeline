FROM python:3.9

WORKDIR /app

COPY manifests/pipeline.yaml .
COPY scripts/kbf-run.py . 
RUN pip install kfp

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    curl vim iputils-ping net-tools \
 #   && pip install --no-cache-dir \
  #  ipython rich \
   #  && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["python","kbf-run.py"]


