from flask import Blueprint,jsonify,request
import json

mod=Blueprint('student_details',__name__,url_prefix='/student')

data=json.load(open('data.json'))

 #GET   http://127.0.0.1:5001/student/
@mod.route('/',methods=['GET'])
def getall():
    return 'List of students.'
#GET #http://127.0.0.1:5001/student/
# @mod.route('/<student_id>',methods=['GET'])
# def show(student_id):
#     print('Student_id:',student_id)
#     response={
#         'Student_id': student_id
#     }
#     return jsonify(response)

#http://127.0.0.1:5001/student/2
@mod.route('/<login_id>', methods=['GET'])
def fetch_one(login_id):
    person_detail=[x for x in data if x['login_id']==int(login_id)]
    #person_detail=[{login_id=1,fn='khushboo',ln='trivedi'}]
    person_detail=person_detail[0]if person_detail else{}
    return jsonify(person_detail)

@mod.route('/get_person/', methods=['GET'])
def fetch_one_permalink():
    login_id=request.args.get('login_id')
    person_detail=[x for x in data if x['login_id']==int(login_id)]
    person_detail=person_detail[0]if person_detail else{}
    # if person_detail:
    #     person_detail=person_detail[0]
    # else:
    #    person_detail= {}
    return jsonify(person_detail)


#POST #http://127.0.0.1:5001/student/create_user_json_req
@mod.route('/create_user_json_req',methods=['POST'])
def create_user_using_json_request():
    request_data=request.get_json()
    response = request_data
    new_user_id=data[-1]['login_id']+1
    response['login_id']=new_user_id
    data.append(response)
    json.dump(data,open('data.json','w'))
    return jsonify(response)

#POST #http://127.0.0.1:5001/student/create_user_form_req
@mod.route('/create_user_form_req',methods=['POST'])
def create_user_form_request():
    print('request_data:',request.form.to_dict())
    firstname=request.form.get('first_name')
    lastname = request.form.get('last_name')
    new_user_id=data[-1]['login_id']+1
    response={
        "login_id": new_user_id,
        "first_name": firstname,
        "last_name": lastname
    }
    data.append(response)
    json.dump(data,open('data.json','w'))
    return jsonify(response)

#PUT #http://127.0.0.1:5001/student/update_user/1/
@mod.route('/update_user/<login_id>',methods=['PUT'])
def update_user(login_id):
    request_data=request.get_json()
    print('request_data:',request_data)
    for d in data:
        if d['login_id']==int(login_id):
            if 'first_name' in request_data:
                d['first_name'] = request_data['first_name']
            if 'last_name'in request_data:
                d['last_name'] = request_data['last_name']
    json.dump(data,open('data.json','w'))
    return 'User details updated'

#delete #http://127.0.0.1:5001/student/delete_user/1/
@mod.route('/delete_user/<login_id>/', methods=['DELETE'])
def delete_user(login_id):
    for key,value in enumerate(data):
        if value['login_id']==int(login_id):
            del data[key]
    json.dump(data, open('data.json', 'w'))
    return 'User has beeen deleted'




