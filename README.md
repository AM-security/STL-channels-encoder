# STL Stego Channels Encoder

## Library that steganographically encodes data into covert channels of STL files. 

### Run tests:

    cd facet_ch_encoder/tests && pytest -q facet_ch_encoder_test.py
    cd vertex_ch_encoder/tests && pytest -q vertex_ch_encoder_test.py 

## Notes:
    Unicode is supported only for DecodeBytesFromSTL and EncodeBytesToSTL
    Not for DecodeFileFromSTL and EncodeFileToSTL!
    And only for vertex channel
