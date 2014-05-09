import nist5_hash
import weakref
import binascii
import StringIO

from binascii import hexlify, unhexlify

teststart = '010000000000000000000000000000000000000000000000000000000000000000000000d122dfd3991718af99d85f63f2011b3e43d91587cb719d5e15b82ca85a4f1998f0981453f0ff0f1ee6590300'
testbin = unhexlify(teststart)
hash_bin = nist5_hash.getPoWHash(testbin)

hash_hex = hexlify(hash_bin[::-1])
print "%s" % hash_hex
assert hash_hex == '00000578c9c073fc55fce4da9fa03339aacfb5f4f274e4c4f6c0f1d99174a860' 
