import requests
import base64
import json

def classify_image(image_path):
    with open("credentials/clarifai_key.txt", "r") as f:
        API_KEY = f.read().strip()

    # ✅ Correct General model ID and version
    MODEL_ID = "aaa03c23b3724a16a56b629203edc62c"
    MODEL_VERSION_ID = "aa7f35c01e0642fda5cf400f543e7c40"

    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    headers = {
        "Authorization": f"Key {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": [
            {
                "data": {
                    "image": {
                        "base64": base64_image
                    }
                }
            }
        ]
    }

    # ✅ Use correct model version endpoint
    response = requests.post(
        f"https://api.clarifai.com/v2/models/{MODEL_ID}/versions/{MODEL_VERSION_ID}/outputs",
        headers=headers,
        json=data
    )

    response_json = response.json()

    # 🧪 Debug: print full response
    print("🔍 Clarifai Response:")
    print(json.dumps(response_json, indent=2))

    # ✅ Validate response
    if "outputs" not in response_json or not response_json["outputs"]:
        raise Exception("Clarifai API Error: No output received.")

    output_data = response_json["outputs"][0].get("data", {})
    concepts = output_data.get("concepts", [])

    if not concepts:
        raise Exception("Clarifai API Error: No labels found in the image.")

    labels = [concept["name"].lower() for concept in concepts]
    return labels
