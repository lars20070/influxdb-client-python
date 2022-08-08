# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class StackResources(object):
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
        'api_version': 'str',
        'resource_id': 'str',
        'kind': 'TemplateKind',
        'template_meta_name': 'str',
        'associations': 'list[StackAssociations]',
        'links': 'StackLinks'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'resource_id': 'resourceID',
        'kind': 'kind',
        'template_meta_name': 'templateMetaName',
        'associations': 'associations',
        'links': 'links'
    }

    def __init__(self, api_version=None, resource_id=None, kind=None, template_meta_name=None, associations=None, links=None):  # noqa: E501,D401,D403
        """StackResources - a model defined in OpenAPI."""  # noqa: E501
        self._api_version = None
        self._resource_id = None
        self._kind = None
        self._template_meta_name = None
        self._associations = None
        self._links = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if resource_id is not None:
            self.resource_id = resource_id
        if kind is not None:
            self.kind = kind
        if template_meta_name is not None:
            self.template_meta_name = template_meta_name
        if associations is not None:
            self.associations = associations
        if links is not None:
            self.links = links

    @property
    def api_version(self):
        """Get the api_version of this StackResources.

        :return: The api_version of this StackResources.
        :rtype: str
        """  # noqa: E501
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Set the api_version of this StackResources.

        :param api_version: The api_version of this StackResources.
        :type: str
        """  # noqa: E501
        self._api_version = api_version

    @property
    def resource_id(self):
        """Get the resource_id of this StackResources.

        :return: The resource_id of this StackResources.
        :rtype: str
        """  # noqa: E501
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Set the resource_id of this StackResources.

        :param resource_id: The resource_id of this StackResources.
        :type: str
        """  # noqa: E501
        self._resource_id = resource_id

    @property
    def kind(self):
        """Get the kind of this StackResources.

        :return: The kind of this StackResources.
        :rtype: TemplateKind
        """  # noqa: E501
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Set the kind of this StackResources.

        :param kind: The kind of this StackResources.
        :type: TemplateKind
        """  # noqa: E501
        self._kind = kind

    @property
    def template_meta_name(self):
        """Get the template_meta_name of this StackResources.

        :return: The template_meta_name of this StackResources.
        :rtype: str
        """  # noqa: E501
        return self._template_meta_name

    @template_meta_name.setter
    def template_meta_name(self, template_meta_name):
        """Set the template_meta_name of this StackResources.

        :param template_meta_name: The template_meta_name of this StackResources.
        :type: str
        """  # noqa: E501
        self._template_meta_name = template_meta_name

    @property
    def associations(self):
        """Get the associations of this StackResources.

        :return: The associations of this StackResources.
        :rtype: list[StackAssociations]
        """  # noqa: E501
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Set the associations of this StackResources.

        :param associations: The associations of this StackResources.
        :type: list[StackAssociations]
        """  # noqa: E501
        self._associations = associations

    @property
    def links(self):
        """Get the links of this StackResources.

        :return: The links of this StackResources.
        :rtype: StackLinks
        """  # noqa: E501
        return self._links

    @links.setter
    def links(self, links):
        """Set the links of this StackResources.

        :param links: The links of this StackResources.
        :type: StackLinks
        """  # noqa: E501
        self._links = links

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in self.openapi_types.items():
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, StackResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other