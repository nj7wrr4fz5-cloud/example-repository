from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Загружаем данные
with open("data.json") as f:
    data = json.load(f)

@app.route("/api/meta-prompt", methods=["POST"])
def generate_meta_prompt():
    request_data = request.json
    role = request_data.get("role")
    protocol = request_data.get("protocol")
    architecture = request_data.get("architecture")

    if not role or not protocol or not architecture:
        return jsonify({"error": "Role, protocol, and architecture are required."}), 400

    # Комбинируем метапромт
    tools = data["tools"].get(role, [])
    meta_prompt = f"Для роли '{role}', используйте протокол '{protocol}' и архитектуру '{architecture}'. Рекомендуемые инструменты: {', '.join(tools)}."
    
    return jsonify({"meta_prompt": meta_prompt})

if __name__ == "__main__":
    app.run(debug=True)