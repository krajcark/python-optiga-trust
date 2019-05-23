# ============================================================================
# The MIT License
# 
# Copyright (c) 2018 Infineon Technologies AG
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE
# ============================================================================

from enum import Enum
from collections import namedtuple

__all__ = ['Rng', 'KeyUsage', 'ObjectId', 'KeyId', 'KeyUsage']

class Rng(Enum):
	# OPTIGA Trust RNG Enumeration
	TRNG = 0
	DRNG = 1
	
class Curves(Enum):
	NIST_P_256 = 3
	NIST_P_384 = 4


class KeyUsage(Enum):
	# This enables the private key for the signature generation as part of authentication commands
	AUTHENTICATION = 0x01
	# This enables the private key for the signature generation
	SIGN = 0x10
	# This enables the private key for key agreement (e.g. ecdh operations)
	KEY_AGREEMENT = 0x20


class ObjectId(Enum):
	# Default Infineon Certificate Slot
	IFX_CERT = 0xE0E0
	# User defined certificate Slot 1
	USER_CERT_1 = 0xE0E1
	# User defined certificate Slot 2
	USER_CERT_2 = 0xE0E2
	# User defined certificate Slot 3
	USER_CERT_3 = 0xE0E3
	# An Object OID to store by default a public key out of newly generated keypair
	DEF_PUBKEY = 0xF1D0


class KeyId(Enum):
	# Key from key store
	IFX_PRIVKEY = 0xE0F0
	# Key from key store
	USER_PRIVKEY_1 = 0xE0F1
	# Key from key store
	USER_PRIVKEY_2 = 0xE0F2
	# Key from key store
	USER_PRIVKEY_3 = 0xE0F3

	# Key from Session context id 1
	SESSION_ID_1 = 0xE100
	# Key from Session context id 2
	SESSION_ID_2 = 0xE101
	# Key from Session context id 3
	SESSION_ID_3 = 0xE102
	# Key from Session context id 4
	SESSION_ID_4 = 0xE103

	@classmethod
	def has_value(cls, value):
		return any(value == item.value for item in cls)


UID = namedtuple("_Curve", "cim_id platform_id model_id rommask_id chip_type batch_num x_coord y_coord fw_id fw_build")