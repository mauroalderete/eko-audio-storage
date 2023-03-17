# microservice_audio_storage.py
from flask import Flask, request, jsonify
import os
import datetime
import wave
import re
import jsonschema
from jsonschema import validate

app = Flask(__name__)
UPLOAD_FOLDER = "audio_sessions"

audio_schema = {
    "type": "object",
    "properties": {
        "metadata": {
            "type": "object",
            "properties": {
                "session": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "pattern": r"^[\w-]+$"},
                    },
                    "required": ["id"],
                },
                "audio": {
                    "type": "object",
                    "properties": {
                        "channels": {"type": "integer"},
                        "rate": {"type": "integer"},
                        "sample_size": {"type": "integer"},
                    },
                    "required": ["channels", "rate", "sample_size"],
                },
            },
            "required": ["session", "audio"],
        },
        "data": {
            "type": "array",
        },
    },
    "required": ["metadata", "data"],
}


@app.route("/store", methods=["POST"])
def store():
    try:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        data = request.json

        validate(instance=data, schema=audio_schema)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        session_folder = os.path.join(
            UPLOAD_FOLDER, data["metadata"]["session"]["id"])
        if not os.path.exists(session_folder):
            os.makedirs(session_folder)

        filename = f"{timestamp}.wav"
        filepath = os.path.join(session_folder, filename)

        save_file(
            filename=filepath,
            audio=data)

        return jsonify({"status": "success", "message": "Audio stored", "file": filepath})

    except jsonschema.ValidationError as e:
        return jsonify({"error": "The data provided doesn't correspond to required scheme: " + str(e)}), 400

    except Exception as e:
        return jsonify({"error": "Internal server error: " + str(e)}), 500


def save_file(filename, audio):
    wf = wave.open(filename, "wb")

    # Config
    wf.setnchannels(audio["metadata"]["audio"]["channels"])
    wf.setsampwidth(audio["metadata"]["audio"]["sample_size"])
    wf.setframerate(audio["metadata"]["audio"]["rate"])

    # Get bytes from int list
    audio_bytes = [i.to_bytes(2, 'little', signed=True) for i in audio["data"]]

    wf.writeframes(b"".join(audio_bytes))
    wf.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
