# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class HistogramViewProperties(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'queries': 'list[DashboardQuery]',
        'colors': 'list[DashboardColor]',
        'shape': 'str',
        'note': 'str',
        'show_note_when_empty': 'bool',
        'x_column': 'str',
        'fill_columns': 'list[str]',
        'x_domain': 'list[float]',
        'x_axis_label': 'str',
        'position': 'str',
        'bin_count': 'int'
    }

    attribute_map = {
        'type': 'type',
        'queries': 'queries',
        'colors': 'colors',
        'shape': 'shape',
        'note': 'note',
        'show_note_when_empty': 'showNoteWhenEmpty',
        'x_column': 'xColumn',
        'fill_columns': 'fillColumns',
        'x_domain': 'xDomain',
        'x_axis_label': 'xAxisLabel',
        'position': 'position',
        'bin_count': 'binCount'
    }

    def __init__(self, type=None, queries=None, colors=None, shape=None, note=None, show_note_when_empty=None, x_column=None, fill_columns=None, x_domain=None, x_axis_label=None, position=None, bin_count=None):  # noqa: E501
        """HistogramViewProperties - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._queries = None
        self._colors = None
        self._shape = None
        self._note = None
        self._show_note_when_empty = None
        self._x_column = None
        self._fill_columns = None
        self._x_domain = None
        self._x_axis_label = None
        self._position = None
        self._bin_count = None
        self.discriminator = None

        self.type = type
        self.queries = queries
        self.colors = colors
        self.shape = shape
        self.note = note
        self.show_note_when_empty = show_note_when_empty
        self.x_column = x_column
        self.fill_columns = fill_columns
        self.x_domain = x_domain
        self.x_axis_label = x_axis_label
        self.position = position
        self.bin_count = bin_count

    @property
    def type(self):
        """Gets the type of this HistogramViewProperties.  # noqa: E501


        :return: The type of this HistogramViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HistogramViewProperties.


        :param type: The type of this HistogramViewProperties.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["histogram"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def queries(self):
        """Gets the queries of this HistogramViewProperties.  # noqa: E501


        :return: The queries of this HistogramViewProperties.  # noqa: E501
        :rtype: list[DashboardQuery]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this HistogramViewProperties.


        :param queries: The queries of this HistogramViewProperties.  # noqa: E501
        :type: list[DashboardQuery]
        """
        if queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501

        self._queries = queries

    @property
    def colors(self):
        """Gets the colors of this HistogramViewProperties.  # noqa: E501

        Colors define color encoding of data into a visualization  # noqa: E501

        :return: The colors of this HistogramViewProperties.  # noqa: E501
        :rtype: list[DashboardColor]
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this HistogramViewProperties.

        Colors define color encoding of data into a visualization  # noqa: E501

        :param colors: The colors of this HistogramViewProperties.  # noqa: E501
        :type: list[DashboardColor]
        """
        if colors is None:
            raise ValueError("Invalid value for `colors`, must not be `None`")  # noqa: E501

        self._colors = colors

    @property
    def shape(self):
        """Gets the shape of this HistogramViewProperties.  # noqa: E501


        :return: The shape of this HistogramViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this HistogramViewProperties.


        :param shape: The shape of this HistogramViewProperties.  # noqa: E501
        :type: str
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501
        allowed_values = ["chronograf-v2"]  # noqa: E501
        if shape not in allowed_values:
            raise ValueError(
                "Invalid value for `shape` ({0}), must be one of {1}"  # noqa: E501
                .format(shape, allowed_values)
            )

        self._shape = shape

    @property
    def note(self):
        """Gets the note of this HistogramViewProperties.  # noqa: E501


        :return: The note of this HistogramViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this HistogramViewProperties.


        :param note: The note of this HistogramViewProperties.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def show_note_when_empty(self):
        """Gets the show_note_when_empty of this HistogramViewProperties.  # noqa: E501

        if true, will display note when empty  # noqa: E501

        :return: The show_note_when_empty of this HistogramViewProperties.  # noqa: E501
        :rtype: bool
        """
        return self._show_note_when_empty

    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty):
        """Sets the show_note_when_empty of this HistogramViewProperties.

        if true, will display note when empty  # noqa: E501

        :param show_note_when_empty: The show_note_when_empty of this HistogramViewProperties.  # noqa: E501
        :type: bool
        """
        if show_note_when_empty is None:
            raise ValueError("Invalid value for `show_note_when_empty`, must not be `None`")  # noqa: E501

        self._show_note_when_empty = show_note_when_empty

    @property
    def x_column(self):
        """Gets the x_column of this HistogramViewProperties.  # noqa: E501


        :return: The x_column of this HistogramViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._x_column

    @x_column.setter
    def x_column(self, x_column):
        """Sets the x_column of this HistogramViewProperties.


        :param x_column: The x_column of this HistogramViewProperties.  # noqa: E501
        :type: str
        """
        if x_column is None:
            raise ValueError("Invalid value for `x_column`, must not be `None`")  # noqa: E501

        self._x_column = x_column

    @property
    def fill_columns(self):
        """Gets the fill_columns of this HistogramViewProperties.  # noqa: E501


        :return: The fill_columns of this HistogramViewProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._fill_columns

    @fill_columns.setter
    def fill_columns(self, fill_columns):
        """Sets the fill_columns of this HistogramViewProperties.


        :param fill_columns: The fill_columns of this HistogramViewProperties.  # noqa: E501
        :type: list[str]
        """
        if fill_columns is None:
            raise ValueError("Invalid value for `fill_columns`, must not be `None`")  # noqa: E501

        self._fill_columns = fill_columns

    @property
    def x_domain(self):
        """Gets the x_domain of this HistogramViewProperties.  # noqa: E501


        :return: The x_domain of this HistogramViewProperties.  # noqa: E501
        :rtype: list[float]
        """
        return self._x_domain

    @x_domain.setter
    def x_domain(self, x_domain):
        """Sets the x_domain of this HistogramViewProperties.


        :param x_domain: The x_domain of this HistogramViewProperties.  # noqa: E501
        :type: list[float]
        """
        if x_domain is None:
            raise ValueError("Invalid value for `x_domain`, must not be `None`")  # noqa: E501

        self._x_domain = x_domain

    @property
    def x_axis_label(self):
        """Gets the x_axis_label of this HistogramViewProperties.  # noqa: E501


        :return: The x_axis_label of this HistogramViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._x_axis_label

    @x_axis_label.setter
    def x_axis_label(self, x_axis_label):
        """Sets the x_axis_label of this HistogramViewProperties.


        :param x_axis_label: The x_axis_label of this HistogramViewProperties.  # noqa: E501
        :type: str
        """
        if x_axis_label is None:
            raise ValueError("Invalid value for `x_axis_label`, must not be `None`")  # noqa: E501

        self._x_axis_label = x_axis_label

    @property
    def position(self):
        """Gets the position of this HistogramViewProperties.  # noqa: E501


        :return: The position of this HistogramViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this HistogramViewProperties.


        :param position: The position of this HistogramViewProperties.  # noqa: E501
        :type: str
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501
        allowed_values = ["overlaid", "stacked"]  # noqa: E501
        if position not in allowed_values:
            raise ValueError(
                "Invalid value for `position` ({0}), must be one of {1}"  # noqa: E501
                .format(position, allowed_values)
            )

        self._position = position

    @property
    def bin_count(self):
        """Gets the bin_count of this HistogramViewProperties.  # noqa: E501


        :return: The bin_count of this HistogramViewProperties.  # noqa: E501
        :rtype: int
        """
        return self._bin_count

    @bin_count.setter
    def bin_count(self, bin_count):
        """Sets the bin_count of this HistogramViewProperties.


        :param bin_count: The bin_count of this HistogramViewProperties.  # noqa: E501
        :type: int
        """
        if bin_count is None:
            raise ValueError("Invalid value for `bin_count`, must not be `None`")  # noqa: E501

        self._bin_count = bin_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HistogramViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other