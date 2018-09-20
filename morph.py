import argparse
import importlib

def signals():
    print('''
            __________              ____  __    __
           /  __  __  \____  ____  / __ \/ /   / /
          /  / / / /  / __ \/  __\/ /_/ / /___/ /
         /  / / / /  / /_/ /  /  /  ___/  ___  /
         \_/  \/  \_/\____/\_/   \_/   \_/  /_/

  By Walkerfuz of Taurus Security(https://github.com/walkerfuz)
                                          Morph - Version 0.4.0
    ''')

def morph(fuzzer, generator, template):

    fuzzer = importlib.import_module("fuzzers.{}".format(fuzzer))
    fuzzer = fuzzer.Fuzzer(generator, template)
    fuzzer.run()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fuzzer', required=True, help="which fuzzer to fuzz.")
    parser.add_argument('-g', '--generator', required=True, help="generator with templates.")
    parser.add_argument('-t', '--template', required=True, help="which template generator to use.")
    args = parser.parse_args()
    signals()
    morph(args.fuzzer, args.generator, args.template)

