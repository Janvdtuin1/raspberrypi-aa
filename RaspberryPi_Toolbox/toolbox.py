#!/usr/bin/env python
#
#
#

class UnknownRevision(Exception):
    pass

class Toolbox:
    '''Set of utilities to exercise the power of the Raspberry Pi'''
    def __init__(self):
        pass
    
    def get_revision(self):
        'Return Model and Revision of the current board'
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if 'Revision' in line:
                    rev = line.split(':')[1].strip()
                    #print rev
                    # Data from: http://raspberryalphaomega.org.uk/?p=428
                    if rev == '0002'
                    elif rev == '0003':
                        return ('Model B', 'Revision 1.0+', '256MB')
                    elif rev == '0004' or rev == '0005' or rev == '0006':
                        return ('Model B', 'Revision 2.0', '256MB')
                    elif rev == '0007' or rev == '0008' or rev == '0009':
                        return ('Model A', 'Revision 1.0', '256MB')
                    elif rev == '000d' or rev == '000e' or rev == '000f':
                        return ('Model B', 'Revision 2.0' '512MB')
                    else:
                        raise UnknownRevision('Revision is: ' + rev)
                
 


if __name__ == '__main__':
    t = Toolbox()
    print ', '.join(t.get_revision())