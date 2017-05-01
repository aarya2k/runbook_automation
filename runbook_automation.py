import os
import io
import sys
import itertools
from flask import Flask, render_template, request, make_response, jsonify, url_for, json
from pprint import pprint
from flask import abort
import shutil
from flask_httpauth import HTTPBasicAuth
from db_backup import Mininons_Db
import subprocess
app = Flask(__name__)
auth = HTTPBasicAuth()

def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)

# Get username and password from HTTP HEADER
@auth.verify_password
def get_creds(username=None, password=None):
    ''' Get Username & Password '''
    global_username = username
    global_password = password
    return global_username, global_password


# @auth.login_required
def verify_pw(username, password):
    if not username or not password:
        return False
    if username == 'admin' and password == 'admin':
        return True

#to create a directory
def mkdir(newpath):
    ''' make dir in windows'''
    if not os.path.exists(newpath):
        os.makedirs(newpath)

#to create files
def createfile(newpath):
    ''' cat dir in windows'''
    if not os.path.exists(newpath):
        with io.FileIO(newpath, "w") as file:
            file.write("Hello!, Please write this statement in the file")

#to copy files
def copyFile(newpath,despath):
    ''' copy dir in windows'''
    if os.path.exists(newpath):
        src = os.listdir(newpath)
        pprint(src)
        try:
            for srcpath in src:
                if srcpath.endswith(".txt"):
                    fullPath = newpath + "\\" + srcpath
                    print "Full Path" , fullPath , "\n"
                    print "Destination =" , despath
                    shutil.copy2(fullPath, despath)
        except Exception as e:
            pprint(e.message)
            print "Move Failed" + str(e.message)

#to cat files
def catFile(newpath):
    if os.path.exists(newpath):
        f = open(newpath, "r")
        text = f.read()
        pprint(text)
        f.close()

#to move files
def moveFile(newpath,despath):
    ''' copy dir in windows'''
    if os.path.exists(newpath):
        src = os.listdir(newpath)
        pprint(src)
        try:
            for srcpath in src:
                if srcpath.endswith(".txt"):
                    fullPath = newpath + "\\" + srcpath
                    print "Full Path" , fullPath , "\n"
                    print "Destination =" , despath
                    shutil.move(fullPath, despath)
        except Exception as e:
            pprint(e.message)
            print "Move Failed" + str(e.message)

#to remove dir
def removeDir(newpath):
    if os.path.exists(newpath):
        os.rmdir(newpath)

#to remove file
def removeFile(newpath):
    files = os.listdir(newpath)
    for file in files:
        if file.endswith(".txt"):
            os.remove(os.path.join(newpath,file))

#to pipe commands
def pipeCmd(newpath):
    file = open(newpath, 'w')
    variations = itertools.product('xyz', repeat=3)
    for variations in variations:
        variation_string = ""
        for letter in variations:
            variation_string += letter
        file.write(variation_string)
    file.close()


# Error code for unauthorized user
def not_found():
    response = jsonify({'code': 401, 'message': 'User is not authorized'})
    response.status_code = 401
    return response


@app.route('/master/api/run', methods=["POST"])
def minnions():
    print "UserName", request.authorization.username, 'Password', request.authorization.password
    if not verify_pw(request.authorization.username, request.authorization.password):
        return not_found()

    msg = None
    json_request = request.json
    monion = Mininons_Db()
    pprint(json_request)
    monion._hostname = json_request['hostname']
    monion._instance = json_request['instance']
    monion._location = json_request['location']
    monion._os = json_request['os']
    monion._port = json_request['port']
    monion._user = json_request['user']
    #command = json_request['command']
    #path = json_request['path']
    commands = json_request['action']
    monion.insert()
    status = []
    for act in commands:
        cmd = act['command']
        path = act['path']
        if cmd == 'mkdir':
            mkdir(path)
            msg = 'Folder created successfully'
            status.append(msg)

        if cmd == 'createfile':
            createfile(path)
            msg = 'Create file is done'
            status.append(msg)

        if cmd == 'copyfile':
            copyFile(path,despath=act['despath'])
            msg = 'Copy file is done'
            status.append(msg)

        if cmd == 'catfile':
            catFile(path)
            pprint(catFile)
            msg = 'Cat file is done'
            status.append(msg)

        if cmd == 'pipefile':
            pipeFile(path)
            msg = 'pipe file is done'
            status.append(msg)

        if cmd == 'movefile':
            moveFile(path,despath=act['despath'])
            msg = 'Move file is done'
            status.append(msg)

        if cmd == 'removedir':
            removeDir(path)
            msg = 'Remove directory is done'
            status.append(msg)

        if cmd == 'removefile':
            removeFile(path)
            msg = 'Remove file is done'
            status.append(msg)

        if cmd == 'pipecmd':
            pipeCmd(path)
            msg = 'Pipe command is done'
            status.append(msg)

    pprint(commands)
    final_msg = ""
    for msg in status:
        final_msg += msg

    # call to hostname, makedir
    msg = 'No Operations Performerd'
    #if path:
    #    mkdir(path)
    #    msg = 'Created Successfull.'

    return jsonify({"message": "record instered successfully.", "Status":"Code :" +final_msg })


@app.route('/master/api/list_server/<int:server_port>', methods=['GET'])
def get_task(server_port):
    print "UserName", request.authorization.username, 'Password', request.authorization.password
    if not verify_pw(request.authorization.username, request.authorization.password):
        return not_found()
    pprint(server_port)
    monion = Mininons_Db()
    monion.fetchport()
    pprint(monion)
    return jsonify(data=[c.json_dump() for c in monion])


@app.route('/master/api/add_server', methods=["POST"])
def db_tasks():
    print "UserName", request.authorization.username, 'Password', request.authorization.password
    if not verify_pw(request.authorization.username, request.authorization.password):
        return not_found()
    json_request = request.json


@app.route('/')
def index():
    # Render template
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
