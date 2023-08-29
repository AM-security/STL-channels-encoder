# STL Stego Channels Encoder

## Library that steganographically encodes data into covert channels of STL files. 

### Run tests:

    cd facet_ch_encoder/tests && pytest -q facet_ch_encoder_test.py # Or python -m pytest
    cd vertex_ch_encoder/tests && pytest -q vertex_ch_encoder_test.py 

## Notes:
    Unicode is supported only for DecodeBytesFromSTL and EncodeBytesToSTL
    Not for DecodeFileFromSTL and EncodeFileToSTL!


# build the package (for developers)
https://packaging.python.org/en/latest/tutorials/packaging-projects/

python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --upgrade twine
python3 -m twine upload --skip-existing --repository testpypi dist/* 

# install this package
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps stlcovertchannels