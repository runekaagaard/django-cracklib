#!/usr/bin/env python
#
#  Cracklib using ctypes

import os

def FascistCheck(passwd, username = None):
	from ctypes import CDLL, c_char_p
	cracklib = CDLL('/usr/lib/libcrack.so.2')
	cracklib.FascistCheck.argtypes = [c_char_p, c_char_p]
	cracklib.FascistCheck.restype = c_char_p

	dictionary = '/usr/lib/cracklib_dict'
	if not os.path.exists(dictionary + '.pwd'):
		raise ValueError('Unable to find dictionary file: "%s"' % dictionary)

	ret = cracklib.FascistCheck(passwd, dictionary)
	if ret is not None: return ret

	#  check password against username
	if username is not None:
		if (username.lower() in passwd.lower()
				or ''.join(reversed(username.lower())) in passwd.lower()):
			return 'it is based on your username' 
		usernamechars = {}
		for c in username.lower(): usernamechars[c] = 1
		usernamechars = ''.join(usernamechars.keys())
		passwdchars = {}
		for c in passwd.lower(): passwdchars[c] = 1
		passwdchars = ''.join([ x for x in passwdchars.keys()
				if x not in usernamechars ])
		if ((len(usernamechars) < 5 and len(passwdchars) < 4)
				or (len(usernamechars) < 10 and len(passwdchars) < 2)):
			return 'it is too similar to your username'

	return None

######################
if __name__ == '__main__':
	import sys, unittest
	if not 'test' in sys.argv:
		sys.stderr.write('ERROR: You need to run with the "test" argument to '
				'run test suite\n')
		sys.exit(1)

	print 'test'
	class testBase(unittest.TestCase):
		def test_passwords(self):
			self.assertEqual(FascistCheck('jafo1234', 'jafo'),
				'it is based on your username')
			self.assertEqual(FascistCheck('jafo1234', 'ofaj'),
				'it is based on your username')
			self.assertEqual(FascistCheck('myjafo123', 'jafo'),
				'it is based on your username')
			self.assertEqual(FascistCheck('myofaj123', 'jafo'),
				'it is based on your username')
			self.assertEqual(FascistCheck('jxayfoxo', 'jafo'),
				'it is too similar to your username')
			self.assertEqual(FascistCheck('jXAyFOxo', 'jafo'),
				'it is too similar to your username')
			self.assertEqual(FascistCheck('jafo'),
				'it is too short')
			self.assertEqual(FascistCheck('jaf'),
				'it is WAY too short')
			self.assertEqual(FascistCheck('secret'),
				'it is based on a dictionary word')
			self.assertEqual(FascistCheck('cretse'),
				'it is based on a dictionary word')
			self.assertEqual(FascistCheck('jxayfoxo'), None)

	suite = unittest.TestLoader().loadTestsFromTestCase(testBase)
	unittest.TextTestRunner(verbosity=2).run(suite)
