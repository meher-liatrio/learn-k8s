from flask import Flask, request, jsonify
import jsonpatch
import base64

warden = Flask(__name__)

# Function to respond back to the Admission Controller
def k8s_response(allowed, uid, message, patch=None):
    response = {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "allowed": allowed,
            "uid": uid,
            "status": {
                "message": message
            }
        }
    }
    if patch:
        response["response"]["patchType"] = "JSONPatch"
        response["response"]["patch"] = base64.b64encode(patch).decode()
    return jsonify(response)

# POST route for Admission Controller
@warden.route('/validate', methods=['POST'])
def validating_webhook():
    request_info = request.get_json()
    uid = request_info["request"].get("uid")

    try:
        if request_info["request"]["kind"]["kind"] == "Pod" and request_info["request"]["namespace"] == "myapp":
            containers = request_info["request"]["object"]["spec"]["containers"]
            for container in containers:
                if not container["image"].startswith("myapp"):
                    return k8s_response(False, uid, "All containers must use an image with the 'myapp' prefix")
            return k8s_response(True, uid, "All containers use the 'myapp' image prefix")
        else:
            return k8s_response(False, uid, "Not in the 'myapp' namespace!")
    except Exception as e:
        return k8s_response(False, uid, "An error occurred during validation: {}".format(str(e)))

# POST route for Admission Controller
@warden.route("/mutate", methods=["POST"])
def mutating_webhook():
    request_info = request.get_json()
    uid = request_info["request"].get("uid")

    try:
        if request_info["request"]["kind"]["kind"] == "Pod" and request_info["request"]["namespace"] == "myapp":
            containers = request_info["request"]["object"]["spec"]["containers"]
            patch = []
            for i, container in enumerate(containers):
                if not container["image"].startswith("myapp"):
                    return k8s_response(False, uid, "All containers must use an image with the 'myapp' prefix")
                if container["image"].startswith("myapp") and container["image"] != "myapp:latest":
                    patch.append({
                        "op": "replace",
                        "path": "/spec/containers/{}/image".format(i),
                        "value": "myapp:latest"
                    })
            if patch:
                patch = jsonpatch.JsonPatch(patch).to_string().encode()
                return k8s_response(True, uid, "Image updated to 'myapp:latest'", patch)
            return k8s_response(True, uid, "All containers already using 'myapp:latest'")
        else:
            return k8s_response(False, uid, "Not in the 'myapp' namespace!")
    except Exception as e:
        return k8s_response(False, uid, "An error occurred during mutation: {}".format(str(e)))

if __name__ == '__main__':
    warden.run(ssl_context=('certs/wardencrt.pem', 'certs/wardenkey.pem'), debug=True, host='0.0.0.0')