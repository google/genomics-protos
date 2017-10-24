# load("//:third_party/clif.bzl", "py_clif_cc", "pyclif_proto_library")
load("@protobuf_bzl//:protobuf.bzl", "py_proto_library")
load("@protobuf_bzl//:protobuf.bzl", "cc_proto_library")

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

#py_proto_library(
#    name = "struct_py_pb2",
#    srcs = ["struct.proto"],
#    default_runtime = "//external:protobuf",
#    protoc = "//external:protoc",
#    srcs_version = "PY2AND3",
#)

# DO we need a pyclif rule?

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

#py_proto_library(
#    name = "cigar_py_pb2",
#    srcs = ["cigar.proto"],
#    default_runtime = "//external:protobuf",
#    protoc = "//external:protoc",
#    srcs_version = "PY2AND3",
#)

#pyclif_proto_library(
#    name = "cigar_pyclif",
#    proto_lib = ":cigar_proto",     # NO COPYBARA
#)

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

#py_proto_library(
#    name = "position_py_pb2",
#    srcs = ["position.proto"],
#    default_runtime = "//external:protobuf",
#    protoc = "//external:protoc",
#    srcs_version = "PY2AND3",
#)

#pyclif_proto_library(
#    name = "position_pyclif",
#    proto_lib = ":position_proto",     # NO COPYBARA
#)

# ----------------------------------------------------------------------
# Range
# ----------------------------------------------------------------------

proto_library(
    name = "range_proto",
    srcs = ["range.proto"],
)

# TODO(mdepristo): everyone needs to use this style.
# TODO(mdepristo): use our own cc_proto_rule that adds this boilerplate.
cc_proto_library(
    name = "range_cc_pb2",
    srcs = ["range.proto"],
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
)

#py_proto_library(
#    name = "range_py_pb2",
#    srcs = ["range.proto"],
#    default_runtime = "//external:protobuf",
#    protoc = "//external:protoc",
#    srcs_version = "PY2AND3",
#)

#pyclif_proto_library(
#    name = "range_pyclif",
#    proto_lib = ":range_proto",     # NO COPYBARA
#)

# ----------------------------------------------------------------------
# Variants
# ----------------------------------------------------------------------

proto_library(
    name = "variants_proto",
    srcs = ["variants.proto"],
    deps = [":struct_proto"],     # NO COPYBARA
)

cc_proto_library(
    name = "variants_cc_pb2",
    srcs = ["variants.proto"],
    deps = [":struct_cc_pb2"],
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
)

#py_proto_library(
#    name = "variants_py_pb2",
#    srcs = ["variants.proto",],
#    deps = [":struct_py_pb2"],
#    default_runtime = "//external:protobuf",
#    protoc = "//external:protoc",
#    srcs_version = "PY2AND3",
#)

#pyclif_proto_library(
#    name = "variants_pyclif",
#    proto_lib = ":variants_proto",     # NO COPYBARA
#)

# ----------------------------------------------------------------------
# Read
# ----------------------------------------------------------------------

proto_library(
    name = "reads_proto",
    srcs = ["reads.proto"],
    deps = [
        ":cigar_proto",     # NO COPYBARA
        ":position_proto",  # NO COPYBARA
        ":struct_proto"     # NO COPYBARA
    ],
)

cc_proto_library(
    name = "reads_cc_pb2",
    srcs = ["reads.proto"],
    deps = [
        ":cigar_cc_pb2",
        ":position_cc_pb2",
        ":struct_cc_pb2",
    ],
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
)

#py_proto_library(
#    name = "reads_py_pb2",
#    srcs = ["reads.proto"],
#    deps = [
#        ":cigar_py_pb2",
#        ":position_py_pb2",
#        ":struct_py_pb2",
#    ],
#    default_runtime = "//external:protobuf",
#    protoc = "//external:protoc",
#    srcs_version = "PY2AND3",
#)

#pyclif_proto_library(
#    name = "reads_pyclif",
#    proto_lib = ":reads_proto",     # NO COPYBARA
#)
