FROM ubuntu:16.04
MAINTAINER Kevin Zhang <kevz@mit.edu>

# Build POV-Ray (based on bradleybossard/docker-povray)
RUN apt-get update
RUN apt-get install -y git \
                       zip \
                       build-essential \
                       libboost-dev \
                       zlib1g-dev \
                       libpng12-dev \
                       libjpeg8-dev \
                       libtiff5-dev \
                       autoconf \
                       libopenexr-dev \
                       libboost-all-dev
RUN git clone https://github.com/POV-Ray/povray.git
WORKDIR /povray/unix
RUN ./prebuild.sh
WORKDIR /povray
RUN ./configure COMPILED_BY="Kevin Zhang <kevz@mit.edu>"
RUN make
RUN make install

# Install Anaconda3 (based on continuumio/anaconda)
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh
ENV PATH /opt/conda/bin:$PATH

# Install things I like
RUN mkdir /opt/conda/var/lib/
RUN mkdir /opt/conda/var/lib/dbus/
RUN apt-get update && apt-get install -y nano libav-tools
RUN pip install tensorflow
RUN pip install keras
RUN pip install tqdm

# Install konics
COPY ./konics /konics
ENV PYTHONPATH /:$PYTHONPATH

# Run.
WORKDIR /
CMD sh -c "jupyter notebook --ip='*' --no-browser"
