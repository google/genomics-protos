workspace(name = "genomics_protos")

git_repository(
    name = "protobuf_bzl",
    # v3.4.0
    commit = "80a37e0782d2d702d52234b62dd4b9ec74fd2c95",
    remote = "https://github.com/google/protobuf.git",
)

bind(
    name = "protobuf",
    actual = "@protobuf_bzl//:protobuf",
)

bind(
    name = "protobuf_python",
    actual = "@protobuf_bzl//:protobuf_python",
)

bind(
    name = "protobuf_python_genproto",
    actual = "@protobuf_bzl//:protobuf_python_genproto",
)

bind(
    name = "protoc",
    actual = "@protobuf_bzl//:protoc",
)

new_http_archive(
    name = "six_archive",
    build_file = "@protobuf_bzl//:six.BUILD",
    sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a",
    url = "https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz#md5=34eed507548117b2ab523ab14b2f8b55",
)

bind(
    name = "six",
    actual = "@six_archive//:six",
)

bazel_version="0.7.0"
http_archive(
    name = "com_google_protobuf",
    url = "https://github.com/bazelbuild/bazel/archive/" + bazel_version + ".zip",
    strip_prefix = "bazel-" + bazel_version + "/third_party/protobuf/3.4.0",
)
