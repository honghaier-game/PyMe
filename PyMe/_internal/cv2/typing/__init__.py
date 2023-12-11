__all__ = [
    "IntPointer",
    "MatLike",
    "MatShape",
    "Size",
    "Size2f",
    "Scalar",
    "Point",
    "Point2i",
    "Point2f",
    "Point2d",
    "Point3i",
    "Point3f",
    "Point3d",
    "Range",
    "Rect",
    "Rect2i",
    "Rect2d",
    "Moments",
    "RotatedRect",
    "TermCriteria",
    "Vec2i",
    "Vec2f",
    "Vec2d",
    "Vec3i",
    "Vec3f",
    "Vec3d",
    "Vec4i",
    "Vec4f",
    "Vec4d",
    "Vec6f",
    "FeatureDetector",
    "DescriptorExtractor",
    "FeatureExtractor",
    "GProtoArg",
    "GProtoInputArgs",
    "GProtoOutputArgs",
    "GRunArg",
    "GOptRunArg",
    "GMetaArg",
    "Prim",
    "Matx33f",
    "Matx33d",
    "Matx44f",
    "Matx44d",
    "GTypeInfo",
    "ExtractArgsCallback",
    "ExtractMetaCallback",
    "LayerId",
    "IndexParams",
    "SearchParams",
    "map_string_and_string",
    "map_string_and_int",
    "map_string_and_vector_size_t",
    "map_string_and_vector_float",
    "map_int_and_double",
]

import cv2
import cv2.dnn
import cv2.gapi.wip.draw
import cv2.mat_wrapper
import numpy
import sys
import typing


if numpy.lib.NumpyVersion(numpy.__version__) > "1.20.0" and sys.version_info >= (3, 9):
    NumPyArrayGeneric = numpy.ndarray[typing.Any, numpy.dtype[numpy.generic]]
else:
    NumPyArrayGeneric = numpy.ndarray


if numpy.lib.NumpyVersion(numpy.__version__) > "1.20.0" and sys.version_info >= (3, 9):
    NumPyArrayFloat32 = numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]]
else:
    NumPyArrayFloat32 = numpy.ndarray


if numpy.lib.NumpyVersion(numpy.__version__) > "1.20.0" and sys.version_info >= (3, 9):
    NumPyArrayFloat64 = numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]]
else:
    NumPyArrayFloat64 = numpy.ndarray


if typing.TYPE_CHECKING:
    TermCriteria_Type = cv2.TermCriteria_Type
else:
    TermCriteria_Type = int


IntPointer = int
"""Represents an arbitrary pointer"""
MatLike = typing.Union[cv2.mat_wrapper.Mat, NumPyArrayGeneric]
MatShape = typing.Sequence[int]
Size = typing.Sequence[int]
"""Required length is 2"""
Size2f = typing.Sequence[float]
"""Required length is 2"""
Scalar = typing.Sequence[float]
"""Required length is at most 4"""
Point = typing.Sequence[int]
"""Required length is 2"""
Point2i = Point
Point2f = typing.Sequence[float]
"""Required length is 2"""
Point2d = typing.Sequence[float]
"""Required length is 2"""
Point3i = typing.Sequence[int]
"""Required length is 3"""
Point3f = typing.Sequence[float]
"""Required length is 3"""
Point3d = typing.Sequence[float]
"""Required length is 3"""
Range = typing.Sequence[int]
"""Required length is 2"""
Rect = typing.Sequence[int]
"""Required length is 4"""
Rect2i = typing.Sequence[int]
"""Required length is 4"""
Rect2d = typing.Sequence[float]
"""Required length is 4"""
Moments = typing.Dict[str, float]
RotatedRect = typing.Tuple[Point2f, Size, float]
"""Any type providing sequence protocol is supported"""
TermCriteria = typing.Tuple[TermCriteria_Type, int, float]
"""Any type providing sequence protocol is supported"""
Vec2i = typing.Sequence[int]
"""Required length is 2"""
Vec2f = typing.Sequence[float]
"""Required length is 2"""
Vec2d = typing.Sequence[float]
"""Required length is 2"""
Vec3i = typing.Sequence[int]
"""Required length is 3"""
Vec3f = typing.Sequence[float]
"""Required length is 3"""
Vec3d = typing.Sequence[float]
"""Required length is 3"""
Vec4i = typing.Sequence[int]
"""Required length is 4"""
Vec4f = typing.Sequence[float]
"""Required length is 4"""
Vec4d = typing.Sequence[float]
"""Required length is 4"""
Vec6f = typing.Sequence[float]
"""Required length is 6"""
FeatureDetector = cv2.Feature2D
DescriptorExtractor = cv2.Feature2D
FeatureExtractor = cv2.Feature2D
GProtoArg = typing.Union[Scalar, cv2.GMat, cv2.GOpaqueT, cv2.GArrayT]
GProtoInputArgs = typing.Sequence[GProtoArg]
GProtoOutputArgs = typing.Sequence[GProtoArg]
GRunArg = typing.Union[MatLike, Scalar, cv2.GOpaqueT, cv2.GArrayT, typing.Sequence[typing.Any], None]
GOptRunArg = typing.Optional[GRunArg]
GMetaArg = typing.Union[cv2.GMat, Scalar, cv2.GOpaqueT, cv2.GArrayT]
Prim = typing.Union[cv2.gapi.wip.draw.Text, cv2.gapi.wip.draw.Circle, cv2.gapi.wip.draw.Image, cv2.gapi.wip.draw.Line, cv2.gapi.wip.draw.Rect, cv2.gapi.wip.draw.Mosaic, cv2.gapi.wip.draw.Poly]
Matx33f = NumPyArrayFloat32
"""NDArray(shape=(3, 3), dtype=numpy.float32)"""
Matx33d = NumPyArrayFloat64
"""NDArray(shape=(3, 3), dtype=numpy.float64)"""
Matx44f = NumPyArrayFloat32
"""NDArray(shape=(4, 4), dtype=numpy.float32)"""
Matx44d = NumPyArrayFloat64
"""NDArray(shape=(4, 4), dtype=numpy.float64)"""
GTypeInfo = typing.Union[cv2.GMat, Scalar, cv2.GOpaqueT, cv2.GArrayT]
ExtractArgsCallback = typing.Callable[[typing.Sequence[GTypeInfo]], typing.Sequence[GRunArg]]
ExtractMetaCallback = typing.Callable[[typing.Sequence[GTypeInfo]], typing.Sequence[GMetaArg]]
LayerId = cv2.dnn.DictValue
IndexParams = typing.Dict[str, typing.Union[bool, int, float, str]]
SearchParams = typing.Dict[str, typing.Union[bool, int, float, str]]
map_string_and_string = typing.Dict[str, str]
map_string_and_int = typing.Dict[str, int]
map_string_and_vector_size_t = typing.Dict[str, typing.Sequence[int]]
map_string_and_vector_float = typing.Dict[str, typing.Sequence[float]]
map_int_and_double = typing.Dict[int, float]
