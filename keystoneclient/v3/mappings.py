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


class Mapping(base.Resource):
    """Represents a Mapping.

    Attributes:
        * id: a uuid that identifies the attribute
        * name: attribute name
        * description: attribute description
        * org_attribute_set: ID of OrgAttributeSet
        * os_attribute_set: ID of OsAttributeSet

    """
    def update(self, name=None, description=None,
               org_attribute_set=None, os_attribute_set=None):
        kwargs = {
            'name': name if name is not None else self.name,
            'description': (description
                            if description is not None
                            else self.description),
            'org_attribute_set': (
                        org_attribute_set if
                        org_attribute_set is not None
                        else self.org_attribute_set),
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


class MappingManager(base.CrudManager):
    """Manager class for manipulating Mappings."""
    resource_class = Mapping
    collection_key = 'mappings'
    key = 'mapping'

    def create(self, name, org_attribute_set,
               os_attribute_set, description=None):
        return super(MappingManager, self).create(
            name=name,
            description=description,
            org_attribute_set=org_attribute_set,
            os_attribute_set=os_attribute_set)

    def list(self):
        base_url = None
        return super(MappingManager, self).list(
            base_url=base_url)

    def get(self, mapping):
        return super(MappingManager, self).get(
            mapping_id=base.getid(mapping))

    def update(self, mapping, name=None, description=None,
               org_attribute_set=None, os_attribute_set=None):
        return super(MappingManager, self).update(
            mapping_id=base.getid(mapping),
            name=name,
            description=description,
            org_attribute_set=org_attribute_set,
            os_attribute_set=os_attribute_set)

    def delete(self, mapping):
        return super(MappingManager, self).delete(
            mapping_id=base.getid(mapping))
