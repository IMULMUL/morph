import argparse
import importlib
import json

def signals():
    print('''
            __________              ____  __    __
           /  __  __  \____  ____  / __ \/ /   / /
          /  / / / /  / __ \/  __\/ /_/ / /___/ /
         /  / / / /  / /_/ /  /  /  ___/  ___  /
         \_/  \/  \_/\____/\_/   \_/   \_/  /_/

  By Walkerfuz of Taurus Security(https://github.com/walkerfuz)
                                          Morph - Version 0.4.3
    ''')

def morph(morpit):
    with open(morpit) as f:
        morpit = json.load(f)

    fuzzer = importlib.import_module(morpit["fuzzer"])
    fuzzer = fuzzer.Fuzzer(morpit["argument"])
    fuzzer.run()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('morpit', help="morpit json file.")
    args = parser.parse_args()
    signals()
    morph(args.morpit)

