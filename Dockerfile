FROM archlinux:base-devel

ARG MAKEFLAGS="-j12"

RUN pacman -Syu --noconfirm

RUN pacman -S --noconfirm git \
    python \
    python-aiohttp \
    python-opencv

RUN useradd -m -G wheel -s /bin/bash builder \
    && passwd -d builder

RUN echo 'builder ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

USER builder
WORKDIR /home/builder

RUN mkdir /home/builder/src
WORKDIR /home/builder/src

# Install dependencies
RUN mkdir /home/builder/src/python-dlib
COPY --chown=builder:builder python-dlib/ /home/builder/src/python-dlib

RUN git clone https://aur.archlinux.org/python-aioice.git \
    && git clone https://aur.archlinux.org/python-av-bin.git \
    && git clone https://aur.archlinux.org/google-crc32c.git \
    && git clone https://aur.archlinux.org/python-google-crc32c.git \
    && git clone https://aur.archlinux.org/python-pylibsrtp.git \
    && git clone https://aur.archlinux.org/python-face_recognition_models.git \
    && git clone https://aur.archlinux.org/python-aiortc.git \
    && git clone https://aur.archlinux.org/python-face_recognition.git

WORKDIR /home/builder/src/python-dlib
RUN makepkg -si --noconfirm --clean

WORKDIR /home/builder/src/python-aioice
RUN makepkg -si --noconfirm --clean

WORKDIR /home/builder/src/python-av-bin
RUN makepkg -si --noconfirm --clean

WORKDIR /home/builder/src/google-crc32c
RUN makepkg -si --noconfirm --clean

WORKDIR /home/builder/src/python-google-crc32c
RUN makepkg -si --noconfirm --clean

WORKDIR /home/builder/src/python-pylibsrtp
RUN makepkg -si --noconfirm --clean

WORKDIR /home/builder/src/python-face_recognition_models
RUN makepkg -si --noconfirm --clean

WORKDIR /home/builder/src/python-aiortc
RUN makepkg -si --noconfirm --clean

WORKDIR /home/builder/src/python-face_recognition
RUN makepkg -si --noconfirm --clean

# Remove leftovers
USER root
RUN pacman -S --noconfirm python-ifaddr
RUN pacman -Qdtq | pacman -Rns --noconfirm -
RUN userdel -r builder
