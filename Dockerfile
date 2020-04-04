FROM continuumio/miniconda:latest

WORKDIR /fris_or_not/

COPY environment.yml ./
COPY src/ ./
COPY model/export.pkl ./model/export.pkl
COPY boot.sh ./

RUN chmod +x boot.sh

RUN conda env create -f environment.yml -q

RUN echo "source activate fris_or_not" > ~/.bashrc
ENV PATH /opt/conda/envs/fris_or_not/bin:$PATH

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
