from flask import Flask, render_template, request
import socket
import time

app=Flask(__name__)

def scan_ports(target, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        target=request.form['target']
        start_port=int(request.form['start_port'])
        end_port=int(request.form['end_port'])
        open_ports=scan_ports(target, start_port, end_port)
        return render_template('result.html', target=target, open_ports=open_ports)
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True, host='192.168.1.71', port=5000)