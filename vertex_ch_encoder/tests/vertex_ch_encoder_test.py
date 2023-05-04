import pytest
from vertex_ch_encoder.lib.vertex_ch_encoder import EncoderSTL, DecoderSTL, base2, base3


# Test text. infiltrating secret.txt into sphere stl file
def test_encode_decode_text_base_2():
    encoder = EncoderSTL("test_objects/base3/text/original_sphere.STL", False)  # carrier's filepath
    encoder.EncodeFileInSTL("test_objects/base2/text/secret.txt",  # secret's path
                            "test_objects/base2/text/encoded/encoded_sphere.STL",
                            base2)  # path to save the carrier with secret

    decoder = DecoderSTL(
        "test_objects/base2/text/encoded/encoded_sphere.STL", False)  # carrier's with secret filepath
    decoder.DecodeFileFromSTL(
        "test_objects/base2/text/decoded/decoded_secret.txt", base2)  # path to save the decoded secret

    secret = open("test_objects/base2/text/decoded/decoded_secret.txt", "r").read()

    assert secret == "This is the secret message!"


# Test image. infiltrating elephant_secret.jpeg into bunny stl file
def test_encode_decode_image_base_2():
    encoder = EncoderSTL("test_objects/base2/image/bunny.STL", False)  # carrier's filepath
    encoder.EncodeFileInSTL("test_objects/base2/image/elephant_secret.jpeg",  # secret's path
                            "test_objects/base2/image/encoded/encoded_bunny.STL",
                            base2)  # path to save the carrier with secret

    decoder = DecoderSTL("test_objects/base2/image/encoded/encoded_bunny.STL", False)  # carrier's with secret filepath
    decoder.DecodeFileFromSTL("test_objects/base2/image/decoded/decoded_secret.jpeg",
                              base2)  # path to save the decoded secret

    orig_secret = open("test_objects/base2/image/elephant_secret.jpeg", "rb").read()

    decoded_secret = open("test_objects/base2/image/decoded/decoded_secret.jpeg", "rb").read()

    assert orig_secret == decoded_secret


# Test image. infiltrating elephant_secret.jpeg into bunny stl file
def test_encode_decode_bitmap_base_2():
    encoder = EncoderSTL("test_objects/base2/bitmap/bunny.STL", False)  # carrier's filepath
    encoder.EncodeFileInSTL("test_objects/base2/bitmap/secret.bmp",  # secret's path
                            "test_objects/base2/bitmap/encoded/encoded_bunny.STL",
                            base2)  # path to save the carrier with secret

    decoder = DecoderSTL(
        "test_objects/base2/bitmap/encoded/encoded_bunny.STL", False)  # carrier's with secret filepath
    decoder.DecodeFileFromSTL(
        "test_objects/base2/bitmap/decoded/decoded_secret.bmp", base2)  # path to save the decoded secret

    orig_secret = open("test_objects/base2/bitmap/secret.bmp", "rb").read()

    decoded_secret = open("test_objects/base2/bitmap/decoded/decoded_secret.bmp", "rb").read()

    assert orig_secret == decoded_secret


# Test text base 3. infiltrating secret.txt into sphere stl file
def test_encode_decode_text_base_3():
    encoder = EncoderSTL("test_objects/base3/text/original_sphere.STL", False)  # carrier's filepath
    encoder.EncodeFileInSTL("test_objects/base3/text/secret.txt",  # secret's path
                            "test_objects/base3/text/encoded/encoded_sphere.STL",
                            base3)  # path to save the carrier with secret

    decoder = DecoderSTL(
        "test_objects/base3/text/encoded/encoded_sphere.STL", False)  # carrier's with secret filepath
    decoder.DecodeFileFromSTL(
        "test_objects/base3/text/decoded/decoded_secret.txt", base3)  # path to save the decoded secret

    orig_secret = open("test_objects/base3/text/secret.txt", "r").read()

    decoded_secret = open("test_objects/base3/text/decoded/decoded_secret.txt", "r").read()

    assert orig_secret == decoded_secret


# Test image base 3. infiltrating elephant_secret.jpeg into bunny stl file
def test_encode_decode_bitmap_base_3():
    encoder = EncoderSTL("test_objects/base3/bitmap/bunny.STL", False)  # carrier's filepath
    encoder.EncodeFileInSTL("test_objects/base3/bitmap/secret.bmp",  # secret's path
                            "test_objects/base3/bitmap/encoded/encoded_bunny.STL",
                            base3)  # path to save the carrier with secret

    decoder = DecoderSTL(
        "test_objects/base3/bitmap/encoded/encoded_bunny.STL", False)  # carrier's with secret filepath
    decoder.DecodeFileFromSTL(
        "test_objects/base3/bitmap/decoded/decoded_secret.bmp", base3)  # path to save the decoded secret

    orig_secret = open("test_objects/base3/bitmap/secret.bmp", "rb").read()

    decoded_secret = open("test_objects/base3/bitmap/decoded/decoded_secret.bmp", "rb").read()

    assert orig_secret == decoded_secret


# Test image base 3. infiltrating elephant_secret.jpeg into bunny stl file
def test_encode_decode_unicode_base_3():
    original_secret = "ȩƠĉÜ?ÎLʺ+ūŏ`ğƨȳüɠƸôȭĕƑŭ"

    encoder = EncoderSTL("test_objects/base3/unicode/bunny.STL", False)  # carrier's filepath
    encoder.EncodeBytesInSTL(original_secret,  # secret's path
                             "test_objects/base3/unicode/encoded/encoded_bunny.STL",
                             base3)  # path to save the carrier with secret

    decoder = DecoderSTL(
        "test_objects/base3/unicode/encoded/encoded_bunny.STL", False)  # carrier's with secret filepath
    secret_list: List[int] = decoder.DecodeBytesFromSTL(base3)  # path to save the decoded secret

    unicode_secret = ""
    for x in secret_list:
        unicode_secret += chr(x)

    assert original_secret == unicode_secret


# Random text vertex channel base 2
def test_encode_decode_unicode_base_2_random_text():
    original_secret = "jebsmmsfzv"

    encoder = EncoderSTL("test_objects/base2/random_text/bunny.STL", False)  # carrier's filepath
    encoder.EncodeBytesInSTL(original_secret,  # secret's path
                             "test_objects/base2/random_text/encoded/encoded_bunny.STL",
                             base2)  # path to save the carrier with secret

    decoder = DecoderSTL(
        "test_objects/base2/random_text/encoded/encoded_bunny.STL", False)  # carrier's with secret filepath
    secret_list: List[int] = decoder.DecodeBytesFromSTL(base2)  # path to save the decoded secret

    unicode_secret = ""
    for x in secret_list:
        unicode_secret += chr(x)

    assert original_secret == unicode_secret
