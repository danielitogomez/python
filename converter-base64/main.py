import base64
from logo import logo
import sys


def encode_decode_str(input_option, str_encode_decode):
    if input_option == "encode":
        sample_string_bytes = str_encode_decode.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        print(f"Encoded string: {base64_string}")
    elif input_option == "decode":
        base64_bytes = str_encode_decode.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        print(f"Decoded string: {sample_string}")
    else:
        sys.exit("Give a valid option!!!\n 'encode/decode'")


print(logo)

should_end = False
while not should_end:
    input_option_arg = input("Type 'encode' into base64 or 'decode' from base64:\n")
    str_encode_decode_arg = input("Type 'whatever' to encode/decode to/from base64\n")

    encode_decode_str(input_option=input_option_arg, str_encode_decode=str_encode_decode_arg)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
    elif restart == "yes":
        should_end = False
    else:
        sys.exit("Give a valid option!!!\n 'yes' or 'no'")