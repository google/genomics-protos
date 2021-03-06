# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/genomics/v1/variants.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.genomics.v1 import struct_pb2 as google_dot_genomics_dot_v1_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/genomics/v1/variants.proto',
  package='google.genomics.v1',
  syntax='proto3',
  serialized_pb=_b('\n!google/genomics/v1/variants.proto\x12\x12google.genomics.v1\x1a\x1fgoogle/genomics/v1/struct.proto\"\x97\x03\n\x07Variant\x12\x16\n\x0evariant_set_id\x18\x0f \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05names\x18\x03 \x03(\t\x12\x0f\n\x07\x63reated\x18\x0c \x01(\x03\x12\x16\n\x0ereference_name\x18\x0e \x01(\t\x12\r\n\x05start\x18\x10 \x01(\x03\x12\x0b\n\x03\x65nd\x18\r \x01(\x03\x12\x17\n\x0freference_bases\x18\x06 \x01(\t\x12\x17\n\x0f\x61lternate_bases\x18\x07 \x03(\t\x12\x0f\n\x07quality\x18\x08 \x01(\x01\x12\x0e\n\x06\x66ilter\x18\t \x03(\t\x12\x33\n\x04info\x18\n \x03(\x0b\x32%.google.genomics.v1.Variant.InfoEntry\x12.\n\x05\x63\x61lls\x18\x0b \x03(\x0b\x32\x1f.google.genomics.v1.VariantCall\x1aJ\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.google.genomics.v1.ListValue:\x02\x38\x01J\x04\x08\x01\x10\x02J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\"\x91\x02\n\x0bVariantCall\x12\x13\n\x0b\x63\x61ll_set_id\x18\x08 \x01(\t\x12\x15\n\rcall_set_name\x18\t \x01(\t\x12\x10\n\x08genotype\x18\x07 \x03(\x05\x12\x10\n\x08phaseset\x18\x05 \x01(\t\x12\x1b\n\x13genotype_likelihood\x18\x06 \x03(\x01\x12\x37\n\x04info\x18\x02 \x03(\x0b\x32).google.genomics.v1.VariantCall.InfoEntry\x1aJ\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.google.genomics.v1.ListValue:\x02\x38\x01J\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05\x42\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_genomics_dot_v1_dot_struct__pb2.DESCRIPTOR,])




_VARIANT_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='google.genomics.v1.Variant.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.genomics.v1.Variant.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.genomics.v1.Variant.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=480,
)

_VARIANT = _descriptor.Descriptor(
  name='Variant',
  full_name='google.genomics.v1.Variant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_set_id', full_name='google.genomics.v1.Variant.variant_set_id', index=0,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.genomics.v1.Variant.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='names', full_name='google.genomics.v1.Variant.names', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='google.genomics.v1.Variant.created', index=3,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='google.genomics.v1.Variant.reference_name', index=4,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='google.genomics.v1.Variant.start', index=5,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='google.genomics.v1.Variant.end', index=6,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_bases', full_name='google.genomics.v1.Variant.reference_bases', index=7,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternate_bases', full_name='google.genomics.v1.Variant.alternate_bases', index=8,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quality', full_name='google.genomics.v1.Variant.quality', index=9,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.genomics.v1.Variant.filter', index=10,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='google.genomics.v1.Variant.info', index=11,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calls', full_name='google.genomics.v1.Variant.calls', index=12,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VARIANT_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=498,
)


_VARIANTCALL_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='google.genomics.v1.VariantCall.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.genomics.v1.VariantCall.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.genomics.v1.VariantCall.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=480,
)

_VARIANTCALL = _descriptor.Descriptor(
  name='VariantCall',
  full_name='google.genomics.v1.VariantCall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_set_id', full_name='google.genomics.v1.VariantCall.call_set_id', index=0,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_set_name', full_name='google.genomics.v1.VariantCall.call_set_name', index=1,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genotype', full_name='google.genomics.v1.VariantCall.genotype', index=2,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phaseset', full_name='google.genomics.v1.VariantCall.phaseset', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genotype_likelihood', full_name='google.genomics.v1.VariantCall.genotype_likelihood', index=4,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='google.genomics.v1.VariantCall.info', index=5,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VARIANTCALL_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=774,
)

_VARIANT_INFOENTRY.fields_by_name['value'].message_type = google_dot_genomics_dot_v1_dot_struct__pb2._LISTVALUE
_VARIANT_INFOENTRY.containing_type = _VARIANT
_VARIANT.fields_by_name['info'].message_type = _VARIANT_INFOENTRY
_VARIANT.fields_by_name['calls'].message_type = _VARIANTCALL
_VARIANTCALL_INFOENTRY.fields_by_name['value'].message_type = google_dot_genomics_dot_v1_dot_struct__pb2._LISTVALUE
_VARIANTCALL_INFOENTRY.containing_type = _VARIANTCALL
_VARIANTCALL.fields_by_name['info'].message_type = _VARIANTCALL_INFOENTRY
DESCRIPTOR.message_types_by_name['Variant'] = _VARIANT
DESCRIPTOR.message_types_by_name['VariantCall'] = _VARIANTCALL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Variant = _reflection.GeneratedProtocolMessageType('Variant', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _VARIANT_INFOENTRY,
    __module__ = 'google.genomics.v1.variants_pb2'
    # @@protoc_insertion_point(class_scope:google.genomics.v1.Variant.InfoEntry)
    ))
  ,
  DESCRIPTOR = _VARIANT,
  __module__ = 'google.genomics.v1.variants_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.Variant)
  ))
_sym_db.RegisterMessage(Variant)
_sym_db.RegisterMessage(Variant.InfoEntry)

VariantCall = _reflection.GeneratedProtocolMessageType('VariantCall', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _VARIANTCALL_INFOENTRY,
    __module__ = 'google.genomics.v1.variants_pb2'
    # @@protoc_insertion_point(class_scope:google.genomics.v1.VariantCall.InfoEntry)
    ))
  ,
  DESCRIPTOR = _VARIANTCALL,
  __module__ = 'google.genomics.v1.variants_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.VariantCall)
  ))
_sym_db.RegisterMessage(VariantCall)
_sym_db.RegisterMessage(VariantCall.InfoEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
_VARIANT_INFOENTRY.has_options = True
_VARIANT_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_VARIANTCALL_INFOENTRY.has_options = True
_VARIANTCALL_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
