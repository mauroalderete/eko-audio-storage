# Eko Audio Storage

<h4 align="center">This microservice allows you to store audio files in a structured manner, with each audio file organized by session ID. It is built using Flask, a lightweight web framework for Python.</h4>

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
[![CodeQL](https://github.com/mauroalderete/eko-audio-storage/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/mauroalderete/eko-audio-storage/actions/workflows/codeql-analysis.yml)

<a href="./issues/new/choose">Report Bug</a>
·
<a href="./issues/new/choose">Request Feature</a>

<a href="https://twitter.com/intent/tweet?text=👋%20Check%20this%20amazing%20repo%20https://github.com/mauroalderete/eko-audio-storage,%20created%20by%20@_mauroalderete%0A%0A%23DEVCommunity%20%23100DaysOfCode%20%23Golang%20%23gcode">
	<img src="https://img.shields.io/twitter/url?label=Share%20on%20Twitter&style=social&url=https%3A%2F%2Fgithub.com%2Fatapas%2Fmodel-repo">
</a>

</div>

# Installation

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

# Usage

Run the application using the following command:

```bash
python microservice_audio_storage.py
```

The microservice will be available on http://localhost:5000.

# Endpoints
## `/store` (POST)

This endpoint accepts a JSON object containing audio metadata and audio data. The audio files will be stored in the audio_sessions folder, organized by session ID.

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

# Testing

To run tests, make sure you have pytest and pytest-cov installed (included in requirements.txt). Run the tests with the following command:

```bash
pytest --cov=microservice_audio_storage tests/
```

To generate a coverage report in HTML format, run:

```bash
pytest --cov=microservice_audio_storage --cov-report html tests/
```

This will create an htmlcov directory with an index.html file. Open this file in a web browser to see the coverage report, which will show the lines of code covered by tests and the lines that still need to be tested.

# License

This project is private.