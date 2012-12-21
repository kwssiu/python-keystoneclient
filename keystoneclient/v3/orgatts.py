# Copyright 2011 OpenStack LLC.
# Copyright 2011 Nebula, Inc.
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


class OrgAttribute(base.Resource):
    """Represents an org_attribute.

    Attributes:
        * id: a uuid that identifies the org_attribute
        * name: org_attribute name
        * description: org_attribute description
        * type attribute type e.g memberRole
        * value value of the attribute e.g. staff

    """
    def update(self, name=None, description=None, type=None, value=None):
        kwargs = {
            'name': name if name is not None else self.name,
            'description': (description
                            if description is not None
                            else self.description),
            'type': (type if type is not None else self.type),
            'value': (value if value is not None else self.value),
        }

        try:
            retval = self.manager.update(self.id, **kwargs)
            self = retval
        except Exception:
            retval = None

        return retval


class OrgAttributeManager(base.CrudManager):
    """Manager class for manipulating Mapping org_attributes."""
    resource_class = OrgAttribute
    collection_key = 'org_attributes'
    key = 'org_attribute'

    def create(self, name, type, description=None, value=None):
        return super(OrgAttributeManager, self).create(
            name=name,
            description=description,
            type=type,
            value=value)

    def list(self):
        base_url = None
        return super(OrgAttributeManager, self).list(
            base_url=base_url)

    def get(self, org_attribute):
        return super(OrgAttributeManager, self).get(
            org_attribute_id=base.getid(org_attribute))

    def update(self, org_attribute, name=None, description=None,
               type=None, value=None):
        return super(OrgAttributeManager, self).update(
            org_attribute_id=base.getid(org_attribute),
            name=name,
            description=description,
            type=type,
            value=value)

    def delete(self, org_attribute):
        return super(OrgAttributeManager, self).delete(
            org_attribute_id=base.getid(org_attribute))
