import argparse

import gdown

parser = argparse.ArgumentParser(description='.')
parser.add_argument('-u', '--url')
parser.add_argument('-n', '--modelname', default="model.ckpt")

args = parser.parse_args()
if args.url:
    gdown.download(args.url, quiet=False, output=f"models/Stable-diffusion/{args.modelname}")
