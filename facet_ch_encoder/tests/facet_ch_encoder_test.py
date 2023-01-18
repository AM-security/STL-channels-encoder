from facet_ch_encoder.lib.facet_ch_encoder import EncoderSTL, DecoderSTL
import pytest


# Test text. infiltrating secret.txt into sphere stl file and decoding it
def test_encode_decode_text():
    encoder = EncoderSTL("test_objects/text/original_sphere.STL", False)  # carrier's filepath
    encoder.EncodeFileInSTL("test_objects/text/secret.txt",  # secret's path
                            "test_objects/text/encoded/encoded_sphere.STL")  # path to save the carrier with secret

    decoder = DecoderSTL("test_objects/text/encoded/encoded_sphere.STL", False)  # carrier's with secret filepath
    decoder.DecodeFileFromSTL(
        "test_objects/text/decoded/decoded_secret.txt")  # path to save the decoded secret

    secret = open("test_objects/text/decoded/decoded_secret.txt", "r").read()

    assert secret == "This is the secret message!"


# Test text. infiltrating secret.txt into sphere stl file
def test_encode_decode_bytes():
    encoder = EncoderSTL("test_objects/bytes/original_sphere.STL", False)  # carrier's filepath
    encoder.EncodeBytesInSTL(bytes("Smith (c)", "utf-8"),
                             "test_objects/text/encoded/encoded_sphere.STL")  # path to save the carrier with secret

    decoder = DecoderSTL("test_objects/text/encoded/encoded_sphere.STL", False)  # carrier's with secret filepath
    secret = decoder.DecodeBytesFromSTL()  # path to save the decoded secret

    assert secret.decode("utf-8") == "Smith (c)"
