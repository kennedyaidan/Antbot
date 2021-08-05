# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from roboteq_msgs/Status.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class Status(genpy.Message):
  _md5sum = "d3a9b223fdfb0968255e25e5a859ac29"
  _type = "roboteq_msgs/Status"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# 10Hz status message for informational/diagnostics purposes
Header header

uint8 FAULT_OVERHEAT=1
uint8 FAULT_OVERVOLTAGE=2
uint8 FAULT_UNDERVOLTAGE=4
uint8 FAULT_SHORT_CIRCUIT=8
uint8 FAULT_EMERGENCY_STOP=16
uint8 FAULT_SEPEX_EXCITATION_FAULT=32
uint8 FAULT_MOSFET_FAILURE=64
uint8 FAULT_STARTUP_CONFIG_FAULT=128
uint8 fault

uint8 STATUS_SERIAL_MODE=1
uint8 STATUS_PULSE_MODE=2
uint8 STATUS_ANALOG_MODE=4
uint8 STATUS_POWER_STAGE_OFF=8
uint8 STATUS_STALL_DETECTED=16
uint8 STATUS_AT_LIMIT=32
uint8 STATUS_MICROBASIC_SCRIPT_RUNNING=128
uint8 status

# Temperature of main logic chip (C)
float32 ic_temperature

# Internal supply and reference voltage (V)
float32 internal_voltage
float32 adc_voltage

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  # Pseudo-constants
  FAULT_OVERHEAT = 1
  FAULT_OVERVOLTAGE = 2
  FAULT_UNDERVOLTAGE = 4
  FAULT_SHORT_CIRCUIT = 8
  FAULT_EMERGENCY_STOP = 16
  FAULT_SEPEX_EXCITATION_FAULT = 32
  FAULT_MOSFET_FAILURE = 64
  FAULT_STARTUP_CONFIG_FAULT = 128
  STATUS_SERIAL_MODE = 1
  STATUS_PULSE_MODE = 2
  STATUS_ANALOG_MODE = 4
  STATUS_POWER_STAGE_OFF = 8
  STATUS_STALL_DETECTED = 16
  STATUS_AT_LIMIT = 32
  STATUS_MICROBASIC_SCRIPT_RUNNING = 128

  __slots__ = ['header','fault','status','ic_temperature','internal_voltage','adc_voltage']
  _slot_types = ['std_msgs/Header','uint8','uint8','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,fault,status,ic_temperature,internal_voltage,adc_voltage

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Status, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.fault is None:
        self.fault = 0
      if self.status is None:
        self.status = 0
      if self.ic_temperature is None:
        self.ic_temperature = 0.
      if self.internal_voltage is None:
        self.internal_voltage = 0.
      if self.adc_voltage is None:
        self.adc_voltage = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.fault = 0
      self.status = 0
      self.ic_temperature = 0.
      self.internal_voltage = 0.
      self.adc_voltage = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2B3f().pack(_x.fault, _x.status, _x.ic_temperature, _x.internal_voltage, _x.adc_voltage))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 14
      (_x.fault, _x.status, _x.ic_temperature, _x.internal_voltage, _x.adc_voltage,) = _get_struct_2B3f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2B3f().pack(_x.fault, _x.status, _x.ic_temperature, _x.internal_voltage, _x.adc_voltage))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 14
      (_x.fault, _x.status, _x.ic_temperature, _x.internal_voltage, _x.adc_voltage,) = _get_struct_2B3f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B3f = None
def _get_struct_2B3f():
    global _struct_2B3f
    if _struct_2B3f is None:
        _struct_2B3f = struct.Struct("<2B3f")
    return _struct_2B3f
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
