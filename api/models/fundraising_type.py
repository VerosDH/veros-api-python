# coding: utf-8

"""
    Veros API

    Routes of Veros project  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FundraisingType(object):
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
        'id': 'int',
        'name': 'str',
        'logo': 'str',
        'color': 'str',
        'max_per_user': 'int',
        'max_per_organization': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'logo': 'logo',
        'color': 'color',
        'max_per_user': 'max_per_user',
        'max_per_organization': 'max_per_organization'
    }

    def __init__(self, id=None, name=None, logo=None, color=None, max_per_user=None, max_per_organization=None):  # noqa: E501
        """FundraisingType - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._logo = None
        self._color = None
        self._max_per_user = None
        self._max_per_organization = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if logo is not None:
            self.logo = logo
        if color is not None:
            self.color = color
        if max_per_user is not None:
            self.max_per_user = max_per_user
        if max_per_organization is not None:
            self.max_per_organization = max_per_organization

    @property
    def id(self):
        """Gets the id of this FundraisingType.  # noqa: E501


        :return: The id of this FundraisingType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FundraisingType.


        :param id: The id of this FundraisingType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FundraisingType.  # noqa: E501


        :return: The name of this FundraisingType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FundraisingType.


        :param name: The name of this FundraisingType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def logo(self):
        """Gets the logo of this FundraisingType.  # noqa: E501


        :return: The logo of this FundraisingType.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this FundraisingType.


        :param logo: The logo of this FundraisingType.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def color(self):
        """Gets the color of this FundraisingType.  # noqa: E501


        :return: The color of this FundraisingType.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this FundraisingType.


        :param color: The color of this FundraisingType.  # noqa: E501
        :type: str
        """
        allowed_values = ["default", "blue", "purple", "dark-green", "orange", "pink"]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"  # noqa: E501
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def max_per_user(self):
        """Gets the max_per_user of this FundraisingType.  # noqa: E501


        :return: The max_per_user of this FundraisingType.  # noqa: E501
        :rtype: int
        """
        return self._max_per_user

    @max_per_user.setter
    def max_per_user(self, max_per_user):
        """Sets the max_per_user of this FundraisingType.


        :param max_per_user: The max_per_user of this FundraisingType.  # noqa: E501
        :type: int
        """
        if max_per_user is not None and max_per_user > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `max_per_user`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if max_per_user is not None and max_per_user < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `max_per_user`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._max_per_user = max_per_user

    @property
    def max_per_organization(self):
        """Gets the max_per_organization of this FundraisingType.  # noqa: E501


        :return: The max_per_organization of this FundraisingType.  # noqa: E501
        :rtype: int
        """
        return self._max_per_organization

    @max_per_organization.setter
    def max_per_organization(self, max_per_organization):
        """Sets the max_per_organization of this FundraisingType.


        :param max_per_organization: The max_per_organization of this FundraisingType.  # noqa: E501
        :type: int
        """
        if max_per_organization is not None and max_per_organization > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `max_per_organization`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if max_per_organization is not None and max_per_organization < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `max_per_organization`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._max_per_organization = max_per_organization

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
        if not isinstance(other, FundraisingType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other