# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pbf/Event.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'pbf/Event.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fpbf/Event.proto\x12\x06\x65vents\"\x85\x01\n\tEventSpec\x12\x11\n\teventUUID\x18\x01 \x01(\t\x12\x12\n\neventTitle\x18\x02 \x01(\t\x12\x18\n\x10\x65ventDescription\x18\x03 \x01(\t\x12\x11\n\teventHref\x18\x04 \x01(\t\x12\x11\n\teventTime\x18\x05 \x01(\t\x12\x11\n\timageHash\x18\x06 \x01(\t\".\n\tEventList\x12!\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x11.events.EventSpec\"=\n\tEventPost\x12\r\n\x05token\x18\x01 \x01(\t\x12!\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x11.events.EventSpec\"+\n\x0b\x45ventDelete\x12\r\n\x05token\x18\x01 \x01(\t\x12\r\n\x05uuids\x18\x02 \x03(\t\">\n\x0b\x45ventUpdate\x12\r\n\x05token\x18\x01 \x01(\t\x12 \n\x05\x65vent\x18\x02 \x01(\x0b\x32\x11.events.EventSpec\"\x1b\n\nAdminToken\x12\r\n\x05token\x18\x01 \x01(\t\"9\n\x0bStorageInfo\x12\x0c\n\x04size\x18\x01 \x01(\x04\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x12\r\n\x05\x66iles\x18\x03 \x03(\t\"=\n\x0bImageUpload\x12\r\n\x05token\x18\x03 \x01(\t\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\".\n\x0bImageDelete\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\" \n\rStateResponse\x12\x0f\n\x07message\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pbf.Event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENTSPEC']._serialized_start=28
  _globals['_EVENTSPEC']._serialized_end=161
  _globals['_EVENTLIST']._serialized_start=163
  _globals['_EVENTLIST']._serialized_end=209
  _globals['_EVENTPOST']._serialized_start=211
  _globals['_EVENTPOST']._serialized_end=272
  _globals['_EVENTDELETE']._serialized_start=274
  _globals['_EVENTDELETE']._serialized_end=317
  _globals['_EVENTUPDATE']._serialized_start=319
  _globals['_EVENTUPDATE']._serialized_end=381
  _globals['_ADMINTOKEN']._serialized_start=383
  _globals['_ADMINTOKEN']._serialized_end=410
  _globals['_STORAGEINFO']._serialized_start=412
  _globals['_STORAGEINFO']._serialized_end=469
  _globals['_IMAGEUPLOAD']._serialized_start=471
  _globals['_IMAGEUPLOAD']._serialized_end=532
  _globals['_IMAGEDELETE']._serialized_start=534
  _globals['_IMAGEDELETE']._serialized_end=580
  _globals['_STATERESPONSE']._serialized_start=582
  _globals['_STATERESPONSE']._serialized_end=614
# @@protoc_insertion_point(module_scope)
