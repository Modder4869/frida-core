import lief
import sys
import random
import os

def replacer(input_file):
    print(f"[*] Patch frida-agent: {input_file}")
    random_name = "".join(random.sample("ABCDEFGHIJKLMNO", 5))
    print(f"[*] Patch `frida` to `{random_name}``")

    binary = lief.parse(input_file)

    if not binary:
        exit()

    for symbol in binary.symbols:
        if symbol.name == "frida_agent_main":
            print(symbol.name)
            symbol.name = "banana_main"

        if "frida" in symbol.name:
            symbol.name = symbol.name.replace("frida", random_name)
            print(symbol.name)

        if "FRIDA" in symbol.name:
            print(symbol.name)
            symbol.name = symbol.name.replace("FRIDA", random_name)

    binary.write(input_file)

    # gum-js-loop thread
    random_name = "".join(random.sample("abcdefghijklmn", 11))
    print(f"[*] Patch `gum-js-loop` to `{random_name}`")
    os.system(f"gsed -i s/gum-js-loop/{random_name}/g {input_file}")

    # gmain thread
    random_name = "".join(random.sample("abcdefghijklmn", 5))
    print(f"[*] Patch `gmain` to `{random_name}`")
    os.system(f"gsed -i s/gmain/{random_name}/g {input_file}")

replacer(sys.argv[1])