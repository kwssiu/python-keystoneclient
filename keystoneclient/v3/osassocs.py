# Copyright 2011 OpenStack LLC.
# Copyright 2011 Nebula, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.os/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from keystoneclient import base


class OsAttributeAssociation(base.Resource):
    """Represents an os_attribute_association.

    Attributes:
        * id: a uuid that identifies the attribute
        * name: attribute name
        * description: attribute description
        * attribute: ID of OsAttribute
        * os_attribute_set: ID of OsAttributeSet

    """
    def update(self, name=None, description=None,
               attribute=None, os_attribute_set=None):
        kwargs = {
            'name': name if name is not None else self.name,
            'description': (description
                            if description is not None
                            else self.description),
            'attribute': (
                        attribute if attribute is not None
                        else self.attribute),
            'os_attribute_set': (
                        os_attribute_set if
                        os_attribute_set is not None
                        else self.os_attribute_set)}

        try:
            retval = self.manager.update(self.id, **kwargs)
            self = retval
        except Exception:
            retval = None

        return retval


class OsAttributeAssociationManager(base.CrudManager):
    """Manager class for manipulating Mapping attributes."""
    resource_class = OsAttributeAssociation
    collection_key = 'os_attribute_associations'
    key = 'os_attribute_association'

    def create(self, name, attribute,
               description=None, os_attribute_set=None):
        return super(OsAttributeAssociationManager, self).create(
            name=name,
            description=description,
            attribute=attribute,
            os_attribute_set=os_attribute_set)

    def list(self):
        base_url = None
        return super(OsAttributeAssociationManager, self).list(
            base_url=base_url)

    def get(self, os_attribute_association):
        return super(OsAttributeAssociationManager, self).get(
            os_attribute_association_id=base.getid(os_attribute_association))

    def update(self, os_attribute_association, name=None, description=None,
               attribute=None, os_attribute_set=None):
        return super(OsAttributeAssociationManager, self).update(
            os_attribute_association_id=base.getid(os_attribute_association),
            name=name,
            description=description,
            attribute=attribute,
            os_attribute_set=os_attribute_set)

    def delete(self, os_attribute_association):
        return super(OsAttributeAssociationManager, self).delete(
            os_attribute_association_id=base.getid(os_attribute_association))
