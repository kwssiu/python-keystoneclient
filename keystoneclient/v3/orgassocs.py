# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from keystoneclient import base


class OrgAttributeAssociation(base.Resource):
    """Represents an org_attribute_association.

    Attributes:
        * id: a uuid that identifies the org_attribute_association
        * name: org_attribute_association name
        * description: org_attribute_association description
        * org_attribute_id  ID of OrgAttribute
        * org_attribute_set_id ID of OrgAttributeSet

    """
    def update(self, name=None, description=None,
               org_attribute=None, org_attribute_set_id=None):
        kwargs = {
            'name': name if name is not None else self.name,
            'description': (description
                            if description is not None
                            else self.description),
            'org_attribute': (
                        org_attribute if org_attribute is not None
                        else self.org_attribute),
            'org_attribute_set': (
                        org_attribute_set_id if
                        org_attribute_set_id is not None
                        else self.org_attribute_set_id)}

        try:
            retval = self.manager.update(self.id, **kwargs)
            self = retval
        except Exception:
            retval = None

        return retval


class OrgAttributeAssociationManager(base.CrudManager):
    """Manager class for manipulating Mapping org_attributes."""
    resource_class = OrgAttributeAssociation
    collection_key = 'org_attribute_associations'
    key = 'org_attribute_association'

    def create(self, name, org_attribute,
               description=None, org_attribute_set=None):
        return super(OrgAttributeAssociationManager, self).create(
            name=name,
            description=description,
            org_attribute=org_attribute,
            org_attribute_set=org_attribute_set)

    def list(self):
        base_url = None
        return super(OrgAttributeAssociationManager, self).list(
            base_url=base_url)

    def get(self, org_attribute_association):
        return super(OrgAttributeAssociationManager, self).get(
            org_attribute_association_id=base.getid(org_attribute_association))

    def update(self, org_attribute_association, name=None, description=None,
               org_attribute=None, org_attribute_set=None):
        return super(OrgAttributeAssociationManager, self).update(
            org_attribute_association_id=base.getid(org_attribute_association),
            name=name,
            description=description,
            org_attribute=org_attribute,
            org_attribute_set=org_attribute_set)

    def delete(self, org_attribute_association):
        return super(OrgAttributeAssociationManager, self).delete(
            org_attribute_association_id=base.getid(org_attribute_association))
