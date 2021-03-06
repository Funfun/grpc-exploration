# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='logs.proto',
  package='logs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nlogs.proto\x12\x04logs\"#\n\x10GetRecentRequest\x12\x0f\n\x07linesNo\x18\x01 \x01(\t\"!\n\x11GetRecentResponse\x12\x0c\n\x04logs\x18\x01 \x01(\t2B\n\x04Logs\x12:\n\x05Print\x12\x16.logs.GetRecentRequest\x1a\x17.logs.GetRecentResponse\"\x00\x62\x06proto3')
)




_GETRECENTREQUEST = _descriptor.Descriptor(
  name='GetRecentRequest',
  full_name='logs.GetRecentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linesNo', full_name='logs.GetRecentRequest.linesNo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=55,
)


_GETRECENTRESPONSE = _descriptor.Descriptor(
  name='GetRecentResponse',
  full_name='logs.GetRecentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logs', full_name='logs.GetRecentResponse.logs', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['GetRecentRequest'] = _GETRECENTREQUEST
DESCRIPTOR.message_types_by_name['GetRecentResponse'] = _GETRECENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRecentRequest = _reflection.GeneratedProtocolMessageType('GetRecentRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETRECENTREQUEST,
  __module__ = 'logs_pb2'
  # @@protoc_insertion_point(class_scope:logs.GetRecentRequest)
  ))
_sym_db.RegisterMessage(GetRecentRequest)

GetRecentResponse = _reflection.GeneratedProtocolMessageType('GetRecentResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETRECENTRESPONSE,
  __module__ = 'logs_pb2'
  # @@protoc_insertion_point(class_scope:logs.GetRecentResponse)
  ))
_sym_db.RegisterMessage(GetRecentResponse)



_LOGS = _descriptor.ServiceDescriptor(
  name='Logs',
  full_name='logs.Logs',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=92,
  serialized_end=158,
  methods=[
  _descriptor.MethodDescriptor(
    name='Print',
    full_name='logs.Logs.Print',
    index=0,
    containing_service=None,
    input_type=_GETRECENTREQUEST,
    output_type=_GETRECENTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGS)

DESCRIPTOR.services_by_name['Logs'] = _LOGS

# @@protoc_insertion_point(module_scope)
