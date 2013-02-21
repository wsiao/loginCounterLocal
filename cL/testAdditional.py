import unittest
import os
import testLib

        
class TestLogin(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode  }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testloginSuccess(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 2)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 3)

    def testloginBadCredentials(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password1'} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user2', 'password' : 'password'} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)


class TestAdd(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode  }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1, errCode = testLib.RestTestCase.SUCCESS)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2', 'password' : 'password2'} )
        self.assertResponse(respData, count = 1, errCode = testLib.RestTestCase.SUCCESS)

    def testBadUsername(self):
        badUser = 'a'*129
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : badUser, 'password' : 'password'} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)

    def testBadPassword(self):
        badPassword = 'a'*129
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : badPassword} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD)

    def testEmptyUsername(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)


class TestResetFixture(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode  }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testReset(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = {} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.SUCCESS)
 
