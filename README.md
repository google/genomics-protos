# Genomics protos

This project contains protocol buffer definitions for working with
genomics data.  These definitions are based on the
`google.genomics.v1.*` protos from
[googleapis](https://github.com/googleapis/googleapis), but with the
API-specific pieces removed.

For convenience, this package also contains pre-compiled Python versions of
the protobufs which can be installed using pip via the instructions below.

## License

This code is licensed under the terms of the [Apache license](LICENSE).

## Disclaimer

*   This is not an official Google product.

## Installing for Python

You are welcome to use the `.proto` files directly. For Python specifically,
we provide pre-compiled files that can be installed via `pip`.

Optional but recommended: start a virtualenv

```
$ cd
$ virtualenv my_genomics
$ source my_genomics/bin/activate
```

Now cd just above the genomics_protos directory and install:

```
pip install --upgrade genomics_protos/
```

You can now use the protos. For example:

```
$ python
from google.genomics.v1 import readalignment_pb2
r = readalignment_pb2.Read()
r.alignment.position.reference_name = 'chr1'
r.alignment.position.position = 1000000
```

## How these files are generated

The *_pb2 files are generated as follows:

```
$ protoc google/genomics/v1/*.proto --python_out=.
```
