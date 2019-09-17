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


class FundCardPublicRetrieve(object):
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
        'title': 'str',
        'short_description': 'str',
        'full_description': 'str',
        'cover': 'str',
        'url': 'str',
        'directions': 'list[int]',
        'fundraising_type': 'int',
        'payment_types': 'list[int]',
        'organizer': 'Organizer',
        'expires': 'str',
        'created': 'str',
        'benefactors': 'int',
        'content': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'short_description': 'short_description',
        'full_description': 'full_description',
        'cover': 'cover',
        'url': 'url',
        'directions': 'directions',
        'fundraising_type': 'fundraising_type',
        'payment_types': 'payment_types',
        'organizer': 'organizer',
        'expires': 'expires',
        'created': 'created',
        'benefactors': 'benefactors',
        'content': 'content'
    }

    def __init__(self, id=None, title=None, short_description=None, full_description=None, cover=None, url=None, directions=None, fundraising_type=None, payment_types=None, organizer=None, expires=None, created=None, benefactors=None, content=None):  # noqa: E501
        """FundCardPublicRetrieve - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._title = None
        self._short_description = None
        self._full_description = None
        self._cover = None
        self._url = None
        self._directions = None
        self._fundraising_type = None
        self._payment_types = None
        self._organizer = None
        self._expires = None
        self._created = None
        self._benefactors = None
        self._content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.title = title
        self.short_description = short_description
        self.full_description = full_description
        self.cover = cover
        self.url = url
        self.directions = directions
        self.fundraising_type = fundraising_type
        self.payment_types = payment_types
        if organizer is not None:
            self.organizer = organizer
        if expires is not None:
            self.expires = expires
        if created is not None:
            self.created = created
        if benefactors is not None:
            self.benefactors = benefactors
        self.content = content

    @property
    def id(self):
        """Gets the id of this FundCardPublicRetrieve.  # noqa: E501


        :return: The id of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FundCardPublicRetrieve.


        :param id: The id of this FundCardPublicRetrieve.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this FundCardPublicRetrieve.  # noqa: E501


        :return: The title of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FundCardPublicRetrieve.


        :param title: The title of this FundCardPublicRetrieve.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if title is not None and len(title) > 128:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `128`")  # noqa: E501
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def short_description(self):
        """Gets the short_description of this FundCardPublicRetrieve.  # noqa: E501


        :return: The short_description of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this FundCardPublicRetrieve.


        :param short_description: The short_description of this FundCardPublicRetrieve.  # noqa: E501
        :type: str
        """
        if short_description is None:
            raise ValueError("Invalid value for `short_description`, must not be `None`")  # noqa: E501
        if short_description is not None and len(short_description) > 128:
            raise ValueError("Invalid value for `short_description`, length must be less than or equal to `128`")  # noqa: E501
        if short_description is not None and len(short_description) < 1:
            raise ValueError("Invalid value for `short_description`, length must be greater than or equal to `1`")  # noqa: E501

        self._short_description = short_description

    @property
    def full_description(self):
        """Gets the full_description of this FundCardPublicRetrieve.  # noqa: E501


        :return: The full_description of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: str
        """
        return self._full_description

    @full_description.setter
    def full_description(self, full_description):
        """Sets the full_description of this FundCardPublicRetrieve.


        :param full_description: The full_description of this FundCardPublicRetrieve.  # noqa: E501
        :type: str
        """
        if full_description is None:
            raise ValueError("Invalid value for `full_description`, must not be `None`")  # noqa: E501
        if full_description is not None and len(full_description) < 1:
            raise ValueError("Invalid value for `full_description`, length must be greater than or equal to `1`")  # noqa: E501

        self._full_description = full_description

    @property
    def cover(self):
        """Gets the cover of this FundCardPublicRetrieve.  # noqa: E501


        :return: The cover of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """Sets the cover of this FundCardPublicRetrieve.


        :param cover: The cover of this FundCardPublicRetrieve.  # noqa: E501
        :type: str
        """

        self._cover = cover

    @property
    def url(self):
        """Gets the url of this FundCardPublicRetrieve.  # noqa: E501


        :return: The url of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FundCardPublicRetrieve.


        :param url: The url of this FundCardPublicRetrieve.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if url is not None and len(url) > 200:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `200`")  # noqa: E501
        if url is not None and len(url) < 1:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

    @property
    def directions(self):
        """Gets the directions of this FundCardPublicRetrieve.  # noqa: E501


        :return: The directions of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: list[int]
        """
        return self._directions

    @directions.setter
    def directions(self, directions):
        """Sets the directions of this FundCardPublicRetrieve.


        :param directions: The directions of this FundCardPublicRetrieve.  # noqa: E501
        :type: list[int]
        """
        if directions is None:
            raise ValueError("Invalid value for `directions`, must not be `None`")  # noqa: E501

        self._directions = directions

    @property
    def fundraising_type(self):
        """Gets the fundraising_type of this FundCardPublicRetrieve.  # noqa: E501


        :return: The fundraising_type of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: int
        """
        return self._fundraising_type

    @fundraising_type.setter
    def fundraising_type(self, fundraising_type):
        """Sets the fundraising_type of this FundCardPublicRetrieve.


        :param fundraising_type: The fundraising_type of this FundCardPublicRetrieve.  # noqa: E501
        :type: int
        """
        if fundraising_type is None:
            raise ValueError("Invalid value for `fundraising_type`, must not be `None`")  # noqa: E501

        self._fundraising_type = fundraising_type

    @property
    def payment_types(self):
        """Gets the payment_types of this FundCardPublicRetrieve.  # noqa: E501


        :return: The payment_types of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: list[int]
        """
        return self._payment_types

    @payment_types.setter
    def payment_types(self, payment_types):
        """Sets the payment_types of this FundCardPublicRetrieve.


        :param payment_types: The payment_types of this FundCardPublicRetrieve.  # noqa: E501
        :type: list[int]
        """
        if payment_types is None:
            raise ValueError("Invalid value for `payment_types`, must not be `None`")  # noqa: E501

        self._payment_types = payment_types

    @property
    def organizer(self):
        """Gets the organizer of this FundCardPublicRetrieve.  # noqa: E501


        :return: The organizer of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: Organizer
        """
        return self._organizer

    @organizer.setter
    def organizer(self, organizer):
        """Sets the organizer of this FundCardPublicRetrieve.


        :param organizer: The organizer of this FundCardPublicRetrieve.  # noqa: E501
        :type: Organizer
        """

        self._organizer = organizer

    @property
    def expires(self):
        """Gets the expires of this FundCardPublicRetrieve.  # noqa: E501


        :return: The expires of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this FundCardPublicRetrieve.


        :param expires: The expires of this FundCardPublicRetrieve.  # noqa: E501
        :type: str
        """

        self._expires = expires

    @property
    def created(self):
        """Gets the created of this FundCardPublicRetrieve.  # noqa: E501


        :return: The created of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FundCardPublicRetrieve.


        :param created: The created of this FundCardPublicRetrieve.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def benefactors(self):
        """Gets the benefactors of this FundCardPublicRetrieve.  # noqa: E501


        :return: The benefactors of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: int
        """
        return self._benefactors

    @benefactors.setter
    def benefactors(self, benefactors):
        """Sets the benefactors of this FundCardPublicRetrieve.


        :param benefactors: The benefactors of this FundCardPublicRetrieve.  # noqa: E501
        :type: int
        """
        if benefactors is not None and benefactors > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `benefactors`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if benefactors is not None and benefactors < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `benefactors`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._benefactors = benefactors

    @property
    def content(self):
        """Gets the content of this FundCardPublicRetrieve.  # noqa: E501


        :return: The content of this FundCardPublicRetrieve.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this FundCardPublicRetrieve.


        :param content: The content of this FundCardPublicRetrieve.  # noqa: E501
        :type: str
        """
        if content is not None and len(content) < 1:
            raise ValueError("Invalid value for `content`, length must be greater than or equal to `1`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, FundCardPublicRetrieve):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
