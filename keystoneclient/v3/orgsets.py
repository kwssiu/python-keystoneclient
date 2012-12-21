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


class OrgAttributeSet(base.Resource):
    """Represents org_attribute_set.

    Attributes:
        * id: a uuid that identifies the org_attribute_set
        * name: org_attribute_set name
        * description: org_attribute_set description

    """
    def update(self, name=None, description=None):
        kwargs = {
            'name': name if name is not None else self.name,
            'description': (description
                            if description is not None
                            else self.description),
        }

        try:
            retval = self.manager.update(self.id, **kwargs)
            self = retval
        except Exception:
            retval = None

        return retval


class OrgAttributeSetManager(base.CrudManager):
    """Manager class for manipulating Identity org_attribute_sets."""
    resource_class = OrgAttributeSet
    collection_key = 'org_attribute_sets'
    key = 'org_attribute_set'

    def create(self, name, domain=None, description=None):
        return super(OrgAttributeSetManager, self).create(
            name=name,
            domain_id=base.getid(domain),
            description=description)

    def list(self, domain=None, user=None):
        if user:
            base_url = '/users/%s' % base.getid(user)
        elif domain:
            base_url = '/domains/%s' % base.getid(domain)
        else:
            base_url = None
        return super(OrgAttributeSetManager, self).list(
            base_url=base_url)

    def get(self, org_attribute_set):
        return super(OrgAttributeSetManager, self).get(
            org_attribute_set_id=base.getid(org_attribute_set))

    def update(self, org_attribute_set, name=None, description=None):
        return super(OrgAttributeSetManager, self).update(
            org_attribute_set_id=base.getid(org_attribute_set),
            name=name,
            description=description)

    def delete(self, org_attribute_set):
        return super(OrgAttributeSetManager, self).delete(
            org_attribute_set_id=base.getid(org_attribute_set))
