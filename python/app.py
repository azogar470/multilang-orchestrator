from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def get_info():
    return jsonify({
        "status": "success",
        "message": "Python Orchestrator Active",
        "pod_name": os.uname()[1],
        "container_ip": socket.gethostbyname(socket.gethostname()),
        "environment": "Kubernetes/KinD"
    })

if __name__ == '__main__':
    # It must run on 0.0.0.0 to be accessible inside the cluster
    app.run(host='0.0.0.0', port=5000)




    #things to be done:
      #rebuild the image 
        