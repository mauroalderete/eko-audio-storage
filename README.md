# Eko Audio Storage <!-- omit in toc -->

<h4 align="center">This microservice, built using Flask, stores audio data received via a REST API. It validates the received data, creates session folders, and saves the audio data as WAV files.
</h4>

&nbsp;

<div align="center">

<a href="./LICENSE">
	<img alt="License: MIT" src="https://img.shields.io/badge/License-Private-yellow.svg">
</a>
<a href="./CODE_OF_CONDUCT.md">
	<img alt="Contributor covenant: 2.1" src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg">
</a>
<a href="https://semver.org/">
	<img alt="Semantic Versioning: 2.0.0" src="https://img.shields.io/badge/Semantic--Versioning-2.0.0-a05f79?logo=semantic-release&logoColor=f97ff0">
</a>

[![Tests](https://github.com/mauroalderete/eko-audio-storage/actions/workflows/tests.yml/badge.svg)](https://github.com/mauroalderete/eko-audio-storage/actions/workflows/tests.yml)

<a href="./issues/new/choose">Report Bug</a>
·
<a href="./issues/new/choose">Request Feature</a>

<a href="https://twitter.com/intent/tweet?text=👋%20Check%20this%20amazing%20repo%20https://github.com/mauroalderete/eko-audio-storage,%20created%20by%20@_mauroalderete%0A%0A%23DEVCommunity%20%23100DaysOfCode%20%23Golang%20%23gcode">
	<img src="https://img.shields.io/twitter/url?label=Share%20on%20Twitter&style=social&url=https%3A%2F%2Fgithub.com%2Fatapas%2Fmodel-repo">
</a>

</div>

- [Docker](#docker)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Microservice with Docker](#running-the-microservice-with-docker)
  - [Docker Compose](#docker-compose)
- [Source](#source)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Testing](#testing)
- [Endpoints](#endpoints)
  - [`/store` (POST)](#store-post)
- [License](#license)

# Docker

## Building the Docker Image

To build the Docker image, run the following command in the project directory:

```bash
docker build -t microservice_audio_storage .
```

## Running the Microservice with Docker

To run the microservice using Docker, execute the following command:

```bash
docker run -p 5000:5000 -v /path/to/your/audio_sessions:/app/audio_sessions --name audio_storage microservice_audio_storage
```

This command maps the host's port 5000 to the container's port 5000 and creates a volume mapping from the host's `/path/to/your/audio_sessions` to the container's `/app/audio_sessions`. The audio sessions stored in the container will be accessible on the host machine.

The session folders inside the volume are organized by session ID, with each folder containing a sequence of audio fragments.

## Docker Compose

To run the microservice using Docker Compose, create a `docker-compose.yml` file with the following content:

```yaml
version: "3.9"

services:
  microservice_audio_storage:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - /path/to/your/audio_sessions:/app/audio_sessions
```

# Source

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mauroalderete/microservice_audio_storage.git
```
2. Change directory to the cloned repository:

```bash
cd microservice_audio_storage
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the application using the following command:

```bash
python microservice_audio_storage.py
```

The microservice will be available on http://localhost:5000.

## Testing

To run tests, make sure you have pytest and pytest-cov installed (included in requirements.txt). Run the tests with the following command:

```bash
pytest --cov=microservice_audio_storage --cov-report html test_microservice_audio_storage.py
```

To generate a coverage report in HTML format, run:

```bash
pytest --cov=microservice_audio_storage --cov-report html tests/
```

This will create an htmlcov directory with an index.html file. Open this file in a web browser to see the coverage report, which will show the lines of code covered by tests and the lines that still need to be tested.

# Endpoints
## `/store` (POST)

This endpoint accepts a JSON object containing audio metadata and audio data. The audio files will be stored in the audio_sessions folder, organized by session ID.

```json
{
  "metadata": {
    "session": {
      "id": "string"
    },
    "audio": {
      "channels": "integer",
      "rate": "integer",
      "sample_size": "integer"
    }
  },
  "data": [
    "integer"
  ]
}
```

- `metadata`: Contains additional information about the session and the audio.
  - `session`: Contains information about the recording session.
    - `id`: A string representing the unique identifier for the recording session. It must contain only alphanumeric characters and hyphens.
  - `audio`: Contains information about the audio configuration.
    - `channels`: An integer representing the number of audio channels. For example, 1 for mono and 2 for stereo.
    - `rate`: An integer representing the audio sampling rate in Hertz (Hz). For example, 44100 Hz is a commonly used sampling rate in audio files.
    - `sample_size`: An integer representing the sample size in bytes. For example, 2 for 16-bit samples.
- `data`: An array of integers representing the audio data in sample format. Each integer corresponds to an audio sample and must be a 16-bit value.

The microservice validates the structure and content of the received JSON object before processing and storing the audio data. If the JSON object does not comply with the required schema, the microservice returns an error.

Example JSON object:

```json
{
    "metadata": {
        "session": {
            "id": "example-session-id"
        },
        "audio": {
            "channels": 1,
            "rate": 16000,
            "sample_size": 160
        }
    },
    "data": [0, 0, 0, 1, 2, 3]
}
```

# License

This project is private.