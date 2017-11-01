load("@protobuf_bzl//:protobuf.bzl", "cc_proto_library", "py_proto_library")

licenses(["notice"])

# ----------------------------------------------------------------------
# Vendor'ed ListValue from google/protobuf/struct.proto
# ----------------------------------------------------------------------

proto_library(
    name = "struct_proto",
    srcs = ["struct.proto"],
)

cc_proto_library(
    name = "struct_cc_pb2",
    srcs = ["struct.proto"],
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
)

py_proto_library(
    name = "struct_py_pb2",
    srcs = ["struct.proto"],
    default_runtime = "@com_google_protobuf//:protobuf_python",
    protoc = "@com_google_protobuf//:protoc",
)

# ----------------------------------------------------------------------
# Cigar
# ----------------------------------------------------------------------

proto_library(
    name = "cigar_proto",
    srcs = ["cigar.proto"],
)

cc_proto_library(
    name = "cigar_cc_pb2",
    srcs = ["cigar.proto"],
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
)

py_proto_library(
    name = "cigar_py_pb2",
    srcs = ["cigar.proto"],
    default_runtime = "@com_google_protobuf//:protobuf_python",
    protoc = "@com_google_protobuf//:protoc",
)

# ----------------------------------------------------------------------
# Position
# ----------------------------------------------------------------------

proto_library(
    name = "position_proto",
    srcs = ["position.proto"],
)

cc_proto_library(
    name = "position_cc_pb2",
    srcs = ["position.proto"],
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
)

py_proto_library(
    name = "position_py_pb2",
    srcs = ["position.proto"],
    default_runtime = "@com_google_protobuf//:protobuf_python",
    protoc = "@com_google_protobuf//:protoc",
)

# ----------------------------------------------------------------------
# Range
# ----------------------------------------------------------------------

proto_library(
    name = "range_proto",
    srcs = ["range.proto"],
)

cc_proto_library(
    name = "range_cc_pb2",
    srcs = ["range.proto"],
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
)

py_proto_library(
    name = "range_py_pb2",
    srcs = ["range.proto"],
    default_runtime = "@com_google_protobuf//:protobuf_python",
    protoc = "@com_google_protobuf//:protoc",
)

# ----------------------------------------------------------------------
# Variants
# ----------------------------------------------------------------------

proto_library(
    name = "variants_proto",
    srcs = ["variants.proto"],
    deps = [":struct_proto"],
)

cc_proto_library(
    name = "variants_cc_pb2",
    srcs = ["variants.proto"],
    deps = [":struct_cc_pb2"],
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
)

py_proto_library(
    name = "variants_py_pb2",
    srcs = ["variants.proto"],
    deps = [":struct_py_pb2"],
    default_runtime = "@com_google_protobuf//:protobuf_python",
    protoc = "@com_google_protobuf//:protoc",
)

# ----------------------------------------------------------------------
# Read
# ----------------------------------------------------------------------

proto_library(
    name = "readalignment_proto",
    srcs = ["readalignment.proto"],
    deps = [
        ":cigar_proto",
        ":position_proto",
        ":struct_proto",
    ],
)

cc_proto_library(
    name = "readalignment_cc_pb2",
    srcs = ["readalignment.proto"],
    deps = [
        ":cigar_cc_pb2",
        ":position_cc_pb2",
        ":struct_cc_pb2",
    ],
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
)

py_proto_library(
    name = "readalignment_py_pb2",
    srcs = ["readalignment.proto"],
    deps = [
        ":cigar_py_pb2",
        ":position_py_pb2",
        ":struct_py_pb2",
    ],
    default_runtime = "@com_google_protobuf//:protobuf_python",
    protoc = "@com_google_protobuf//:protoc",
)

