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


class View(object):
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
        'links': 'ViewLinks',
        'id': 'str',
        'name': 'str',
        'properties': 'object'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'name': 'name',
        'properties': 'properties'
    }

    def __init__(self, links=None, id=None, name=None, properties=None):  # noqa: E501
        """View - a model defined in OpenAPI"""  # noqa: E501

        self._links = None
        self._id = None
        self._name = None
        self._properties = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties

    @property
    def links(self):
        """Gets the links of this View.  # noqa: E501


        :return: The links of this View.  # noqa: E501
        :rtype: ViewLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this View.


        :param links: The links of this View.  # noqa: E501
        :type: ViewLinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this View.  # noqa: E501


        :return: The id of this View.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this View.


        :param id: The id of this View.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this View.  # noqa: E501


        :return: The name of this View.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this View.


        :param name: The name of this View.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this View.  # noqa: E501


        :return: The properties of this View.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this View.


        :param properties: The properties of this View.  # noqa: E501
        :type: object
        """

        self._properties = properties

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
        if not isinstance(other, View):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other