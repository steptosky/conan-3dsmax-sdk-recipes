# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#
#
#  Copyright (C) 2017, StepToSky
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1.Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#  2.Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and / or other materials provided with the distribution.
#  3.Neither the name of StepToSky nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED.IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#  Contacts: www.steptosky.com
#
# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#

import os
import sys

# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#
# BUILDING
# Define the flowing variables yourself

# Visual studio is needed for checking created packages.
# You have to specify Visual Studio version you are using.
# 14 - VS2015, 15 - VS2017, 16 - VS2019
visual_studio_version = 17

# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#
# UPLOADING
# Define the flowing variables yourself

# Enable or disable uploading to the conan remote repository
# If it is enabled then after building the package
# it will be uploaded to the specified conan remote repository
# otherwise the package will be only in your local cache.
upload = True

# The remote alias. See "conan remote" in the conan docs.
remote = 'stsff'

# The remote user. See "conan user" in the conan docs.
remote_user = 'stsff'

# The remote password. See "conan user" in the conan docs.
remote_psw = ''


# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#

def replace_in_file(fileFrom, fileTo, data):
    f1 = open(fileFrom, 'r')
    f2 = open(fileTo, 'w')
    for line in f1:
        for d in data:
            line = line.replace(d[0], d[1])
        f2.write(line)
    f1.close()
    f2.close()


def upload_package(pckg_name):
    command = 'conan user %s -r %s -p %s' % (remote_user, remote, remote_psw)
    if os.system(command) != 0:
        raise Exception('conan user problem')
    command = 'conan upload %s/last@steptosky/stable --all -r %s' % (pckg_name, remote)
    if os.system(command) != 0:
        raise Exception('conan upload problem')


def do_package(pckg_name, sdk_version, sdk_dir):
    os.environ["PKG_NAME"] = pckg_name
    os.environ["SDK_VERSION"] = sdk_version
    os.environ["MAX_SDK_DIR"] = sdk_dir
    replace = [('PKG_NAME', pckg_name), ('SDK_VERSION', sdk_version)]
    replace_in_file('conanfile-template.py', 'conanfile.py', replace)

    settings = '-s compiler="Visual Studio" -s compiler.version=%s' % visual_studio_version
    command = 'conan create . %s/last@steptosky/stable --build=%s %s' % (pckg_name, pckg_name, settings)
    if os.system(command) != 0:
        raise Exception('conan create problem')

    command = 'conan remove %s/* -s -b -f' % pckg_name
    if os.system(command) != 0:
        raise Exception('conan remove problem')

    if upload:
        upload_package(pckg_name)


# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#

# PREPARE
# You have to specify the correct path to 3DsMax sdk root folder.
# If you don't want to use all of them just comment necessary lines.
# [package name, 3d max SDK version, path to SDK]
# do_package('3DsMaxSdk9', '9.0', 'W:/Programs/Environments/env_3dmax/maxsdk_9')
# do_package('3DsMaxSdk2008', '10.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2008')
# do_package('3DsMaxSdk2009', '11.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2009')
# do_package('3DsMaxSdk2010', '12.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2010')
# do_package('3DsMaxSdk2011', '13.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2011')
# do_package('3DsMaxSdk2012', '14.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2012')
# do_package('3DsMaxSdk2013', '15.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2013')
# do_package('3DsMaxSdk2014', '16.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2014')
# do_package('3DsMaxSdk2015', '17.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2015')
# do_package('3DsMaxSdk2016', '18.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2016')
# do_package('3DsMaxSdk2017', '19.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2017')
# do_package('3DsMaxSdk2018', '20.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2018')
# do_package('3DsMaxSdk2019', '21.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2019')
# do_package('3DsMaxSdk2020', '22.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2020')
# do_package('3DsMaxSdk2021', '23.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2021')
# do_package('3DsMaxSdk2022', '24.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2022')
# do_package('3DsMaxSdk2023', '25.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2023')
# do_package('3DsMaxSdk2024', '26.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2024')
# do_package('3DsMaxSdk2025', '27.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2025')
# do_package('3DsMaxSdk2026', '28.0', 'W:/Programs/Environments/env_3dmax/maxsdk_2026')

# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#
