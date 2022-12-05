import argparse

import gdown

parser = argparse.ArgumentParser(description='.')
parser.add_argument('-u', '--url')

args = parser.parse_args()
if args.url:
    gdown.download(args.url, quiet=False, output="models/Stable-diffusion/model.ckpt")
