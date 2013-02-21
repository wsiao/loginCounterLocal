from django.db import models
import json

import unittest
import StringIO
#mport tests

#Error codes
SUCCESS = 1
ERR_BAD_CREDENTIALS = -1
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3 
ERR_BAD_PASSWORD = -4

# Create your models here.

class UsersModelManager(models.Manager):
    MAX_USERNAME_LENGTH = 128
    MAX_PASSWORD_LENGTH = 128
    def reset(self):
        allUsers = self.all().delete()
        #for user in allUsers:
        #    user.delete()
        return SUCCESS

    def TESTAPI_resetFixture(self):
        self.reset()
        return SUCCESS

    def TESTAPI_unitTests(self):
        '''buffer = StringIO.StringIO()
        suite = unittest.TestLoader().loadTestsFromTestCase(tests.TestUsers)
        result = unittest.TextTestRunner(stream = buffer, verbosity = 2).run(suite)
        
        rv = {"totalTests": result.testsRun, "nrFailed": len(result.failures), "output": buffer.getvalue()}
        return rv'''
        #return HttpResponse(json.dumps(rv), content_type = "application/json")
        #return SUCCESS

    def login(self, loginUser, loginPassword):
        if len(self.filter(user=loginUser)) == 0:
            return ERR_BAD_CREDENTIALS
        data = self.get(user=loginUser)
        if data.password != loginPassword:
            return ERR_BAD_CREDENTIALS
        data.count += 1
        data.save()
        return data.count
        
    def add(self, loginUser, loginPassword):
        if len(self.filter(user=loginUser)) > 0:
            return ERR_USER_EXISTS
        def valid_username(username):
            return username != "" and len(username) <= self.MAX_USERNAME_LENGTH
        def valid_password(password):
            return len(password) <= self.MAX_PASSWORD_LENGTH

        if not valid_username(loginUser):
            return ERR_BAD_USERNAME
        if not valid_password(loginPassword):
            return ERR_BAD_PASSWORD

        newUser = UsersModel(user=loginUser, password=loginPassword, count=1)
        newUser.save()
        return SUCCESS

class UsersModel(models.Model):
    #UsersModelManager = UsersModelManager()
    user = models.TextField()
    password = models.TextField()
    count = models.IntegerField()
    UsersModelManager = UsersModelManager()
    def __unicode__(self):
        return self.user
        
