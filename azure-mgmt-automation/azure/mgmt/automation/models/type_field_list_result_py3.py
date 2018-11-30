# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TypeFieldListResult(Model):
    """The response model for the list fields operation.

    :param value: Gets or sets a list of fields.
    :type value: list[~azure.mgmt.automation.models.TypeField]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[TypeField]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(TypeFieldListResult, self).__init__(**kwargs)
        self.value = value
