import sys

import argparse
from bitstring import ConstBitStream, BitArray


def cmdline_args():
    # Make parser object
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    p.add_argument("input",
        help="input file")
        
    p.add_argument("reference",
        help="reference/key file")
        
    p.add_argument("output",
        help="output file name")
        
    return(p.parse_args()) 


def v_encrypt(args):
    print("/nStarting on file: {}".format(args.input))
    print("Output: {}".format(args.output))
    print("Key: {}".format(args.reference))
    
    bits_in = ConstBitStream(filename = args.input)
    bits_ref = ConstBitStream(filename = args.reference)
    
    if len(bits_ref) < len(bits_in):
        while len(bits_ref) < len(bits_in):
            bits_ref += bits_ref
    
    if len(bits_ref) > len(bits_in):
        bits_ref = bits_ref[0:len(bits_in)]

    bits_out = (bits_in ^ bits_ref) #xor
    
    print(bits_in.bin[0:8])
    print(bits_ref.bin[0:8])
    print(bits_out.bin[0:8])
    
    with open(args.output, 'wb') as f:
        f.write(bits_out.bytes) 
    
    
if __name__ == '__main__':
    args = cmdline_args()
    v_encrypt(args)


