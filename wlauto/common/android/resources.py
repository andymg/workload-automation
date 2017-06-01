#    Copyright 2014-2015 ARM Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from wlauto.common.resources import FileResource


class ReventFile(FileResource):

    name = 'revent'

    def __init__(self, owner, stage):
        super(ReventFile, self).__init__(owner)
        self.stage = stage


class JarFile(FileResource):

    name = 'jar'


class ApkFile(FileResource):

    name = 'apk'

    def __init__(self, owner, platform=None):
        super(ApkFile, self).__init__(owner)
        self.platform = platform

    def __str__(self):
        return '<{}\'s {} APK>'.format(self.owner, self.platform)


class uiautoApkFile(FileResource):

    name = 'uiautoapk'

    def __init__(self, owner, platform=None):
        super(uiautoApkFile, self).__init__(owner)
        self.platform = platform

    def __str__(self):
        return '<{}\'s {} UiAuto APK>'.format(self.owner, self.platform)