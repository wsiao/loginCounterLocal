from cL.models import UsersModel
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import StringIO
import cL.unitTests
import unittest
from django.shortcuts import render_to_response
from django.template import RequestContext


#Error codes
SUCCESS = 1
ERR_BAD_CREDENTIALS = -1
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3 
ERR_BAD_PASSWORD = -4

@csrf_exempt
def frontPage(request):
    return render_to_response('frontEnd.html',{},context_instance=RequestContext(request))


@csrf_exempt
def login(request):
    requestData = json.loads(request.body)
    username = requestData["user"]
    password = requestData["password"]
    rval = UsersModel.UsersModelManager.login(username,password)
    if rval < 0:
        resp = {"errCode" : rval}
    else:
        resp = {"errCode" : SUCCESS, "count" : rval}
    return HttpResponse(json.dumps(resp), content_type = "application/json")

@csrf_exempt
def add(request):
    requestData = json.loads(request.body)
    username = requestData["user"]
    password = requestData["password"]
    rval = UsersModel.UsersModelManager.add(username,password)
    if rval < 0:
        resp = {"errCode" : rval}
    else:
        resp = {"errCode" : SUCCESS, "count" : rval}
    return HttpResponse(json.dumps(resp), content_type = "application/json")

@csrf_exempt
def resetFixture(request):
    rval = UsersModel.UsersModelManager.TESTAPI_resetFixture()
    resp = {"errCode" : rval}
    return HttpResponse(json.dumps(resp), content_type = "application/json")

@csrf_exempt
def unitTests(request):
    buffer = StringIO.StringIO()
    suite = unittest.TestLoader().loadTestsFromTestCase(cL.unitTests.TestUsers)
    result = unittest.TextTestRunner(stream = buffer, verbosity = 2).run(suite)
    
    rv = {"totalTests": result.testsRun, "nrFailed": len(result.failures), "output": buffer.getvalue()}
    #resp = UsersModel.UsersModelManager.TESTAPI_unitTests()
    return HttpResponse(json.dumps(rv), content_type = "application/json")
    #return UsersModel.UsersModelManager.TESTAPI_unitTests
